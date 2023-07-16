from newspaper import Article
def fun(url):
    # Provide the URL of the article you want to analyze
    """ url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/' """

    # Create an Article object and download the article's HTML
    article = Article(url)
    article.download()

    # Parse the HTML to extract relevant information
    article.parse()

    # Extract the title of the article
    title = article.title

    # Extract the authors of the article
    authors = article.authors

    # Extract the publishing date of the article
    publish_date = article.publish_date

    # Extract the main text content of the article
    text = article.text

    # Extract the URL of the main image associated with the article
    top_image = article.top_image

    # Extract any embedded movies or videos in the article
    movies = article.movies

    # Extract the source URL of the article
    source_url = article.source_url

    # Extract the canonical URL of the article
    canonical_url = article.canonical_link

    # Extract the HTML content of the article
    html = article.html


    # Print the extracted attributes
    return {"Title:": title,
    "Publish Date:": publish_date,
    "Text:": text,
    "Top Image:": top_image,
    "Movies:": movies,
    "Source URL:": source_url
    ,"Canonical URL:": canonical_url}
    


""" import newspaper
from newspaper import Article
from newspaper import fulltext
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import re
from googletrans import Translator
from langdetect import detect
import transformers
import tensorflow as tf

def delete_strings_before(lst, s):
    index = -1
    for i, string in enumerate(lst):
        if string == s:
            index = i
            break
    if index != -1:
        del lst[:index]
    return lst

def generate_summary_from_text(TEXT):    
   
 # Load the summarization pipeline with the desired model
    summarizer = pipeline("summarization", model="t5-base")

    # Split the input text into smaller parts
    max_length = 1024  # Maximum sequence length for the model
    chunks = [TEXT[i:i+max_length] for i in range(0, len(TEXT), max_length)]

    # Summarize each chunk and store the summaries
    summaries = []
    for chunk in chunks:
        summary = summarizer(translate_for_summary(chunk, 'en'), max_length=60, min_length=20, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    # Join the summaries to get the final result
    SUMMARY = " ".join(summaries)
    return SUMMARY

def Classifier(sequence, candidate_labels):
    # Load the zero-shot classification pipeline with the desired model
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", revision="c626438")

    # Perform zero-shot classification
    result = classifier(sequence, candidate_labels)

    # Print the input sequence
    print("Input Sequence:", sequence)
    print()

    # Print the candidate labels
    print("Candidate Labels:", candidate_labels)
    print()

    # Print the predictions
    print("Predicted Label:", result['labels'][0])
    print("Predicted Score:", result['scores'][0])
    print()
    return result

def remove_unnecessary_spaces(TEXT_0):
    TEXT_0 = [x.strip() for x in TEXT_0]
    TEXT_0 = [x for x in TEXT_0 if x != '' and x != ' ']
    return TEXT_0

def fun3(TEXT_0):
    TEXT = " ".join(TEXT_0)
    return TEXT

def extract_editing_and_publishing_dates(TEXT_0):
    date_labels = ["date", "not date"]
    labels = ["edit", "publish"]
    E_Date = ''
    P_Date = ''
    for i in range(1, 7):
        y = Classifier(TEXT_0[i], date_labels)
        if y['scores'][0] > 0.9:
            d = TEXT_0[i-1] + TEXT_0[i]
            z = Classifier(d, labels)
            if z['scores'][1] > 0.7:
                E_Date = "The date of editing: " + TEXT_0[i]
            else:
                P_Date = "The date of publishing: " + TEXT_0[i]
    return {"E_Date": E_Date, "P_Date": P_Date}
def get_author(TEXT_0):
    author = ''
    author_labels = ["human author", "not author"]
    for i in range(1, 20):
        y1 = Classifier(TEXT_0[i], author_labels)
        if y1['scores'][0] > 0.9:
            author = TEXT_0[i]
            break
    return author

def translate_for_summary(text, lang):
    translator = Translator()
    sentences = re.split(r'(?<=[.!?])\s+', text)  # Split text into sentences using punctuation marks as delimiters
    translated_sentences = []
    for sentence in sentences:
        translation = translator.translate(sentence, dest=lang)
        translated_sentences.append(translation.text)
    translated_text = ' '.join(translated_sentences)
    return translated_text

def identify_original_language(text):
    original_language = detect(text)
    return original_language

# Set TensorFlow CPU optimization flags
tf.config.threading.set_intra_op_parallelism_threads(2)
tf.config.threading.set_inter_op_parallelism_threads(2) """