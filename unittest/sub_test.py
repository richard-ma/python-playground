import unittest


class MyTest(unittest.TestCase):
    def test_subtest(self):
        for i in range(6):
            with self.subTest(i=i): # 使用subTest，让循环继续运行，不符合要求的参数会被显示，而不是直接终止
                self.assertEqual(i % 2, 0)


if __name__ == "__main__":
    unittest.main()