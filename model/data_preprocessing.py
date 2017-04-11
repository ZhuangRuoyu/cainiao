#coding=utf-8

"""
对原始数据做预处理，添加字段名，划分补少、补多成本字段

"""

import pandas as pd

config = pd.read_csv('../data/config2.csv',header=None)
config.columns = ['item_id','store_code','a_b']
config['a'] = config['a_b'].apply(lambda x:float(x.split('_')[0]))
config['b'] = config['a_b'].apply(lambda x:float(x.split('_')[1]))
config.to_csv('../data/config2.csv',index=None)


item_feature = pd.read_csv('/Users/hyy/Downloads/CAINIAO/item_feature2.csv',header=None)
item_feature.columns = ['date','item_id','cate_id','cate_level_id','brand_id','supplier_id','pv_ipv','pv_uv','cart_ipv','cart_uv','collect_uv','num_gmv',
'amt_gmv','qty_gmv','unum_gmv','amt_alipay','num_alipay','qty_alipay','unum_alipay','ztc_pv_ipv','tbk_pv_ipv','ss_pv_ipv','jhs_pv_ipv','ztc_pv_uv',
'tbk_pv_uv','ss_pv_uv','jhs_pv_uv','num_alipay_njhs','amt_alipay_njhs','qty_alipay_njhs','unum_alipay_njhs']
item_feature.to_csv('../data/item_feature2.csv',index=None)

item_store_feature = pd.read_csv('../data/item_store_feature2.csv',header=None)
item_store_feature.columns = ['date','item_id','store_code','cate_id','cate_level_id','brand_id','supplier_id','pv_ipv','pv_uv','cart_ipv','cart_uv','collect_uv','num_gmv',
'amt_gmv','qty_gmv','unum_gmv','amt_alipay','num_alipay','qty_alipay','unum_alipay','ztc_pv_ipv','tbk_pv_ipv','ss_pv_ipv','jhs_pv_ipv',
'ztc_pv_uv','tbk_pv_uv','ss_pv_uv','jhs_pv_uv','num_alipay_njhs','amt_alipay_njhs','qty_alipay_njhs','unum_alipay_njhs']
item_store_feature.to_csv('../data/item_store_feature2.csv',index=None)


train_all = pd.read_csv('/Applications/dev/tmp/train_all.csv',header=None)
train_all.columns = ['watch','store_code','item_id','label','pv_ipv_1','pv_uv_1','cart_ipv_1','cart_uv_1','collect_uv_1','num_gmv_1','amt_gmv_1','qty_gmv_1','unum_gmv_1','amt_alipay_1','num_alipay_1','qty_alipay_1','unum_alipay_1','ztc_pv_ipv_1','tbk_pv_ipv_1','ss_pv_ipv_1','jhs_pv_ipv_1','ztc_pv_uv_1','tbk_pv_uv_1','ss_pv_uv_1','jhs_pv_uv_1','num_alipay_njhs_1','amt_alipay_njhs_1','qty_alipay_njhs_1','unum_alipay_njhs_1','pv_ipv_sum_1','pv_uv_sum_1','cart_ipv_sum_1','cart_uv_sum_1','collect_uv_sum_1','num_gmv_sum_1','amt_gmv_sum_1','qty_gmv_sum_1','unum_gmv_sum_1','amt_alipay_sum_1','num_alipay_sum_1','qty_alipay_sum_1','unum_alipay_sum_1','ztc_pv_ipv_sum_1','tbk_pv_ipv_sum_1','ss_pv_ipv_sum_1','jhs_pv_ipv_sum_1','ztc_pv_uv_sum_1','tbk_pv_uv_sum_1','ss_pv_uv_sum_1','jhs_pv_uv_sum_1','num_alipay_njhs_sum_1','amt_alipay_njhs_sum_1','qty_alipay_njhs_sum_1','unum_alipay_njhs_sum_1','pv_ipv_2','pv_uv_2','cart_ipv_2','cart_uv_2','collect_uv_2','num_gmv_2','amt_gmv_2','qty_gmv_2','unum_gmv_2','amt_alipay_2','num_alipay_2','qty_alipay_2','unum_alipay_2','ztc_pv_ipv_2','tbk_pv_ipv_2','ss_pv_ipv_2','jhs_pv_ipv_2','ztc_pv_uv_2','tbk_pv_uv_2','ss_pv_uv_2','jhs_pv_uv_2','num_alipay_njhs_2','amt_alipay_njhs_2','qty_alipay_njhs_2','unum_alipay_njhs_2','pv_ipv_sum_2','pv_uv_sum_2','cart_ipv_sum_2','cart_uv_sum_2','collect_uv_sum_2','num_gmv_sum_2','amt_gmv_sum_2','qty_gmv_sum_2','unum_gmv_sum_2','amt_alipay_sum_2','num_alipay_sum_2','qty_alipay_sum_2','unum_alipay_sum_2','ztc_pv_ipv_sum_2','tbk_pv_ipv_sum_2','ss_pv_ipv_sum_2','jhs_pv_ipv_sum_2','ztc_pv_uv_sum_2','tbk_pv_uv_sum_2','ss_pv_uv_sum_2','jhs_pv_uv_sum_2','num_alipay_njhs_sum_2','amt_alipay_njhs_sum_2','qty_alipay_njhs_sum_2','unum_alipay_njhs_sum_2','pv_ipv_3','pv_uv_3','cart_ipv_3','cart_uv_3','collect_uv_3','num_gmv_3','amt_gmv_3','qty_gmv_3','unum_gmv_3','amt_alipay_3','num_alipay_3','qty_alipay_3','unum_alipay_3','ztc_pv_ipv_3','tbk_pv_ipv_3','ss_pv_ipv_3','jhs_pv_ipv_3','ztc_pv_uv_3','tbk_pv_uv_3','ss_pv_uv_3','jhs_pv_uv_3','num_alipay_njhs_3','amt_alipay_njhs_3','qty_alipay_njhs_3','unum_alipay_njhs_3','pv_ipv_sum_3','pv_uv_sum_3','cart_ipv_sum_3','cart_uv_sum_3','collect_uv_sum_3','num_gmv_sum_3','amt_gmv_sum_3','qty_gmv_sum_3','unum_gmv_sum_3','amt_alipay_sum_3','num_alipay_sum_3','qty_alipay_sum_3','unum_alipay_sum_3','ztc_pv_ipv_sum_3','tbk_pv_ipv_sum_3','ss_pv_ipv_sum_3','jhs_pv_ipv_sum_3','ztc_pv_uv_sum_3','tbk_pv_uv_sum_3','ss_pv_uv_sum_3','jhs_pv_uv_sum_3','num_alipay_njhs_sum_3','amt_alipay_njhs_sum_3','qty_alipay_njhs_sum_3','unum_alipay_njhs_sum_3','pv_ipv_5','pv_uv_5','cart_ipv_5','cart_uv_5','collect_uv_5','num_gmv_5','amt_gmv_5','qty_gmv_5','unum_gmv_5','amt_alipay_5','num_alipay_5','qty_alipay_5','unum_alipay_5','ztc_pv_ipv_5','tbk_pv_ipv_5','ss_pv_ipv_5','jhs_pv_ipv_5','ztc_pv_uv_5','tbk_pv_uv_5','ss_pv_uv_5','jhs_pv_uv_5','num_alipay_njhs_5','amt_alipay_njhs_5','qty_alipay_njhs_5','unum_alipay_njhs_5','pv_ipv_sum_5','pv_uv_sum_5','cart_ipv_sum_5','cart_uv_sum_5','collect_uv_sum_5','num_gmv_sum_5','amt_gmv_sum_5','qty_gmv_sum_5','unum_gmv_sum_5','amt_alipay_sum_5','num_alipay_sum_5','qty_alipay_sum_5','unum_alipay_sum_5','ztc_pv_ipv_sum_5','tbk_pv_ipv_sum_5','ss_pv_ipv_sum_5','jhs_pv_ipv_sum_5','ztc_pv_uv_sum_5','tbk_pv_uv_sum_5','ss_pv_uv_sum_5','jhs_pv_uv_sum_5','num_alipay_njhs_sum_5','amt_alipay_njhs_sum_5','qty_alipay_njhs_sum_5','unum_alipay_njhs_sum_5','pv_ipv_7','pv_uv_7','cart_ipv_7','cart_uv_7','collect_uv_7','num_gmv_7','amt_gmv_7','qty_gmv_7','unum_gmv_7','amt_alipay_7','num_alipay_7','qty_alipay_7','unum_alipay_7','ztc_pv_ipv_7','tbk_pv_ipv_7','ss_pv_ipv_7','jhs_pv_ipv_7','ztc_pv_uv_7','tbk_pv_uv_7','ss_pv_uv_7','jhs_pv_uv_7','num_alipay_njhs_7','amt_alipay_njhs_7','qty_alipay_njhs_7','unum_alipay_njhs_7','pv_ipv_sum_7','pv_uv_sum_7','cart_ipv_sum_7','cart_uv_sum_7','collect_uv_sum_7','num_gmv_sum_7','amt_gmv_sum_7','qty_gmv_sum_7','unum_gmv_sum_7','amt_alipay_sum_7','num_alipay_sum_7','qty_alipay_sum_7','unum_alipay_sum_7','ztc_pv_ipv_sum_7','tbk_pv_ipv_sum_7','ss_pv_ipv_sum_7','jhs_pv_ipv_sum_7','ztc_pv_uv_sum_7','tbk_pv_uv_sum_7','ss_pv_uv_sum_7','jhs_pv_uv_sum_7','num_alipay_njhs_sum_7','amt_alipay_njhs_sum_7','qty_alipay_njhs_sum_7','unum_alipay_njhs_sum_7','pv_ipv_9','pv_uv_9','cart_ipv_9','cart_uv_9','collect_uv_9','num_gmv_9','amt_gmv_9','qty_gmv_9','unum_gmv_9','amt_alipay_9','num_alipay_9','qty_alipay_9','unum_alipay_9','ztc_pv_ipv_9','tbk_pv_ipv_9','ss_pv_ipv_9','jhs_pv_ipv_9','ztc_pv_uv_9','tbk_pv_uv_9','ss_pv_uv_9','jhs_pv_uv_9','num_alipay_njhs_9','amt_alipay_njhs_9','qty_alipay_njhs_9','unum_alipay_njhs_9','pv_ipv_sum_9','pv_uv_sum_9','cart_ipv_sum_9','cart_uv_sum_9','collect_uv_sum_9','num_gmv_sum_9','amt_gmv_sum_9','qty_gmv_sum_9','unum_gmv_sum_9','amt_alipay_sum_9','num_alipay_sum_9','qty_alipay_sum_9','unum_alipay_sum_9','ztc_pv_ipv_sum_9','tbk_pv_ipv_sum_9','ss_pv_ipv_sum_9','jhs_pv_ipv_sum_9','ztc_pv_uv_sum_9','tbk_pv_uv_sum_9','ss_pv_uv_sum_9','jhs_pv_uv_sum_9','num_alipay_njhs_sum_9','amt_alipay_njhs_sum_9','qty_alipay_njhs_sum_9','unum_alipay_njhs_sum_9','pv_ipv_11','pv_uv_11','cart_ipv_11','cart_uv_11','collect_uv_11','num_gmv_11','amt_gmv_11','qty_gmv_11','unum_gmv_11','amt_alipay_11','num_alipay_11','qty_alipay_11','unum_alipay_11','ztc_pv_ipv_11','tbk_pv_ipv_11','ss_pv_ipv_11','jhs_pv_ipv_11','ztc_pv_uv_11','tbk_pv_uv_11','ss_pv_uv_11','jhs_pv_uv_11','num_alipay_njhs_11','amt_alipay_njhs_11','qty_alipay_njhs_11','unum_alipay_njhs_11','pv_ipv_sum_11','pv_uv_sum_11','cart_ipv_sum_11','cart_uv_sum_11','collect_uv_sum_11','num_gmv_sum_11','amt_gmv_sum_11','qty_gmv_sum_11','unum_gmv_sum_11','amt_alipay_sum_11','num_alipay_sum_11','qty_alipay_sum_11','unum_alipay_sum_11','ztc_pv_ipv_sum_11','tbk_pv_ipv_sum_11','ss_pv_ipv_sum_11','jhs_pv_ipv_sum_11','ztc_pv_uv_sum_11','tbk_pv_uv_sum_11','ss_pv_uv_sum_11','jhs_pv_uv_sum_11','num_alipay_njhs_sum_11','amt_alipay_njhs_sum_11','qty_alipay_njhs_sum_11','unum_alipay_njhs_sum_11','pv_ipv_14','pv_uv_14','cart_ipv_14','cart_uv_14','collect_uv_14','num_gmv_14','amt_gmv_14','qty_gmv_14','unum_gmv_14','amt_alipay_14','num_alipay_14','qty_alipay_14','unum_alipay_14','ztc_pv_ipv_14','tbk_pv_ipv_14','ss_pv_ipv_14','jhs_pv_ipv_14','ztc_pv_uv_14','tbk_pv_uv_14','ss_pv_uv_14','jhs_pv_uv_14','num_alipay_njhs_14','amt_alipay_njhs_14','qty_alipay_njhs_14','unum_alipay_njhs_14','pv_ipv_sum_14','pv_uv_sum_14','cart_ipv_sum_14','cart_uv_sum_14','collect_uv_sum_14','num_gmv_sum_14','amt_gmv_sum_14','qty_gmv_sum_14','unum_gmv_sum_14','amt_alipay_sum_14','num_alipay_sum_14','qty_alipay_sum_14','unum_alipay_sum_14','ztc_pv_ipv_sum_14','tbk_pv_ipv_sum_14','ss_pv_ipv_sum_14','jhs_pv_ipv_sum_14','ztc_pv_uv_sum_14','tbk_pv_uv_sum_14','ss_pv_uv_sum_14','jhs_pv_uv_sum_14','num_alipay_njhs_sum_14','amt_alipay_njhs_sum_14','qty_alipay_njhs_sum_14','unum_alipay_njhs_sum_14','max_qty_alipay_njhs','min_qty_alipay_njhs','std_qty_alipay_njhs','cate_id_qty_alipay_njhs_sum','cate_id_qty_alipay_njhs_avg','cate_id_qty_alipay_njhs_std','cate_level_id_qty_alipay_njhs_sum','cate_level_id_qty_alipay_njhs_avg','cate_level_id_qty_alipay_njhs_std','brand_id_qty_alipay_njhs_sum','brand_id_qty_alipay_njhs_avg','brand_id_qty_alipay_njhs_std','supplier_id_qty_alipay_njhs_sum','supplier_id_qty_alipay_njhs_avg','supplier_id_qty_alipay_njhs_std']
test_all = pd.read_csv('/Applications/dev/tmp/test_all.csv',header=None)
test_all.columns = ['watch','store_code','item_id','label','pv_ipv_1','pv_uv_1','cart_ipv_1','cart_uv_1','collect_uv_1','num_gmv_1','amt_gmv_1','qty_gmv_1','unum_gmv_1','amt_alipay_1','num_alipay_1','qty_alipay_1','unum_alipay_1','ztc_pv_ipv_1','tbk_pv_ipv_1','ss_pv_ipv_1','jhs_pv_ipv_1','ztc_pv_uv_1','tbk_pv_uv_1','ss_pv_uv_1','jhs_pv_uv_1','num_alipay_njhs_1','amt_alipay_njhs_1','qty_alipay_njhs_1','unum_alipay_njhs_1','pv_ipv_sum_1','pv_uv_sum_1','cart_ipv_sum_1','cart_uv_sum_1','collect_uv_sum_1','num_gmv_sum_1','amt_gmv_sum_1','qty_gmv_sum_1','unum_gmv_sum_1','amt_alipay_sum_1','num_alipay_sum_1','qty_alipay_sum_1','unum_alipay_sum_1','ztc_pv_ipv_sum_1','tbk_pv_ipv_sum_1','ss_pv_ipv_sum_1','jhs_pv_ipv_sum_1','ztc_pv_uv_sum_1','tbk_pv_uv_sum_1','ss_pv_uv_sum_1','jhs_pv_uv_sum_1','num_alipay_njhs_sum_1','amt_alipay_njhs_sum_1','qty_alipay_njhs_sum_1','unum_alipay_njhs_sum_1','pv_ipv_2','pv_uv_2','cart_ipv_2','cart_uv_2','collect_uv_2','num_gmv_2','amt_gmv_2','qty_gmv_2','unum_gmv_2','amt_alipay_2','num_alipay_2','qty_alipay_2','unum_alipay_2','ztc_pv_ipv_2','tbk_pv_ipv_2','ss_pv_ipv_2','jhs_pv_ipv_2','ztc_pv_uv_2','tbk_pv_uv_2','ss_pv_uv_2','jhs_pv_uv_2','num_alipay_njhs_2','amt_alipay_njhs_2','qty_alipay_njhs_2','unum_alipay_njhs_2','pv_ipv_sum_2','pv_uv_sum_2','cart_ipv_sum_2','cart_uv_sum_2','collect_uv_sum_2','num_gmv_sum_2','amt_gmv_sum_2','qty_gmv_sum_2','unum_gmv_sum_2','amt_alipay_sum_2','num_alipay_sum_2','qty_alipay_sum_2','unum_alipay_sum_2','ztc_pv_ipv_sum_2','tbk_pv_ipv_sum_2','ss_pv_ipv_sum_2','jhs_pv_ipv_sum_2','ztc_pv_uv_sum_2','tbk_pv_uv_sum_2','ss_pv_uv_sum_2','jhs_pv_uv_sum_2','num_alipay_njhs_sum_2','amt_alipay_njhs_sum_2','qty_alipay_njhs_sum_2','unum_alipay_njhs_sum_2','pv_ipv_3','pv_uv_3','cart_ipv_3','cart_uv_3','collect_uv_3','num_gmv_3','amt_gmv_3','qty_gmv_3','unum_gmv_3','amt_alipay_3','num_alipay_3','qty_alipay_3','unum_alipay_3','ztc_pv_ipv_3','tbk_pv_ipv_3','ss_pv_ipv_3','jhs_pv_ipv_3','ztc_pv_uv_3','tbk_pv_uv_3','ss_pv_uv_3','jhs_pv_uv_3','num_alipay_njhs_3','amt_alipay_njhs_3','qty_alipay_njhs_3','unum_alipay_njhs_3','pv_ipv_sum_3','pv_uv_sum_3','cart_ipv_sum_3','cart_uv_sum_3','collect_uv_sum_3','num_gmv_sum_3','amt_gmv_sum_3','qty_gmv_sum_3','unum_gmv_sum_3','amt_alipay_sum_3','num_alipay_sum_3','qty_alipay_sum_3','unum_alipay_sum_3','ztc_pv_ipv_sum_3','tbk_pv_ipv_sum_3','ss_pv_ipv_sum_3','jhs_pv_ipv_sum_3','ztc_pv_uv_sum_3','tbk_pv_uv_sum_3','ss_pv_uv_sum_3','jhs_pv_uv_sum_3','num_alipay_njhs_sum_3','amt_alipay_njhs_sum_3','qty_alipay_njhs_sum_3','unum_alipay_njhs_sum_3','pv_ipv_5','pv_uv_5','cart_ipv_5','cart_uv_5','collect_uv_5','num_gmv_5','amt_gmv_5','qty_gmv_5','unum_gmv_5','amt_alipay_5','num_alipay_5','qty_alipay_5','unum_alipay_5','ztc_pv_ipv_5','tbk_pv_ipv_5','ss_pv_ipv_5','jhs_pv_ipv_5','ztc_pv_uv_5','tbk_pv_uv_5','ss_pv_uv_5','jhs_pv_uv_5','num_alipay_njhs_5','amt_alipay_njhs_5','qty_alipay_njhs_5','unum_alipay_njhs_5','pv_ipv_sum_5','pv_uv_sum_5','cart_ipv_sum_5','cart_uv_sum_5','collect_uv_sum_5','num_gmv_sum_5','amt_gmv_sum_5','qty_gmv_sum_5','unum_gmv_sum_5','amt_alipay_sum_5','num_alipay_sum_5','qty_alipay_sum_5','unum_alipay_sum_5','ztc_pv_ipv_sum_5','tbk_pv_ipv_sum_5','ss_pv_ipv_sum_5','jhs_pv_ipv_sum_5','ztc_pv_uv_sum_5','tbk_pv_uv_sum_5','ss_pv_uv_sum_5','jhs_pv_uv_sum_5','num_alipay_njhs_sum_5','amt_alipay_njhs_sum_5','qty_alipay_njhs_sum_5','unum_alipay_njhs_sum_5','pv_ipv_7','pv_uv_7','cart_ipv_7','cart_uv_7','collect_uv_7','num_gmv_7','amt_gmv_7','qty_gmv_7','unum_gmv_7','amt_alipay_7','num_alipay_7','qty_alipay_7','unum_alipay_7','ztc_pv_ipv_7','tbk_pv_ipv_7','ss_pv_ipv_7','jhs_pv_ipv_7','ztc_pv_uv_7','tbk_pv_uv_7','ss_pv_uv_7','jhs_pv_uv_7','num_alipay_njhs_7','amt_alipay_njhs_7','qty_alipay_njhs_7','unum_alipay_njhs_7','pv_ipv_sum_7','pv_uv_sum_7','cart_ipv_sum_7','cart_uv_sum_7','collect_uv_sum_7','num_gmv_sum_7','amt_gmv_sum_7','qty_gmv_sum_7','unum_gmv_sum_7','amt_alipay_sum_7','num_alipay_sum_7','qty_alipay_sum_7','unum_alipay_sum_7','ztc_pv_ipv_sum_7','tbk_pv_ipv_sum_7','ss_pv_ipv_sum_7','jhs_pv_ipv_sum_7','ztc_pv_uv_sum_7','tbk_pv_uv_sum_7','ss_pv_uv_sum_7','jhs_pv_uv_sum_7','num_alipay_njhs_sum_7','amt_alipay_njhs_sum_7','qty_alipay_njhs_sum_7','unum_alipay_njhs_sum_7','pv_ipv_9','pv_uv_9','cart_ipv_9','cart_uv_9','collect_uv_9','num_gmv_9','amt_gmv_9','qty_gmv_9','unum_gmv_9','amt_alipay_9','num_alipay_9','qty_alipay_9','unum_alipay_9','ztc_pv_ipv_9','tbk_pv_ipv_9','ss_pv_ipv_9','jhs_pv_ipv_9','ztc_pv_uv_9','tbk_pv_uv_9','ss_pv_uv_9','jhs_pv_uv_9','num_alipay_njhs_9','amt_alipay_njhs_9','qty_alipay_njhs_9','unum_alipay_njhs_9','pv_ipv_sum_9','pv_uv_sum_9','cart_ipv_sum_9','cart_uv_sum_9','collect_uv_sum_9','num_gmv_sum_9','amt_gmv_sum_9','qty_gmv_sum_9','unum_gmv_sum_9','amt_alipay_sum_9','num_alipay_sum_9','qty_alipay_sum_9','unum_alipay_sum_9','ztc_pv_ipv_sum_9','tbk_pv_ipv_sum_9','ss_pv_ipv_sum_9','jhs_pv_ipv_sum_9','ztc_pv_uv_sum_9','tbk_pv_uv_sum_9','ss_pv_uv_sum_9','jhs_pv_uv_sum_9','num_alipay_njhs_sum_9','amt_alipay_njhs_sum_9','qty_alipay_njhs_sum_9','unum_alipay_njhs_sum_9','pv_ipv_11','pv_uv_11','cart_ipv_11','cart_uv_11','collect_uv_11','num_gmv_11','amt_gmv_11','qty_gmv_11','unum_gmv_11','amt_alipay_11','num_alipay_11','qty_alipay_11','unum_alipay_11','ztc_pv_ipv_11','tbk_pv_ipv_11','ss_pv_ipv_11','jhs_pv_ipv_11','ztc_pv_uv_11','tbk_pv_uv_11','ss_pv_uv_11','jhs_pv_uv_11','num_alipay_njhs_11','amt_alipay_njhs_11','qty_alipay_njhs_11','unum_alipay_njhs_11','pv_ipv_sum_11','pv_uv_sum_11','cart_ipv_sum_11','cart_uv_sum_11','collect_uv_sum_11','num_gmv_sum_11','amt_gmv_sum_11','qty_gmv_sum_11','unum_gmv_sum_11','amt_alipay_sum_11','num_alipay_sum_11','qty_alipay_sum_11','unum_alipay_sum_11','ztc_pv_ipv_sum_11','tbk_pv_ipv_sum_11','ss_pv_ipv_sum_11','jhs_pv_ipv_sum_11','ztc_pv_uv_sum_11','tbk_pv_uv_sum_11','ss_pv_uv_sum_11','jhs_pv_uv_sum_11','num_alipay_njhs_sum_11','amt_alipay_njhs_sum_11','qty_alipay_njhs_sum_11','unum_alipay_njhs_sum_11','pv_ipv_14','pv_uv_14','cart_ipv_14','cart_uv_14','collect_uv_14','num_gmv_14','amt_gmv_14','qty_gmv_14','unum_gmv_14','amt_alipay_14','num_alipay_14','qty_alipay_14','unum_alipay_14','ztc_pv_ipv_14','tbk_pv_ipv_14','ss_pv_ipv_14','jhs_pv_ipv_14','ztc_pv_uv_14','tbk_pv_uv_14','ss_pv_uv_14','jhs_pv_uv_14','num_alipay_njhs_14','amt_alipay_njhs_14','qty_alipay_njhs_14','unum_alipay_njhs_14','pv_ipv_sum_14','pv_uv_sum_14','cart_ipv_sum_14','cart_uv_sum_14','collect_uv_sum_14','num_gmv_sum_14','amt_gmv_sum_14','qty_gmv_sum_14','unum_gmv_sum_14','amt_alipay_sum_14','num_alipay_sum_14','qty_alipay_sum_14','unum_alipay_sum_14','ztc_pv_ipv_sum_14','tbk_pv_ipv_sum_14','ss_pv_ipv_sum_14','jhs_pv_ipv_sum_14','ztc_pv_uv_sum_14','tbk_pv_uv_sum_14','ss_pv_uv_sum_14','jhs_pv_uv_sum_14','num_alipay_njhs_sum_14','amt_alipay_njhs_sum_14','qty_alipay_njhs_sum_14','unum_alipay_njhs_sum_14','max_qty_alipay_njhs','min_qty_alipay_njhs','std_qty_alipay_njhs','cate_id_qty_alipay_njhs_sum','cate_id_qty_alipay_njhs_avg','cate_id_qty_alipay_njhs_std','cate_level_id_qty_alipay_njhs_sum','cate_level_id_qty_alipay_njhs_avg','cate_level_id_qty_alipay_njhs_std','brand_id_qty_alipay_njhs_sum','brand_id_qty_alipay_njhs_avg','brand_id_qty_alipay_njhs_std','supplier_id_qty_alipay_njhs_sum','supplier_id_qty_alipay_njhs_avg','supplier_id_qty_alipay_njhs_std']
train_fencang = pd.read_csv('/Applications/dev/tmp/train_fencang.csv',header=None)
train_fencang.columns = ['watch','store_code','item_id','label','pv_ipv_1','pv_uv_1','cart_ipv_1','cart_uv_1','collect_uv_1','num_gmv_1','amt_gmv_1','qty_gmv_1','unum_gmv_1','amt_alipay_1','num_alipay_1','qty_alipay_1','unum_alipay_1','ztc_pv_ipv_1','tbk_pv_ipv_1','ss_pv_ipv_1','jhs_pv_ipv_1','ztc_pv_uv_1','tbk_pv_uv_1','ss_pv_uv_1','jhs_pv_uv_1','num_alipay_njhs_1','amt_alipay_njhs_1','qty_alipay_njhs_1','unum_alipay_njhs_1','pv_ipv_sum_1','pv_uv_sum_1','cart_ipv_sum_1','cart_uv_sum_1','collect_uv_sum_1','num_gmv_sum_1','amt_gmv_sum_1','qty_gmv_sum_1','unum_gmv_sum_1','amt_alipay_sum_1','num_alipay_sum_1','qty_alipay_sum_1','unum_alipay_sum_1','ztc_pv_ipv_sum_1','tbk_pv_ipv_sum_1','ss_pv_ipv_sum_1','jhs_pv_ipv_sum_1','ztc_pv_uv_sum_1','tbk_pv_uv_sum_1','ss_pv_uv_sum_1','jhs_pv_uv_sum_1','num_alipay_njhs_sum_1','amt_alipay_njhs_sum_1','qty_alipay_njhs_sum_1','unum_alipay_njhs_sum_1','pv_ipv_2','pv_uv_2','cart_ipv_2','cart_uv_2','collect_uv_2','num_gmv_2','amt_gmv_2','qty_gmv_2','unum_gmv_2','amt_alipay_2','num_alipay_2','qty_alipay_2','unum_alipay_2','ztc_pv_ipv_2','tbk_pv_ipv_2','ss_pv_ipv_2','jhs_pv_ipv_2','ztc_pv_uv_2','tbk_pv_uv_2','ss_pv_uv_2','jhs_pv_uv_2','num_alipay_njhs_2','amt_alipay_njhs_2','qty_alipay_njhs_2','unum_alipay_njhs_2','pv_ipv_sum_2','pv_uv_sum_2','cart_ipv_sum_2','cart_uv_sum_2','collect_uv_sum_2','num_gmv_sum_2','amt_gmv_sum_2','qty_gmv_sum_2','unum_gmv_sum_2','amt_alipay_sum_2','num_alipay_sum_2','qty_alipay_sum_2','unum_alipay_sum_2','ztc_pv_ipv_sum_2','tbk_pv_ipv_sum_2','ss_pv_ipv_sum_2','jhs_pv_ipv_sum_2','ztc_pv_uv_sum_2','tbk_pv_uv_sum_2','ss_pv_uv_sum_2','jhs_pv_uv_sum_2','num_alipay_njhs_sum_2','amt_alipay_njhs_sum_2','qty_alipay_njhs_sum_2','unum_alipay_njhs_sum_2','pv_ipv_3','pv_uv_3','cart_ipv_3','cart_uv_3','collect_uv_3','num_gmv_3','amt_gmv_3','qty_gmv_3','unum_gmv_3','amt_alipay_3','num_alipay_3','qty_alipay_3','unum_alipay_3','ztc_pv_ipv_3','tbk_pv_ipv_3','ss_pv_ipv_3','jhs_pv_ipv_3','ztc_pv_uv_3','tbk_pv_uv_3','ss_pv_uv_3','jhs_pv_uv_3','num_alipay_njhs_3','amt_alipay_njhs_3','qty_alipay_njhs_3','unum_alipay_njhs_3','pv_ipv_sum_3','pv_uv_sum_3','cart_ipv_sum_3','cart_uv_sum_3','collect_uv_sum_3','num_gmv_sum_3','amt_gmv_sum_3','qty_gmv_sum_3','unum_gmv_sum_3','amt_alipay_sum_3','num_alipay_sum_3','qty_alipay_sum_3','unum_alipay_sum_3','ztc_pv_ipv_sum_3','tbk_pv_ipv_sum_3','ss_pv_ipv_sum_3','jhs_pv_ipv_sum_3','ztc_pv_uv_sum_3','tbk_pv_uv_sum_3','ss_pv_uv_sum_3','jhs_pv_uv_sum_3','num_alipay_njhs_sum_3','amt_alipay_njhs_sum_3','qty_alipay_njhs_sum_3','unum_alipay_njhs_sum_3','pv_ipv_5','pv_uv_5','cart_ipv_5','cart_uv_5','collect_uv_5','num_gmv_5','amt_gmv_5','qty_gmv_5','unum_gmv_5','amt_alipay_5','num_alipay_5','qty_alipay_5','unum_alipay_5','ztc_pv_ipv_5','tbk_pv_ipv_5','ss_pv_ipv_5','jhs_pv_ipv_5','ztc_pv_uv_5','tbk_pv_uv_5','ss_pv_uv_5','jhs_pv_uv_5','num_alipay_njhs_5','amt_alipay_njhs_5','qty_alipay_njhs_5','unum_alipay_njhs_5','pv_ipv_sum_5','pv_uv_sum_5','cart_ipv_sum_5','cart_uv_sum_5','collect_uv_sum_5','num_gmv_sum_5','amt_gmv_sum_5','qty_gmv_sum_5','unum_gmv_sum_5','amt_alipay_sum_5','num_alipay_sum_5','qty_alipay_sum_5','unum_alipay_sum_5','ztc_pv_ipv_sum_5','tbk_pv_ipv_sum_5','ss_pv_ipv_sum_5','jhs_pv_ipv_sum_5','ztc_pv_uv_sum_5','tbk_pv_uv_sum_5','ss_pv_uv_sum_5','jhs_pv_uv_sum_5','num_alipay_njhs_sum_5','amt_alipay_njhs_sum_5','qty_alipay_njhs_sum_5','unum_alipay_njhs_sum_5','pv_ipv_7','pv_uv_7','cart_ipv_7','cart_uv_7','collect_uv_7','num_gmv_7','amt_gmv_7','qty_gmv_7','unum_gmv_7','amt_alipay_7','num_alipay_7','qty_alipay_7','unum_alipay_7','ztc_pv_ipv_7','tbk_pv_ipv_7','ss_pv_ipv_7','jhs_pv_ipv_7','ztc_pv_uv_7','tbk_pv_uv_7','ss_pv_uv_7','jhs_pv_uv_7','num_alipay_njhs_7','amt_alipay_njhs_7','qty_alipay_njhs_7','unum_alipay_njhs_7','pv_ipv_sum_7','pv_uv_sum_7','cart_ipv_sum_7','cart_uv_sum_7','collect_uv_sum_7','num_gmv_sum_7','amt_gmv_sum_7','qty_gmv_sum_7','unum_gmv_sum_7','amt_alipay_sum_7','num_alipay_sum_7','qty_alipay_sum_7','unum_alipay_sum_7','ztc_pv_ipv_sum_7','tbk_pv_ipv_sum_7','ss_pv_ipv_sum_7','jhs_pv_ipv_sum_7','ztc_pv_uv_sum_7','tbk_pv_uv_sum_7','ss_pv_uv_sum_7','jhs_pv_uv_sum_7','num_alipay_njhs_sum_7','amt_alipay_njhs_sum_7','qty_alipay_njhs_sum_7','unum_alipay_njhs_sum_7','pv_ipv_9','pv_uv_9','cart_ipv_9','cart_uv_9','collect_uv_9','num_gmv_9','amt_gmv_9','qty_gmv_9','unum_gmv_9','amt_alipay_9','num_alipay_9','qty_alipay_9','unum_alipay_9','ztc_pv_ipv_9','tbk_pv_ipv_9','ss_pv_ipv_9','jhs_pv_ipv_9','ztc_pv_uv_9','tbk_pv_uv_9','ss_pv_uv_9','jhs_pv_uv_9','num_alipay_njhs_9','amt_alipay_njhs_9','qty_alipay_njhs_9','unum_alipay_njhs_9','pv_ipv_sum_9','pv_uv_sum_9','cart_ipv_sum_9','cart_uv_sum_9','collect_uv_sum_9','num_gmv_sum_9','amt_gmv_sum_9','qty_gmv_sum_9','unum_gmv_sum_9','amt_alipay_sum_9','num_alipay_sum_9','qty_alipay_sum_9','unum_alipay_sum_9','ztc_pv_ipv_sum_9','tbk_pv_ipv_sum_9','ss_pv_ipv_sum_9','jhs_pv_ipv_sum_9','ztc_pv_uv_sum_9','tbk_pv_uv_sum_9','ss_pv_uv_sum_9','jhs_pv_uv_sum_9','num_alipay_njhs_sum_9','amt_alipay_njhs_sum_9','qty_alipay_njhs_sum_9','unum_alipay_njhs_sum_9','pv_ipv_11','pv_uv_11','cart_ipv_11','cart_uv_11','collect_uv_11','num_gmv_11','amt_gmv_11','qty_gmv_11','unum_gmv_11','amt_alipay_11','num_alipay_11','qty_alipay_11','unum_alipay_11','ztc_pv_ipv_11','tbk_pv_ipv_11','ss_pv_ipv_11','jhs_pv_ipv_11','ztc_pv_uv_11','tbk_pv_uv_11','ss_pv_uv_11','jhs_pv_uv_11','num_alipay_njhs_11','amt_alipay_njhs_11','qty_alipay_njhs_11','unum_alipay_njhs_11','pv_ipv_sum_11','pv_uv_sum_11','cart_ipv_sum_11','cart_uv_sum_11','collect_uv_sum_11','num_gmv_sum_11','amt_gmv_sum_11','qty_gmv_sum_11','unum_gmv_sum_11','amt_alipay_sum_11','num_alipay_sum_11','qty_alipay_sum_11','unum_alipay_sum_11','ztc_pv_ipv_sum_11','tbk_pv_ipv_sum_11','ss_pv_ipv_sum_11','jhs_pv_ipv_sum_11','ztc_pv_uv_sum_11','tbk_pv_uv_sum_11','ss_pv_uv_sum_11','jhs_pv_uv_sum_11','num_alipay_njhs_sum_11','amt_alipay_njhs_sum_11','qty_alipay_njhs_sum_11','unum_alipay_njhs_sum_11','pv_ipv_14','pv_uv_14','cart_ipv_14','cart_uv_14','collect_uv_14','num_gmv_14','amt_gmv_14','qty_gmv_14','unum_gmv_14','amt_alipay_14','num_alipay_14','qty_alipay_14','unum_alipay_14','ztc_pv_ipv_14','tbk_pv_ipv_14','ss_pv_ipv_14','jhs_pv_ipv_14','ztc_pv_uv_14','tbk_pv_uv_14','ss_pv_uv_14','jhs_pv_uv_14','num_alipay_njhs_14','amt_alipay_njhs_14','qty_alipay_njhs_14','unum_alipay_njhs_14','pv_ipv_sum_14','pv_uv_sum_14','cart_ipv_sum_14','cart_uv_sum_14','collect_uv_sum_14','num_gmv_sum_14','amt_gmv_sum_14','qty_gmv_sum_14','unum_gmv_sum_14','amt_alipay_sum_14','num_alipay_sum_14','qty_alipay_sum_14','unum_alipay_sum_14','ztc_pv_ipv_sum_14','tbk_pv_ipv_sum_14','ss_pv_ipv_sum_14','jhs_pv_ipv_sum_14','ztc_pv_uv_sum_14','tbk_pv_uv_sum_14','ss_pv_uv_sum_14','jhs_pv_uv_sum_14','num_alipay_njhs_sum_14','amt_alipay_njhs_sum_14','qty_alipay_njhs_sum_14','unum_alipay_njhs_sum_14','max_qty_alipay_njhs','min_qty_alipay_njhs','std_qty_alipay_njhs','cate_id_qty_alipay_njhs_sum','cate_id_qty_alipay_njhs_avg','cate_id_qty_alipay_njhs_std','cate_level_id_qty_alipay_njhs_sum','cate_level_id_qty_alipay_njhs_avg','cate_level_id_qty_alipay_njhs_std','brand_id_qty_alipay_njhs_sum','brand_id_qty_alipay_njhs_avg','brand_id_qty_alipay_njhs_std','supplier_id_qty_alipay_njhs_sum','supplier_id_qty_alipay_njhs_avg','supplier_id_qty_alipay_njhs_std']
test_fencang = pd.read_csv('/Applications/dev/tmp/test_fencang.csv',header=None)
test_fencang.columns = ['watch','store_code','item_id','label','pv_ipv_1','pv_uv_1','cart_ipv_1','cart_uv_1','collect_uv_1','num_gmv_1','amt_gmv_1','qty_gmv_1','unum_gmv_1','amt_alipay_1','num_alipay_1','qty_alipay_1','unum_alipay_1','ztc_pv_ipv_1','tbk_pv_ipv_1','ss_pv_ipv_1','jhs_pv_ipv_1','ztc_pv_uv_1','tbk_pv_uv_1','ss_pv_uv_1','jhs_pv_uv_1','num_alipay_njhs_1','amt_alipay_njhs_1','qty_alipay_njhs_1','unum_alipay_njhs_1','pv_ipv_sum_1','pv_uv_sum_1','cart_ipv_sum_1','cart_uv_sum_1','collect_uv_sum_1','num_gmv_sum_1','amt_gmv_sum_1','qty_gmv_sum_1','unum_gmv_sum_1','amt_alipay_sum_1','num_alipay_sum_1','qty_alipay_sum_1','unum_alipay_sum_1','ztc_pv_ipv_sum_1','tbk_pv_ipv_sum_1','ss_pv_ipv_sum_1','jhs_pv_ipv_sum_1','ztc_pv_uv_sum_1','tbk_pv_uv_sum_1','ss_pv_uv_sum_1','jhs_pv_uv_sum_1','num_alipay_njhs_sum_1','amt_alipay_njhs_sum_1','qty_alipay_njhs_sum_1','unum_alipay_njhs_sum_1','pv_ipv_2','pv_uv_2','cart_ipv_2','cart_uv_2','collect_uv_2','num_gmv_2','amt_gmv_2','qty_gmv_2','unum_gmv_2','amt_alipay_2','num_alipay_2','qty_alipay_2','unum_alipay_2','ztc_pv_ipv_2','tbk_pv_ipv_2','ss_pv_ipv_2','jhs_pv_ipv_2','ztc_pv_uv_2','tbk_pv_uv_2','ss_pv_uv_2','jhs_pv_uv_2','num_alipay_njhs_2','amt_alipay_njhs_2','qty_alipay_njhs_2','unum_alipay_njhs_2','pv_ipv_sum_2','pv_uv_sum_2','cart_ipv_sum_2','cart_uv_sum_2','collect_uv_sum_2','num_gmv_sum_2','amt_gmv_sum_2','qty_gmv_sum_2','unum_gmv_sum_2','amt_alipay_sum_2','num_alipay_sum_2','qty_alipay_sum_2','unum_alipay_sum_2','ztc_pv_ipv_sum_2','tbk_pv_ipv_sum_2','ss_pv_ipv_sum_2','jhs_pv_ipv_sum_2','ztc_pv_uv_sum_2','tbk_pv_uv_sum_2','ss_pv_uv_sum_2','jhs_pv_uv_sum_2','num_alipay_njhs_sum_2','amt_alipay_njhs_sum_2','qty_alipay_njhs_sum_2','unum_alipay_njhs_sum_2','pv_ipv_3','pv_uv_3','cart_ipv_3','cart_uv_3','collect_uv_3','num_gmv_3','amt_gmv_3','qty_gmv_3','unum_gmv_3','amt_alipay_3','num_alipay_3','qty_alipay_3','unum_alipay_3','ztc_pv_ipv_3','tbk_pv_ipv_3','ss_pv_ipv_3','jhs_pv_ipv_3','ztc_pv_uv_3','tbk_pv_uv_3','ss_pv_uv_3','jhs_pv_uv_3','num_alipay_njhs_3','amt_alipay_njhs_3','qty_alipay_njhs_3','unum_alipay_njhs_3','pv_ipv_sum_3','pv_uv_sum_3','cart_ipv_sum_3','cart_uv_sum_3','collect_uv_sum_3','num_gmv_sum_3','amt_gmv_sum_3','qty_gmv_sum_3','unum_gmv_sum_3','amt_alipay_sum_3','num_alipay_sum_3','qty_alipay_sum_3','unum_alipay_sum_3','ztc_pv_ipv_sum_3','tbk_pv_ipv_sum_3','ss_pv_ipv_sum_3','jhs_pv_ipv_sum_3','ztc_pv_uv_sum_3','tbk_pv_uv_sum_3','ss_pv_uv_sum_3','jhs_pv_uv_sum_3','num_alipay_njhs_sum_3','amt_alipay_njhs_sum_3','qty_alipay_njhs_sum_3','unum_alipay_njhs_sum_3','pv_ipv_5','pv_uv_5','cart_ipv_5','cart_uv_5','collect_uv_5','num_gmv_5','amt_gmv_5','qty_gmv_5','unum_gmv_5','amt_alipay_5','num_alipay_5','qty_alipay_5','unum_alipay_5','ztc_pv_ipv_5','tbk_pv_ipv_5','ss_pv_ipv_5','jhs_pv_ipv_5','ztc_pv_uv_5','tbk_pv_uv_5','ss_pv_uv_5','jhs_pv_uv_5','num_alipay_njhs_5','amt_alipay_njhs_5','qty_alipay_njhs_5','unum_alipay_njhs_5','pv_ipv_sum_5','pv_uv_sum_5','cart_ipv_sum_5','cart_uv_sum_5','collect_uv_sum_5','num_gmv_sum_5','amt_gmv_sum_5','qty_gmv_sum_5','unum_gmv_sum_5','amt_alipay_sum_5','num_alipay_sum_5','qty_alipay_sum_5','unum_alipay_sum_5','ztc_pv_ipv_sum_5','tbk_pv_ipv_sum_5','ss_pv_ipv_sum_5','jhs_pv_ipv_sum_5','ztc_pv_uv_sum_5','tbk_pv_uv_sum_5','ss_pv_uv_sum_5','jhs_pv_uv_sum_5','num_alipay_njhs_sum_5','amt_alipay_njhs_sum_5','qty_alipay_njhs_sum_5','unum_alipay_njhs_sum_5','pv_ipv_7','pv_uv_7','cart_ipv_7','cart_uv_7','collect_uv_7','num_gmv_7','amt_gmv_7','qty_gmv_7','unum_gmv_7','amt_alipay_7','num_alipay_7','qty_alipay_7','unum_alipay_7','ztc_pv_ipv_7','tbk_pv_ipv_7','ss_pv_ipv_7','jhs_pv_ipv_7','ztc_pv_uv_7','tbk_pv_uv_7','ss_pv_uv_7','jhs_pv_uv_7','num_alipay_njhs_7','amt_alipay_njhs_7','qty_alipay_njhs_7','unum_alipay_njhs_7','pv_ipv_sum_7','pv_uv_sum_7','cart_ipv_sum_7','cart_uv_sum_7','collect_uv_sum_7','num_gmv_sum_7','amt_gmv_sum_7','qty_gmv_sum_7','unum_gmv_sum_7','amt_alipay_sum_7','num_alipay_sum_7','qty_alipay_sum_7','unum_alipay_sum_7','ztc_pv_ipv_sum_7','tbk_pv_ipv_sum_7','ss_pv_ipv_sum_7','jhs_pv_ipv_sum_7','ztc_pv_uv_sum_7','tbk_pv_uv_sum_7','ss_pv_uv_sum_7','jhs_pv_uv_sum_7','num_alipay_njhs_sum_7','amt_alipay_njhs_sum_7','qty_alipay_njhs_sum_7','unum_alipay_njhs_sum_7','pv_ipv_9','pv_uv_9','cart_ipv_9','cart_uv_9','collect_uv_9','num_gmv_9','amt_gmv_9','qty_gmv_9','unum_gmv_9','amt_alipay_9','num_alipay_9','qty_alipay_9','unum_alipay_9','ztc_pv_ipv_9','tbk_pv_ipv_9','ss_pv_ipv_9','jhs_pv_ipv_9','ztc_pv_uv_9','tbk_pv_uv_9','ss_pv_uv_9','jhs_pv_uv_9','num_alipay_njhs_9','amt_alipay_njhs_9','qty_alipay_njhs_9','unum_alipay_njhs_9','pv_ipv_sum_9','pv_uv_sum_9','cart_ipv_sum_9','cart_uv_sum_9','collect_uv_sum_9','num_gmv_sum_9','amt_gmv_sum_9','qty_gmv_sum_9','unum_gmv_sum_9','amt_alipay_sum_9','num_alipay_sum_9','qty_alipay_sum_9','unum_alipay_sum_9','ztc_pv_ipv_sum_9','tbk_pv_ipv_sum_9','ss_pv_ipv_sum_9','jhs_pv_ipv_sum_9','ztc_pv_uv_sum_9','tbk_pv_uv_sum_9','ss_pv_uv_sum_9','jhs_pv_uv_sum_9','num_alipay_njhs_sum_9','amt_alipay_njhs_sum_9','qty_alipay_njhs_sum_9','unum_alipay_njhs_sum_9','pv_ipv_11','pv_uv_11','cart_ipv_11','cart_uv_11','collect_uv_11','num_gmv_11','amt_gmv_11','qty_gmv_11','unum_gmv_11','amt_alipay_11','num_alipay_11','qty_alipay_11','unum_alipay_11','ztc_pv_ipv_11','tbk_pv_ipv_11','ss_pv_ipv_11','jhs_pv_ipv_11','ztc_pv_uv_11','tbk_pv_uv_11','ss_pv_uv_11','jhs_pv_uv_11','num_alipay_njhs_11','amt_alipay_njhs_11','qty_alipay_njhs_11','unum_alipay_njhs_11','pv_ipv_sum_11','pv_uv_sum_11','cart_ipv_sum_11','cart_uv_sum_11','collect_uv_sum_11','num_gmv_sum_11','amt_gmv_sum_11','qty_gmv_sum_11','unum_gmv_sum_11','amt_alipay_sum_11','num_alipay_sum_11','qty_alipay_sum_11','unum_alipay_sum_11','ztc_pv_ipv_sum_11','tbk_pv_ipv_sum_11','ss_pv_ipv_sum_11','jhs_pv_ipv_sum_11','ztc_pv_uv_sum_11','tbk_pv_uv_sum_11','ss_pv_uv_sum_11','jhs_pv_uv_sum_11','num_alipay_njhs_sum_11','amt_alipay_njhs_sum_11','qty_alipay_njhs_sum_11','unum_alipay_njhs_sum_11','pv_ipv_14','pv_uv_14','cart_ipv_14','cart_uv_14','collect_uv_14','num_gmv_14','amt_gmv_14','qty_gmv_14','unum_gmv_14','amt_alipay_14','num_alipay_14','qty_alipay_14','unum_alipay_14','ztc_pv_ipv_14','tbk_pv_ipv_14','ss_pv_ipv_14','jhs_pv_ipv_14','ztc_pv_uv_14','tbk_pv_uv_14','ss_pv_uv_14','jhs_pv_uv_14','num_alipay_njhs_14','amt_alipay_njhs_14','qty_alipay_njhs_14','unum_alipay_njhs_14','pv_ipv_sum_14','pv_uv_sum_14','cart_ipv_sum_14','cart_uv_sum_14','collect_uv_sum_14','num_gmv_sum_14','amt_gmv_sum_14','qty_gmv_sum_14','unum_gmv_sum_14','amt_alipay_sum_14','num_alipay_sum_14','qty_alipay_sum_14','unum_alipay_sum_14','ztc_pv_ipv_sum_14','tbk_pv_ipv_sum_14','ss_pv_ipv_sum_14','jhs_pv_ipv_sum_14','ztc_pv_uv_sum_14','tbk_pv_uv_sum_14','ss_pv_uv_sum_14','jhs_pv_uv_sum_14','num_alipay_njhs_sum_14','amt_alipay_njhs_sum_14','qty_alipay_njhs_sum_14','unum_alipay_njhs_sum_14','max_qty_alipay_njhs','min_qty_alipay_njhs','std_qty_alipay_njhs','cate_id_qty_alipay_njhs_sum','cate_id_qty_alipay_njhs_avg','cate_id_qty_alipay_njhs_std','cate_level_id_qty_alipay_njhs_sum','cate_level_id_qty_alipay_njhs_avg','cate_level_id_qty_alipay_njhs_std','brand_id_qty_alipay_njhs_sum','brand_id_qty_alipay_njhs_avg','brand_id_qty_alipay_njhs_std','supplier_id_qty_alipay_njhs_sum','supplier_id_qty_alipay_njhs_avg','supplier_id_qty_alipay_njhs_std']
train_all.to_csv('../data/train_all.csv',index=None)
test_all.to_csv('../data/test_all.csv',index=None)
train_fencang.to_csv('../data/train_fencang.csv',index=None)
test_fencang.to_csv('../data/test_fencang.csv',index=None)
