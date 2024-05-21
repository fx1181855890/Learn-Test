from discuz.model.comment import Comment
from discuz.model.post import Post
from discuz.model.recommend import Recommend
from discuz.page.board_page import BoardPage
from discuz.page.main_page import MainPage


def submit_posts(main_page: MainPage, board_page: BoardPage, posts: list[Post]):
    for post in posts:
        main_page.init()
        main_page.enter_board(post.board_name)
        board_page.submit_post(post)


def recommend_posts(main_page: MainPage, board_page: BoardPage, recommends: list[Recommend]):
    for recommend in recommends:
        main_page.init()
        main_page.enter_board(recommend.board_name)
        board_page.recommend_post(recommend)


def comment_posts(main_page: MainPage, board_page: BoardPage, comments: list[Comment]):
    for comment in comments:
        main_page.init()
        main_page.enter_board(comment.board_name)
        board_page.comment_post(comment)
