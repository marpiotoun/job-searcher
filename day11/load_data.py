from bs4 import BeautifulSoup
import requests

subreddit_list = ['r/javascript',
                  'r/reactjs',
                  'r/reactnative',
                  'r/programming',
                  'r/css',
                  'r/golang',
                  'r/flutter',
                  'r/rust',
                  'r/django'
                  ]

URL = 'https://www.reddit.com/r/django'

# 전체 페이지 list 가져오기
class_ = 'rpBJOHq2PR60pnwJlUyP0'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
reddits = BeautifulSoup(requests.get(URL, headers=headers).text, 'html.parser').select(f"div.{class_} > div > div > div")

# for r in reddits:
#     print(r.prettify())
#     print('-'*100)

""" 한 블록 parsing """
block = reddits[0]
# Promote class
promote_class = '_2oEYZXchPfHwcf9mTMGMg8'
if block.find(class_=promote_class) is not None:
    print("이건 광고잖아")
# title class name = _eYtD2XCVieq6emjKBH3m
title_class = '_eYtD2XCVieq6emjKBH3m'
title = (block.find(class_=title_class)).string
print(title)
# title a class name
a_class = 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE'
a_href = URL+(block.find(class_=a_class))['href']
print(a_href)
# upvote class name
upvote_class = '_1rZYMD_4xY3gRcSS3p8ODO'
upvote = (block.find(class_=upvote_class)).string
print(upvote)
