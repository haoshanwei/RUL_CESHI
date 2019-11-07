# -*- coding: utf-8 -*-
from base.demo import RunMain
from data.data_get import getData
import json
from utils.common_util import CommonUtil


class RunTest(object):
    def __init__(self):
        self.runmain = RunMain()
        self.data = getData()
        self.com_util = CommonUtil()

    def run(self):
            res = None
            row_counts = self.data.get_case_lines()  # 获取excel表格行数
            # print(row_counts) 5
            print(row_counts)
            for row_count in range(1, row_counts):
                 print("==============================================================================")
                 print(row_count)
                 url = self.data.get_request_url(row_count)  # y行不变遍历获取x列的请求地址
                 method = self.data.get_request_method(row_count)  # y行不变遍历获取x列的请求方式
                 is_run = self.data.get_is_run(row_count)  # y行不变遍历获取x列的是否运行
                 data = self.data.get_request_data(row_count)  # y行不变遍历获取x列的请求数据，这里面时三次调用，依次分别是get_data_for_json丶get_key_words丶get_request_data
                # header = self.data.get_is_header
                 print(eval(data))
                 data = json.dumps(eval(data))
                 header = {'Content-Type':'application/json',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                          'Authorization':'access_key=&^Rwqq%QSSx!HTnFm9XB@pFzL&8im$;app_id=2LaqRXRQvNrVN0Nl'
                          }
                 expect = int(self.data.get_expect_data(row_count))
                 print('url:', url)
                 print('method:', method)
                 print('is_run:', is_run)
                 print('data:', data)
                 print("expect", expect)
                 print(type(data))
                 # print('header:', header)

                 if is_run:
                     res = self.runmain.run_main(url, method, data, header)
                     if self.com_util.is_contains(expect, res):
                         print("测试通过")
                         self.data.write_reality_data(row_count, "pass")
                     else:
                         print("测试失败")
                         self.data.write_reality_data(row_count, "fail")
                     print("*" * 60 + "分割线" + "*" * 60)
            return res


if __name__ == '__main__':
    print('res:', RunTest().run())
    # RunTest().run


print("zhongguo")
print("我来了中国，欢迎你")
