from bs4 import BeautifulSoup
import lxml
import requests
import json
import newspaper
Title = " "
Top_Image = " "
source_url = " "
def extract_main_article_info(url):
    
    def extract_main_article(url):
        # Create a newspaper Article object
        article = newspaper.Article(url)

        # Download and parse the article
        article.download()
        article.parse()

        # Extract the main article text
        global Title
        global Top_Image
        global source_url

        main_article = article.text
        Title = article.title
        Top_Image = article.top_image
        source_url = article.source_url

        print(article.top_image)
        print(article.title)
        print(article.source_url)
        # Return the main article
        return { "main_article" : article.text,
        "Title" : article.title,
        "Top_Image" : article.top_image,
        "source_url" : article.source_url}
    v=  extract_main_article(url)
    return v


def retrieve_text_content_from_url(url):
    # Send a GET request to the URL and retrieve the HTML content
    response = requests.get(url)
    html_content = response.text

    # Create a BeautifulSoup object
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the text content
    text_content = soup.get_text()

    text_content_with_newlines = soup.get_text('\n')
    text_content_with_newlines_splited = text_content_with_newlines.split('\n')
    return text_content_with_newlines_splited
    #print(text_content_with_newlines_splited)


def get_website(URL):
   
   # html_text = requests.get(URL)
   # print(html_text)
    html_text = requests.get(URL).text 
    #print(html_text)
    soup = BeautifulSoup(html_text,'lxml')
    header = soup.find('header')
    soup = soup.find('body')
    #return soup
    return {"header":header,"body":soup}
