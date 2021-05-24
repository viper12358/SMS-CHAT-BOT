import praw
import random

reddit = praw.Reddit(client_id = "" # get your own,
                        client_secret = "" # get your own,
                        user_agent = "<Firefox/Chrome><TwilloAPI>:<University of Calgary Hackathon 2020> (by /u/viper_12358")

# keyword: quote.lowercase(), motivational,
def getQuote():

    quoteList = {}
    for submission in reddit.subreddit('im14andthisisdeep').hot(limit=10):
        if ".jpg" in submission.url:
            quoteList.update({submission.title:submission.url})

    title, url = random.choice(list(quoteList.items()))
    return title, url

# keyword: memes, meme, funny
def getMeme():

    memeList = {}
    for submission in reddit.subreddit("memes").hot(limit=10):
        if ".jpg" in submission.url:
            memeList.update({submission.title:submission.url})
    for submission in reddit.subreddit("bonehurtingjuice").hot(limit=10):
        if ".jpg" in submission.url:
            memeList.update({submission.title:submission.url})
    title, url = random.choice(list(memeList.items()))
    return title, url


# keyword: fact, interesting, learn
def getFact():
    factList = []
    for submission in reddit.subreddit("todayilearned").hot(limit=10):
        fact = submission.title
        fact = fact.replace("TIL","")
        fact.title()
        factList.append(fact)
    q = random.randrange(len(factList))
    title = factList[q]
    return title

# keyword: fact, interesting, learn
def getJoke():

    memeList = {}
    for submission in reddit.subreddit("jokes").hot(limit=10):
        if "discord" not in submission.title and len(submission.selftext) <= 280:
            memeList.update({submission.title:submission.selftext})
    title, body = random.choice(list(memeList.items()))
    return title, body

# keywords: poland, ball, comic

def getComic():

    comicList = {}
    for submission in reddit.subreddit("polandball").hot(limit=15):
        comicList.update({submission.title:submission.url})

    title, url = random.choice(list(comicList.items()))
    return title, url


# print(getMeme())
# print(meme[0])
# print(meme[1])
# print(getComic())
# print(getQuote())
# print(getJoke())
# print(getFact())
# c = getQuote()
# print(c)
# print(c[0])
# print(getFact())
