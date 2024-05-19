import json

from discuz.model.post import Post
from discuz.model.recommend import Recommend


def load_post_data(filename='discuz/data/post.json'):
    with open(filename, 'r') as f:
        post_data = json.load(f)
        return [Post(**data) for data in post_data]


def load_recommend_data(filename='discuz/data/recommend.json'):
    with open(filename, 'r') as f:
        recommend_data = json.load(f)
        return [Recommend(**data) for data in recommend_data]
