import tweepy
import time

auth = tweepy.OAuthHandler('Ef3mbrQa2j83BFexT4xR1D5F5',
                           'rpjHvCtG4w9CFUmsaJOCOoGw4gqX4e7m504XhrfOJLldUvIegJ')
auth.set_access_token('1247064631484571651-ZkVHbqrC5JcBjnKXJcRArJkGRGPGwm',
                      'L0H3bW0RBjIBrMVwa4yHHRZEg0lvQfUWxwgwqCWezD2Ah')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'amarelo'
numero = 1000

for tweet in tweepy.Cursor(api.search, search).items(numero):
    try:
        print(tweet.text.encode("utf-8"))
        if((tweet.text.encode("utf-8"))=='amarelo'):
            print("nome do usuario: @" + tweet.user.screen_name)
            api.update_status("@" + tweet.user.screen_name + " concordo", in_reply_to_status_id=tweet.id)
            print("tuite enviado corretamente")
            time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break