import json

from unittest.model.board import Board


def load_boards_from_json(filename='data/boards.json'):
    with open(filename, 'r') as f:
        boards_data = json.load(f)
        return [Board(**data) for data in boards_data]
