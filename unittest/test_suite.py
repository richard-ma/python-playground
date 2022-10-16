import unittest
import test_functions

# 可以使用TestSuite组织TestCase
# TestSuite可以实现测试策略的变更
def suite():
    suite = unittest.TestSuite()
    # 添加TestCase
    suite.addTest(test_functions.FunctionTest('test_returnInt'))
    suite.addTest(test_functions.FunctionTest('test_returnBool'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
