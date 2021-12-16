import argparse
from bs4 import BeautifulSoup
import re
import time
import requests

parser = argparse.ArgumentParser(description='Program to scrape the news articles for the links')
parser.add_argument('-l','--links', help='Path to links file', required=True)
parser.add_argument('-r','--results', help='Path to results file', required=True)
args = vars(parser.parse_args())

text_file = open(args['links'], "r")
data = text_file.read()
text_file.close()

with open(args['results'], "w") as f:

    links = data.splitlines()

    for l in links:
        time.sleep(1)
        text = ''
        if l == 'NAN':
            f.write('NAN&|&NAN\n')
        else:
            try:
                response = requests.get(l)
                htmlParse = BeautifulSoup(response.text, 'html.parser')
                for para in htmlParse.find_all("p"):
                    text = text + para.get_text().replace('\n', ' ').replace('\r', ' ').replace('Reuters, the news and media division of Thomson Reuters, is the world’s largest multimedia news provider, reaching billions of people worldwide every day. Reuters provides business, financial, national and international news to professionals via desktop terminals, the world''s media organizations, industry events and directly to consumers.', '')
                for para in htmlParse.find_all("div", {"class": "zn-body__paragraph"}):
                    text = text + para.get_text().replace('\n', ' ').replace('\r', ' ')
                text = re.sub('Our Standards.*', '', text)
                text = re.sub('Reuters, the news and media division.*', '', text)
                f.write( (l + '&|&' + text + '\n') )
            except Exception as e:
                print(e)
                f.write(l + '&|&NAN\n')