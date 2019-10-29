from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'HOy9AiALAEXwaBBxEJUzFPE9C'
consumer_secret = 'I64GZgbKGiqqFPHVuIid7HllnVFpgrUKPk6AMY82WqbgCLMhlE'

access_token = '831787864534941697-yqr1TIbYRq1iIiNI0MqjUygIDQdhpgo'
access_token_secret = 'iP5v6ZOFJ1WTzaK92ATt09hcJn2u6gVm7TCHplRIOWDXZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended', count=18000)
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})


#---------------------------------------------------------------------------


