import unittest
from selenium import webdriver

from discuz.page.board_page import BoardPage
from discuz.page.user_page import UserPage
from discuz.util import load_boards_from_json


class DiscuzTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize WebDriver
        cls.driver = webdriver.Chrome()
        cls.user_page = UserPage(cls.driver)
        cls.board_page = BoardPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        # Sign in before each test
        self.user_page.sign_in(username="admin", password="admin")
        self.assertTrue(self.user_page.is_signed_in(), "User should be signed in")

    def test_add_boards(self):
        # Initialize board page
        self.board_page.init_board()

        # Load boards from JSON
        loaded_boards = load_boards_from_json()

        # Add boards using the board page
        self.board_page.add_boards(loaded_boards)
        self.assertTrue(self.board_page.is_boards_added(loaded_boards), "Boards should be added")

        # Clear added boards
        self.board_page.clean_up()


if __name__ == "__main__":
    unittest.main()
