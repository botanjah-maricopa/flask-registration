# Test 1
# The app imports and refister responds 

import unittest

from app import app

class TestServer(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_register_route_responds(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)
        
    def test_unknown_route_returns_404(self):
        response = self.client.get("/does-not-exist")
        self.assertEqual(response.status_code, 404)
        
if __name__ == "__main__":
    unittest.main()
        