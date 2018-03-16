import random
import pandas as pd
from goose3 import Goose
import newspaper
import requests
input_file = '../data/author-data.csv'
output_file = '../data/author-output.csv'

'''
class GooseAuthorExtractor(BaseAuthorExtractor):
    pass
class NewspaperAuthorExtractor(BaseAuthorExtractor):
    pass

class BaseAuthorExtractor:

    article = None
    article_url = None
    inferred_authors = []
    ground_truth = []

    # Initilize object with a given article
    def __init__(article_url, ground_truth=None):
        pass

    # Extracts and returns article object
    def fetch_and_download_article():
        article = ""
        return article

    # Extracts and returns inferred_authors
    def extract_author():
        return self.inferred_authors

    # Returns True/False based comparision between inferred_authors and ground_truth
    def compare_results():
        return False
'''
#output_csv_filename = 'data-from-author-fetch.csv'
#input_csv_filename = 'samples-for-author-fetch.csv'
#manual_output_csv_filename = 'manual-data-from-author-fetch.csv'
#manual_input_csv_filename = 'manual-articles-for-author-fetch.csv'

def infer_authors(input_file, output_file, direct_url=False):
    output = pd.DataFrame()
    rows = []
    values = []
    csv = pd.read_csv(input_file)
    print(csv)
    for index, row in csv.iterrows():
        print("Starting with new story")
        print("--- Newspaper ---")
        authors = []
        columns = list(row.values)
        try:
            article = newspaper.Article(row.URL)
            article.download()
            article.parse()
            story_url = article.url
            print(story_url)
            print(article.authors)
            columns.append(story_url)
            columns.append(article.authors)
        except Exception as e:
            print(e)
            columns.append('Newspaper exception')
        print("--- Goose ---")
        g = Goose()
        try:
            g_article = g.extract(url=article.url)
            print(g_article.title)
            print(g_article.authors)
        except RuntimeError as re:
            print(re)
            columns.append('Goose ERROR')
        except requests.exceptions.ConnectionError as ce:
            print(ce)
            columns.append('Goose Timeout')
        else:   
            columns.append(g_article.authors) 
        authors.append(columns)
        output = output.append(authors)
        output.to_csv(output_file, sep='\t', encoding='utf-8')
    output.to_csv(output_file, sep='\t', encoding='utf-8')

infer_authors(input_file, output_file)
'''
def lookup_articles_from(input_file, output_file, direct_url=False):
    output_df = pd.DataFrame()
    rows = []

    # ITERATE THROUGH CURATED DATA
    data = pd.read_csv(input_file)
    for index, row in data.iterrows():

        rows = []
        new_list = list(row.values)

        if direct_url==False:
            site_url = row.url
            print site_url
        
            # GET ARTICLES
            site = npp.build(site_url)

        if direct_url==True or len(site.articles) > 0:
            
            if direct_url==False:
                # NEWSPAPER
                article = random.choice(site.articles)
                article.download()
                article.parse()
                story_url = article.url
            else:
                article = npp.Article(row.url)
                article.download()
                article.parse()
                story_url = article.url


            print story_url
            new_list.append(story_url)
            print article.authors
            new_list.append(article.authors)
            print '--\n'

            # GOOSE
            try:
                g_article = g.extract(url=article.url)
            except RuntimeError, re:
                print repr(re)
                new_list.append('Goose ERROR')
            else:   
                # print g_article.authors
                new_list.append(g_article.authors)
            
            print '--\n'

            rows.append(new_list)
            output_df = output_df.append(rows)
            
            # CAPTURE INCREMENTAL RESULTS IN CASE OF FAILURE
            output_df.to_csv(output_file, sep='\t', encoding='utf-8')
        else:
            new_list.append('NO ARTICLES PARSED FROM SITE')
            rows.append(new_list)
            output_df = output_df.append(rows)

            # CAPTURE INCREMENTAL RESULTS IN CASE OF FAILURE
            output_df.to_csv(output_file, sep='\t', encoding='utf-8')

    # WRITE FINAL RESULTS
    output_df.to_csv(output_file, sep='\t', encoding='utf-8')

lookup_articles_from(input_csv_filename, output_csv_filename)
lookup_articles_from(manual_input_csv_filename, manual_output_csv_filename, direct_url=True)
'''