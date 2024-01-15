import unittest
from scripts.api.fetch_posts import response
class TestAPI(unittest.TestCase):
    def test_status_code(self):
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()
