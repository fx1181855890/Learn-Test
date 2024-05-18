import json

from discuz.model.post import Post


def load_post__data_from_json(filename='discuz/data/post.json'):
    with open(filename, 'r') as f:
        post_data = json.load(f)
        return [Post(**data) for data in post_data]
