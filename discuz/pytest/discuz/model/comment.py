from dataclasses import dataclass


@dataclass
class Comment:
    board_name: str
    subject: str
    message: str
