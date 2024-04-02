import csv


def save_ups_to_csv(ups, file_path):
    headers = ['name', 'up_desc', 'avatar_url']

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(headers)

        for up in ups:
            row = [
                up.name,
                up.up_desc,
                up.avatar_url
            ]
            writer.writerow(row)


class Up:
    def __init__(self):
        self.name = ""
        self.up_desc = ""
        self.avatar_url = ""
