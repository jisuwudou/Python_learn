# import tushare as ts
# d = ts.get_tick_data('601318',date='2018-06-26')
#
# # c = "输出。。%s" % d
# # c= 'ccc'
#
# str = '输出'
# str.format(d)
#
# e = ts.get_hist_data('601318',start='2017-08-23',end='2017-09-26')
# print(e)
# ---------------------
# 作者：xieyan0811
# 来源：CSDN
# 原文：https://blog.csdn.net/xieyan0811/article/details/73799775
# 版权声明：本文为博主原创文章，转载请附上博文链接！

# import tushare as ts
# cons = ts.get_apis()
# df_day =ts.bar("601318",conn=cons,asset='X',freq='D')
# df_1min =ts.bar("601318",conn=cons,asset='X',freq='1min')
# print(df_1min)
# ---------------------
# 作者：songroom
# 来源：CSDN
# 原文：https://blog.csdn.net/wowotuo/article/details/78857770
# 版权声明：本文为博主原创文章，转载请附上博文链接！