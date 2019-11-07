import unittest

class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("这是类方法开始")
    @classmethod
    def tearDownClass(cls):
        print("这是类方法结束")

    def setUp(self):
        print("case开始")

    def tearDown(self):
        print("case结束")

    def test_01(self):
        print("第一个case")

    def test_02(self):
        print("第二个case")


if __name__ == "__main__":
    TestMethod()