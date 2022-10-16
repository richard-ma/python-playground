import unittest
from functions import *


class FunctionTest(unittest.TestCase):
    # 开始测试时调用
    def setUp(self) -> None:
        return super().setUp()

    # 所有测试结束时调用
    def tearDown(self) -> None:
        return super().tearDown()

    # 开始测试

    # 测试返回值是否和输入值相等
    def test_returnInt(self):
        val = 100
        # assertEqual
        self.assertEqual(returnInt(val), val)

    # 测试布尔值
    def test_returnBool(self):
        # assertTrue / assertFalse
        self.assertTrue(returnBool(True))
        self.assertFalse(returnBool(False))
        # assertEqual
        self.assertEqual(returnBool(True), True)
        self.assertEqual(returnBool(False), False)


if __name__ == "__main__":
    unittest.main()
