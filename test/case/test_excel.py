import xlrd

from utils.config import DATA_PATH

fname = DATA_PATH + '/yueyueying.xlsx'
# fname = "reflect.xls"
bk = xlrd.open_workbook (fname)
shxrange = range (bk.nsheets)
try:
    sh = bk.sheet_by_name ("Sheet1")
except:
    print
    "no sheet in %s named Sheet1" % fname
        # # 获取行数
        # nrows = sh.nrows
        # # 获取列数
        # ncols = sh.ncols
        # print("nrows %d, ncols %d" % (nrows, ncols))

# 获取第一行第一列数据
cell_value = sh.cell_value (1, 0)
print (cell_value)

        # row_list = []
        # # 获取各行数据
        # for i in range (1, nrows):
        #     row_data = sh.row_values (i)
        #     row_list.append (row_data)
