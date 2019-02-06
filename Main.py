import tweepy
import datetime
from janome.tokenizer import Tokenizer
from requests_oauthlib import OAuth1Session

#認証情報の設定
CK = os.environ["CONSUMER_KEY"]
CS = os.environ["CONSUMER_SECRET"]
AT = os.environ["ACCESS_TOKEN_KEY"]
AS = os.environ["ACCESS_TOKEN_SECRET"]

#認証
twitter = OAuth1Session(client_key, client_secret, resource_owner_key, resource_owner_secret)

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

#削除後の報告
def report(liked,RTed):
  #進める
  print("先程こちらが削除したあなたのツイートは削除までに%d件のいいねと%d件のリツイートを獲得していました!"% )

#該当ツイートを削除する
def del(tweetID):
  api = 'https://api.twitter.com/1.1/statuses/destroy/' + tweet_ID + '.json'
  req = twitter.post(api)
  #for debug
  if req.status_code == 200:
    print("Success Delete!")
  else:
    print("Error! ErrorCode: %d" % req.status_code)
  

#5分ごとに実行
@sched.scheduled_job('cron', minute = '0, 5, 10, 15,20,25,30,35,40,45,50,55', hour = '*/1')
def check():
  #for debug
  print("Start checking...")
  myinfo = api.me()
  #対象の最新100件のツイートを取得
  tweets = tweepy.Cursor(api.user_timeline, id = myinfo.id).items(100)
  for tweet in tweets:
    sentence = tweet.text#これはツイート本文
    t = Tokenizer()
    watasiha=False
    jukujo=False
    rorikon=False
    #形態素解析した単語を入れていく
    sec=[]
    words=0
    for token in t.tokenize(sentance):
      sec.append((str)token)
      words=words+1
    for i in words:
      if sec[i]=="私は":
        watashiha=True
      if sec[i]=="熟女":
        jukujo=True
      #このワードは解析でどのように分けられるのか未調査
      if sec[i]=="":
        rorikon=True
      
      #条件を満たしていれば削除行程へ
      if watashiha and (jukujo or rorikon):
        del(tweet.id)
     #for debug
     print("Done!")
