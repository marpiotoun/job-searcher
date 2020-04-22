import requests
from flask import Flask, render_template, request
from load_api import LoadApi

app = Flask('Marpi News')
loader = LoadApi()
loader.search_all()
order_by_new_db, order_by_popular_db = loader.load_fake_db()


@app.route('/')
def home():
  try:
    order_by = request.args['order_by']
    if order_by == 'new':
      return render_template("index.html", objs=order_by_new_db)
  except Exception:
      pass
    return render_template("index.html", objs=order_by_popular_db)


@app.route('/<_id>')
def story_view(_id):
    comments = []
    target_obj=None
    for obj in order_by_new_db:
        if obj['objectID'] == _id:
            target_obj = obj
            comments = obj['comments']
    if comments is None:
        for obj in order_by_popular_db:
            if obj['objectID'] == _id:
                target_obj = obj
                comments = obj['comments']
    if target_obj:
      return render_template("detail.html",
                             title=target_obj['title'],
                             points=target_obj['points'],
                             author=target_obj['author'],
                             url=target_obj['url'],
                             objs=comments)
    else:
       return render_template("detail.html", objs=comments)


app.run()
