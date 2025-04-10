from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
load_dotenv()

NEWSAPIKEY = os.getenv("NEWSAPI")
# Init
newsapi = NewsApiClient(api_key=NEWSAPIKEY)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q=input("welches thema interessiert dich"))


print(top_headlines)