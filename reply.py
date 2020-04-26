import tweepy
import time

auth = tweepy.OAuthHandler('2DqT3E4Wsd9WM1Wv5JfUx0TXw',
                           'igr9NF3c0wwB7ATkiQSApDPnE3T3HFPZfn600NI7hyp6XdffVn')
auth.set_access_token('1247064631484571651-oyXPaSWa1qT9KTJAsIgZuRnndvPOn6',
                      'SCagOml9JTLI7mhYge6QZo2C8V03FeeP44hu41tGEwQ7h')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'babu merece ganhar'
numero = 30

for tweet in tweepy.Cursor(api.search, search).items(numero):
    try:
        print("nome do usuario: @" + tweet.user.screen_name)
        api.update_status("concordo", in_reply_to_status_id=tweet)
        print("tuite enviado corretamente")
        time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
