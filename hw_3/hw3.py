import json
from csv import DictReader


def distribute_books(books, users):
    distribution = [[] for _ in range(len(users))]
    user_index = 0
    for b in books:
        distribution[user_index].append(b)
        user_index = (user_index + 1) % len(users)
    return distribution


def book(file_book: str, argument_book: list):
    with open(file_book, 'r', encoding='utf-8') as file_csv:
        books = list(DictReader(file_csv))
    filtered_books = []
    for b in books:
        filtered_book = {
            key.lower(): b[key]
            for key in b
            if key.lower() in [arg.lower() for arg in argument_book]
        }
        filtered_books.append(filtered_book)
    return filtered_books


def user(file_user: str, argument_user: list):
    with open(file_user, 'r') as file_json:
        users = json.load(file_json)
    filtered_users = []
    for u in users:
        filtered_user = {key: u[key] for key in u if key in argument_user}
        filtered_users.append(filtered_user)
    return filtered_users


def new_file(book_file: str,argument_book: list, user_file: str, argument_user: list, output_file: str):
    books = book(book_file,argument_book)
    users = user(user_file, argument_user)
    book_distribution = distribute_books(books, users)
    for i, user_data in enumerate(users):
        user_data['books'] = book_distribution[i]

    with open(output_file, 'w') as file_json:
        json.dump(users, file_json, indent=4)


if __name__ == "__main__":
    new_file(
        "books.csv",
        ["title", "author", "pages", "genre"],
        "user.json",
        ["name", "gender", "address", "age"],
        "result.json"
    )

