import unittest
import json
# from HtmlTestRunner import HTMLTestRunner
from base2.HTMLTestRunner import  HTMLTestRunner
from base.demo import RunMain


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
    def test_01(self):
        header = {'Content-Type': 'application/json',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                  'Authorization': 'access_key=&^Rwqq%QSSx!HTnFm9XB@pFzL&8im$;app_id=2LaqRXRQvNrVN0Nl'
                  }

        url = 'http://172.16.101.35:16000/user'
        data = {
            "id_card_name": "张全－",
            "id_card_image1": "https://images.coralglobal.cn/20171009/3628696048878239322.JPG",
            "id_card_image2": "https://images.coralglobal.cn/auth_images/20190410/3628705426294555.JPG",
            "merchant": "哇",
            "mobile":"16188880002",
            "bank_account": "612888528144912",
            "id_card_no":"622222194021144911",
            "email":"16188880002@163.com",
            "bank_branch": "中国银行杭州分行",
            "company_en_name": "coralglobal",
            "id_card_image3": "https://images.coralglobal.cn/auth_images/20190410/3628705426294555.JPG",
            "type": "1"
        }

        res1 = self.run.run_main(url, "POST", json.dumps(data), header)
        self.assertEqual(eval(res1["code"]), 1105, "测试成功")
        print(res1.json())

    def test_02(self):
        url = 'http://api.ishugui.com/asg/portal/call/265.do'
        data = {

        }
        res2 = self.run.run_main(url, 'POST', data)
        print("test02")
        print(res2)


    def test_03(self):
        print("我是第三个案例")




if __name__=="__main__":
    fp  = open('../report/html_report.html', 'wb')
    suit = unittest.TestSuite()
    suit.addTest(TestMethod("test_01"))
    # suit.addTest(TestMethod("test_03"))
    print("==============")
    runner = HTMLTestRunner(stream=fp, title="this is second report")
    runner.run(suit)
