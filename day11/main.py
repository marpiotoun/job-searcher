import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

db = []
BASE_URL = 'https://www.reddit.com'

def get_data(select):
    URL = f'{BASE_URL}/r/{select}'
    class_ = 'rpBJOHq2PR60pnwJlUyP0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    reddits = BeautifulSoup(requests.get(URL, headers=headers).text, 'html.parser').select(f"div.{class_} > div > div > div")
    data_list = []
    for reddit in reddits:
        promote_class = '_2oEYZXchPfHwcf9mTMGMg8'
        if reddit.find(class_=promote_class) is not None:
            continue

        title_class = '_eYtD2XCVieq6emjKBH3m'
        title = (reddit.find(class_=title_class)).string

        a_class = 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE'
        a_href = URL + (reddit.find(class_=a_class))['href']

        upvote_class = '_1rZYMD_4xY3gRcSS3p8ODO'
        upvote = (reddit.find(class_=upvote_class)).string

        data_list.append((title, a_href, upvote))
    return data_list

app = Flask("DayEleven")

@app.route('/')
def home():
    pass

@app.route('/result')
def result():
     = request

app.run()