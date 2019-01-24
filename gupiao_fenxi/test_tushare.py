import tushare as  ts

re = ts.fund_holdings(2018, 3)
# print(type(re))
# re.to_excal('./tushare_out/fund_holdings.xlsx')
# print(re)  


df = ts.get_hist_data('000875')
#直接保存
print(type(df))
df.to_excel('./000875.xlsx')

#设定数据位置（从第3行，第6列开始插入数据）
# df.to_excel('c:/day/000875.xlsx', startrow=2,startcol=5)