from discuz.model.comment import Comment
from discuz.model.post import Post
from discuz.model.recommend import Recommend
from discuz.page.board_page import BoardPage
from discuz.page.main_page import MainPage


def submit_post(main_page: MainPage, board_page: BoardPage, post: Post):
    main_page.init()
    main_page.enter_board(post.board_name)
    board_page.submit_post(post)


def recommend_post(main_page: MainPage, board_page: BoardPage, recommend: Recommend):
    main_page.init()
    main_page.enter_board(recommend.board_name)
    board_page.recommend_post(recommend)


def comment_post(main_page: MainPage, board_page: BoardPage, comment: Comment):
    main_page.init()
    main_page.enter_board(comment.board_name)
    board_page.comment_post(comment)


def is_commented(main_page: MainPage, board_page: BoardPage, comment: Comment) -> bool:
    main_page.init()
    main_page.enter_board(comment.board_name)
    return board_page.is_commented(comment)
