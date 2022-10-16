import unittest
from unittest import mock
import mock_client


class TestClient(unittest.TestCase):
    def test_success_request(self):
        success_send = mock.Mock(return_value=200)
        mock_client.send_request = success_send
        self.assertEqual(mock_client.visit_ustack(), 200)

    def test_fail_request(self):
        fail_send = mock.Mock(return_value=404)
        mock_client.send_request = fail_send
        self.assertEqual(mock_client.visit_ustack(), 404)

    def test_call_send_request(self):
        success_send = mock.Mock(return_value=200)
        mock_client.send_request = success_send
        self.assertEqual(mock_client.visit_ustack(), 200)
        self.assertEqual(mock_client.send_request.called, True) # 检查send_request函数是否被调用

    def test_patch(self):
        success_send = mock.Mock(return_value=200)
        with mock.patch('mock_client.send_request', success_send): # 使用patch函数进行对象的替换
            self.assertEqual(mock_client.visit_ustack(), 200)

    # https://docs.python.org/zh-cn/3/library/unittest.mock-examples.html
    # 更多mock的使用方法


if __name__ == "__main__":
    unittest.main()
