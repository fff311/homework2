import json
from csv import DictReader


with open('books.csv','r') as file_csv:
    book = list(DictReader(file_csv))

with open('reference.json', 'r') as file_json:
    reference = json.load(file_json)
    if isinstance(reference, list):
        combined_data = {}
        for item in reference:
            combined_data.update(item)
        reference = combined_data
    user_reference = {key: reference[key] for key in reference if key != "books"}
    book_reference = reference.get("books")[0]

with open('user.json', 'r') as file_json:
    user = json.load(file_json)

def distribute_books(book, user):
    num_book = len(book)
    num_user = len(user)
    base_book = num_book // num_user
    remainder = num_book % num_user
    distribution = []
    start = 0
    for i in range(num_user):
        end = start + base_book + (1 if i < remainder else 0)
        distribution.append(book[start:end])
        start = end
    return distribution

with open('result.json', 'w') as file_json:
    list_user = []
    for i in user:
        filtered_user = {key: i[key] for key in i if key in user_reference}
        list_user.append(filtered_user)
    book_distribution = distribute_books(book, list_user)
    for i, user_data in enumerate(list_user):
        user_data['books'] = book_distribution[i]
    json.dump(list_user, file_json, indent=4)
