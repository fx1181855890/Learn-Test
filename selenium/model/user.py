import csv


def save_users_to_csv(users, file_path):
    headers = ['name', 'up', 'course_desc', 'pubdate', 'url', 'card_url', 'course_like', 'course_fav', 'course_view', 'tag']

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(headers)

        for user in users:
            row = [
                user.name,
                user.up,
                user.course_desc,
                user.pubdate,
                user.url,
                user.card_url,
                user.course_like,
                user.course_fav,
                user.course_view,
                user.tag
            ]
            writer.writerow(row)


class User:
    def __init__(self):
        self.name = ""
        self.up = ""
        self.course_desc = ""
        self.pubdate = ""
        self.url = ""
        self.card_url = ""
        self.course_like = ""
        self.course_fav = ""
        self.course_view = ""
        self.tag = ""
