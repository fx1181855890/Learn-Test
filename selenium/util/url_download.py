import csv
import os
import requests


def download_image(url, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(folder_path, url.split('/')[-1].split('@')[0])
        with open(file_path, 'wb') as file:
            file.write(response.content)


def download_images_from_csv(csv_file_path, image_column, folder_name):
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            image_url = row[image_column]
            if image_url:
                download_image(image_url, folder_name)


download_images_from_csv('../data/users.csv', 'card_url', '../data/cover_img')
download_images_from_csv('../data/ups.csv', 'avatar_url', '../data/avatar_img')
