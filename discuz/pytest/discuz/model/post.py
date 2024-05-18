from dataclasses import dataclass


@dataclass
class Post:
    board_name: str
    subject: str
    message: str
