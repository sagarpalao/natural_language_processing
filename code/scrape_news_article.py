# Run it from the code directory

text_file = open("../data/sample_links", "r")
data = text_file.read()
text_file.close()

with open("../data/sample_article_body", "w") as f:

    links = data.splitlines()

    from bs4 import BeautifulSoup
    import re
    import time
    import requests

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