# 菜鸟-需求预测与分仓规划问题详解

## 1 数据分析

### 1.1 原始数据

​      表：item_feature，样本情况(210549, 31)；

​      表：item_store_feature.shape：(864772, 32)

​      表： config.sape：(5779, 5)     

​      总计有963个不同的样本，预测时间为后面两周（20151228-20160110）的全国和区域分仓目标库存。但是从单独的每个商品分析，商品有段时间会有销量，有限时间会什么都没有，缺失较多，故考虑补差。

 ###  1.2 增加补差样本

​       首先将样本时间20141001-20151227与963个不同的样本做全量笛卡尔积，共计时间样本425646。然后补查后面32个指标。分分仓和全国分别补足，由于交叉后数据量比较大，故只选择（20150701-20151227）的数据做全量生成。并将生成后的全量数据，牵扯到双11，双12的样本时间段删除：（20151021-20151226）数据删除。

​        最终，全国样本个数：115560        缺失值个数：3728条

​                    分仓样本个数：577800        缺失值个数：17063条

​       **注意， 此处将所有缺失值全部补0，因为此处缺失值仅仅是由于的商品当天没有发生点击浏览等原因造成。**

## 2 特征提取

### 2.1标签界定

​        因为数据量少，所以采用滑动窗口提取指标及特征，每天每个商品的时间轴往后滑动14天，这14天内的总计销量作为***label***

### 2.2 [特征提取](../特征描述.xlsx)

1. 原始的商品特征：类目、品牌等，还有历史的一些用户行为特征：浏览人数、加购物车人数，购买人数。

2. 与销量相关组合特征：某些特征相乘，相除等组成。

3. 按照窗口平滑生成特征，平滑时长：1，2，3，4，7，11，14，21，28（根据记忆曲线拐点来确定时间范围。）产生方式：

   以item_id当日前1，2，3，4，7，11，14，21，28天的avg,sum,stddev,属性进行合并。

   以item_id与其他id对应关系，产生总的描述统计特征，叶子类目id特征，大类目ID特征，品牌ID特征，供应商ID特征

4. 事件影响因子：

   最大天数：商品最早出现历史数据的日期距离要预测的那一周的天数。

   最小天数：商品最后一次出现历史数据的日期距离要预测的那一周的天数。

   时间因子：商品时间距离20151228天数。

   详细特征描述详见附件：[特征描述.xls](../特征描述.xlsx)

**详细特征描述详见附件：[特征描述.xls](../特征描述.xlsx)  **

## 3 数据预处理

1. 去掉了11.11与12.12一整天的数据，然后将之前的日期往前平移
2. 奇异值缺失值处理：删除行

​      *奇异值定位：在商品一列平均值的正负3西格玛范围外，即为奇异值*

3. 对label进行log变换

## 4 特征选择

​      使用xgb来筛选特征，选择排名top100的特征，计算相似度，去除冗余特征。

## 5 模型选择与参数调优

### 5.1 模型选择

​       由于事回归类问题预测，故选用回归类模型

1. rf：基于boostrap重抽样和随机选取特征，基预测器是决策树的集成方法，并行处理速度快，泛化能力强,可以很好的避免过拟合，对于不平衡数据集可以平衡误差。
2. gbrt：基于boosting方法，提升方向是梯度方向的决策树的集成方法，精度高;可以发现多种有区分性的特征以及特征组合
3. xgboost：对目标函数做了二阶导数，主要改进是使用了正则化和特征分块存储并行处理
4. Adaboost：可以使用各种回归分类模型来构建弱学习器，非常灵活
5. Rule：预测窗口前两周的销量分别记作week1,week2，对每个(item，store_ code)，如果补少成本大于补多成本，则预测为2* max(week1,week2)，反之预测为2* min(week1,week2)

### 5.2参数调优

​      用agboost举例，首先根据经验，确定几个需要调整的参数，然后用xgb.cv 进行调参

1. booster: gbtree  ，objective: reg:linear ，eval_metric: rmse


2. eta: 0.008, [default=0.3] ，为了防止过拟合，通常最后设置eta为0.01~0.2，通过交叉验证（xgb.cv ) 进行调参, 本文为0.008，0.009
3. gamma, [default=0] 
4. max_depth: 7, [default=6]，通过交叉验证（xgb.cv ) 进行调参，本文最终为6-8之间 
5. lambda：100, [default=0] , L2 正则的惩罚系数,用来降低过拟合
6. subsample: 0.7, [default=1] 用于训练模型的子样本占整个样本集合的比例(0, 1]
7. colsample_bytree: 0.7 [default=1] 
8. seed:1024,[ default=0 ] ;  nthread: 8 ,XGBoost运行时的线程数 ;
9. num_boost_round=500提升迭代的个数

##  6 模型融合

6.1 model1 = model in  (RF,GBRT,XGBOOST,Adaboost),按照商品成本做融合,补多成本大，则选择min(models),补少成本大选择    max(models).

6.2 model = 0.25rule + 0.75model1,最终模型，加入规则，加权而得。