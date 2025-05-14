import unittest
from unittest.mock import patch
import requests
from apiplatzi import get_products

class TestApiPlatzi(unittest.TestCase):
    @patch('apiplatzi.requests.get')
    def test_products_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"title": "Majestic...", "price": 25}]

        result = get_products("Majestic")
        self.assertEqual(result, "Found: Majestic... - Price: $25")


    @patch('apiplatzi.requests.get')
    def test_products_failure_with_side_effect(self, mock_get):
        mock_get.side_effect = requests.ConnectionError("Simulated ConnectionError")


        with self.assertRaises(requests.ConnectionError):
            get_products("Majestic")

        
if __name__ == "__main__":
    unittest.main()