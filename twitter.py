import tweepy
import time

auth = tweepy.OAuthHandler('bl221K3N88jjxbUIdkxlKdusw','aE40iWYcdfMnYJneyhwPO2Z3nOyfTSdLK5UmcJQGm7j5O4cPER')
auth.set_access_token('1247064631484571651-lcSyz3w3wzpf5mryFqeIFVn9KqqPJY', 'hXx3rrKwrz53w0BOg1ukICCpyhTI10vxS676rE5FZ2VTB')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'votei bolsonaro arrependi'
numeroDeTweets = 100

for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        print('tweet retuitado e favoritado')
        tweet.retweet()
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


