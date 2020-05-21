import tweepy
import time

auth = tweepy.OAuthHandler('Dxw05fIkKdSRhLD1aiPTMbAt7',
                           'NpA6jhO7zvSkxcq1kHXlj5Yj67BsO7X3m1QpSTsJXFS2QitoJL')
auth.set_access_token('1247064631484571651-GtsKB6FNYesVuB1C90DQ0ar6TswuLJ',
                      'xAFB40Mj2fpWuwikgPDsnDc1iuMj8EgS3XmjphxTwZrh0')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

search = 'amarelo'
numero = 10000000

for tweet in tweepy.Cursor(api.search, search).items(numero):
    try:
        if((tweet.text)=='amarelo'):
            print("nome do usuario: @" + tweet.user.screen_name)
            api.update_status("@" + tweet.user.screen_name + " concordo", in_reply_to_status_id=tweet.id)
            print("tuite enviado corretamente")
            time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break