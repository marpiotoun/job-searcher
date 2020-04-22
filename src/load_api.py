import json
import requests
import copy


class LoadApi:
    def __init__(self):
        self.URL_date = "http://hn.algolia.com/api/v1/search?"
        self.URL_points = "http://hn.algolia.com/api/v1/search_by_date?"
        self.order_by_date = None
        self.order_by_points = None

    def load_json(self, url):
        return json.loads(requests.get(url).text)

    def search_by_date(self):
        self.order_by_date = self.load_json(self.URL_date)['hits']

    def search_by_points(self):
        self.order_by_points = self.load_json(self.URL_points)['hits']

    def search_all(self):
        self.search_by_date()
        self.search_by_points()

    @staticmethod
    def load_comments(_id):
        url = f"http://hn.algolia.com/api/v1/search?tags=comment,story_{_id}"
        response = json.loads(requests.get(url).text, encoding='utf-8')['hits']
        comments = []
        for d in response:
            comment = {}
            for k in d:
                if k in ('author', 'comment_text'):
                    comment.update({k: d[k]})
            comments.append(comment)
        return comments

    def load_fake_db(self):
        cleaned_order_by_date = []
        cleaned_order_by_points = []
        for _dict in self.order_by_date:
            _dict_copy = _dict.copy()
            cleaned_order_by_date.append(clean(_dict_copy))
        for _dict in self.order_by_points:
            _dict_copy = _dict.copy()
            cleaned_order_by_points.append(clean(_dict_copy))
        return cleaned_order_by_date, cleaned_order_by_points


def clean(_dict):
    keys = list(_dict.keys())[:]
    for key in keys:
        if key not in ['title', 'url', 'author', 'points', 'num_comments', 'objectID']:
            del _dict[key]
    _dict.update({'comments': LoadApi.load_comments(_dict['objectID'])})
    print
    return _dict


if __name__ == '__main__':
    a = LoadApi()
    b, c = a.load_fake_db()
    print(b)