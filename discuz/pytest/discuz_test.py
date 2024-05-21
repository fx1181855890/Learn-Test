import pytest
import json

from discuz import process
from discuz.model.comment import Comment
from discuz.model.post import Post
from discuz.model.recommend import Recommend


def load_test_data():
    with open('data/test_data.json', 'r') as file:
        return json.load(file)


@pytest.mark.parametrize("post", load_test_data()["posts"])
def test_post(main_page, board_page, post):
    main_page.sign_in("admin", "admin")
    assert main_page.is_signed_in()

    post_object = Post(post["board_name"], post["subject"], post["message"])

    process.submit_post(main_page, board_page, post_object)

    main_page.sign_out()


@pytest.mark.parametrize("comment", load_test_data()["comments"])
def test_comment(main_page, board_page, comment):
    main_page.sign_in("test", "123456")
    assert main_page.is_signed_in()

    comment_object = Comment(comment["board_name"], comment["subject"], comment["message"])

    process.comment_post(main_page, board_page, comment_object)

    main_page.sign_out()


@pytest.mark.parametrize("recommend", load_test_data()["recommends"])
def test_recommend(main_page, board_page, recommend):
    main_page.sign_in("test", "123456")
    assert main_page.is_signed_in()

    recommend_object = Recommend(recommend["board_name"], recommend["subject"])

    process.recommend_post(main_page, board_page, recommend_object)

    main_page.sign_out()
