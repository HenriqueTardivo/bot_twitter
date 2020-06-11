import tweepy
import time

auth = tweepy.OAuthHandler('jkYgDdpDlsE7n2uI0XjZRBVTO',
                           'o93hUv2RzIzjuKXo3UCvDa3HS2onFtjIh6OvJhhej5oTU2TQ3S')
auth.set_access_token('1247064631484571651-3fjWllhNWDhm8KwLkRAAEAh9Ym9tBr',
                      'CqFGRHBaEiFbt4dyJn7u1mRsRwYPOt91152iP5IFpPVkN')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        api.update_status("@" + status.user.screen_name + "mentira!", in_reply_to_status_id=status.id)
        

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow='128372940')