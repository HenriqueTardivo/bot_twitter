import tweepy
import time
import requests
from bs4 import BeautifulSoup

auth = tweepy.OAuthHandler('bl221K3N88jjxbUIdkxlKdusw',
                           'aE40iWYcdfMnYJneyhwPO2Z3nOyfTSdLK5UmcJQGm7j5O4cPER')
auth.set_access_token('1247064631484571651-lcSyz3w3wzpf5mryFqeIFVn9KqqPJY',
                      'hXx3rrKwrz53w0BOg1ukICCpyhTI10vxS676rE5FZ2VTB')

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

url = 'https://covid.saude.gov.br/'

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

