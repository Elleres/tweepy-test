import tweepy
from time import sleep
from random import randint


def load_api():
    bearer_token = "bearer token"
    consumer_key = "consumer key"
    consumer_secret = "consumer secret"
    acess_token = "acess token"
    acess_token_secret = "acess token secret"
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(acess_token, acess_token_secret)
    return tweepy.API(auth, wait_on_rate_limit=True)


def last_tweet(user_id, count):
    # THIS FUNCTION FINDS THE LAST TWEET ID FROM THE USER
    for tweets in api.user_timeline(user_id=user_id, count=count):
        ultimo_tweet = tweets.id
    return ultimo_tweet


# LOADING API

api = load_api()
lista_ofensas = ['LIST OF THINGS U WANT TO TWEET']
user1_user = api.get_user(screen_name="@USER_U_WANT_TO_TWEET")
user2_user = api.get_user(screen_name="@USER_U_WANT_TO_TWEET_1")

# EMPTY LIST FOR TWEET THAT HAVE ALREADY BEEN REPLIED TO

tweets_res = []

# GETTING LAST TWEETS FOR BOTH USERS
user1_last_tweet = last_tweet(user1_user, 1)
user2_last_tweet = last_tweet(user2_user, 1)

# LOOP TO KEEP SEARCHING FOR NEW TWEETS
while True:
    sleep(10)
    user1_user_tweets = api.user_timeline(user_id=user1_user.id, count=1)
    user2_user_tweets = api.user_timeline(user_id=user2_user.id, count=1)
    for tweet in user1_user_tweets:
        if tweet.id > user1_last_tweet and tweet.id not in tweets_res and tweet.retweeted == False:
            api.update_status(status=lista_ofensas[randint(0, 7)], in_reply_to_status_id=tweet.id,
                              auto_populate_reply_metadata=True)
            tweets_res.append(tweet.id)
            print(f'Resposta Tweetada para {user1_user.screen_name}, {tweet.text}')
    for tweet in user2_user_tweets:
        if tweet.id > user2_last_tweet and tweet.id not in tweets_res and tweet.retweeted == False:
            api.update_status(status='STATUS THAT YOU WANT TO TWEET',
                              in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
            tweets_res.append(tweet.id)
            print(f'Resposta tweetada para  {user2_user.screen_name}, {tweet.text}')
