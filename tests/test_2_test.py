import unittest
import newsapi
from newsapi import NewsAPI

class TestNewsAPI(unittest.TestCase):
    def setUp(self):
        self.news_api = NewsAPI()

    def test_recognize_article_structure(self):
        url = "https://www.example.com/news/article"
        result = self.news_api.recognize_structure(url)
        self.assertTrue(result)

    def test_convert_to_json(self):
        article = {
            "title": "Example News Article",
            "author": "John Doe",
            "published_date": "2023-07-08",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        json_data = self.news_api.convert_to_json(article)
        self.assertIsInstance(json_data, dict)
        self.assertIn("title", json_data)
        self.assertIn("author", json_data)
        self.assertIn("published_date", json_data)
        self.assertIn("content", json_data)

if __name__ == '__main__':
    unittest.main()