#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_user_info(**users):
    for username, info in users.items():
        print(f"User: {username}")
        for key, value in info.items():
            print(f"{key}: {value}")
        print()


if __name__ == "__main__":
    print_user_info(
        Anna={"age": 25, "city": "Moscow"},
        Boris={"age": 30, "city": "Stavropol", "email": "boris@mail.ru"},
        Clara={"age": 28, "city": "Pyatigorsk", "phone": "31-67-64"}
    )
