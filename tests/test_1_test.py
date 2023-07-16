import unittest
from newsapi import NewsAPI

class TestNewsAPIIntegration(unittest.TestCase):
    def setUp(self):
        self.news_api = NewsAPI()

    def test_store_article_on_server(self):
        json_data = {
            "title": "Example News Article",
            "author": "John Doe",
            "published_date": "2023-07-08",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        result = self.news_api.store_on_server(json_data)
        self.assertTrue(result)

    def test_retrieve_article_from_server(self):
        result = self.news_api.retrieve_from_server()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn("title", result)
        self.assertIn("author", result)
        self.assertIn("published_date", result)
        self.assertIn("content", result)

if __name__ == '__main__':
    unittest.main()