import xlrd
from xlutils.copy import copy

# data = xlrd.open_workbook("../test_data/frist.xls")
# print(data)
# table = data.sheets()[0]
# print("行:", table.nrows)
# print("列:", table.ncols)
# print(table.cell_value(0,1))
# print("--------------------这是一次伟大的改革------------------------")


class operationExcel(object):
    def __init__(self, file_path="../test_data/two.xls", sheet_id=0):
        self.file_path = file_path
        self.sheet_id = sheet_id
        self.data = self.get_data

    def get_data(self):
        data = xlrd.open_workbook(self.file_path)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_nrows(self):
        #获取单元排数
        return self.get_data().nrows


    def get_cell_value(self, x=0, y=0):
        #获取某个单元格数据
        return self.get_data().cell_value(x, y)

    def write_reality_result_data(self, x, y, data):
        #写入数据
        read_data = xlrd.open_workbook(self.file_path, formatting_info=True)
        write_data = copy(read_data)
        print(write_data)
        sheet_data = write_data.get_sheet(0)
        print("+++=================++++")
        sheet_data.write(x, y, data)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        write_data.save(self.file_path)

# print(operationExcel().get_cell_value(1,6))

