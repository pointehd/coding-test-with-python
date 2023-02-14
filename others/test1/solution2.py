import re


def solution(phone_number: str):
    matches = [
        re.compile("^010-[\d]{4}-[\d]{4}$"),
        re.compile("^010[\d]{8}$"),
        re.compile("^\+82-10-[\d]{4}-[\d]{4}$"),
    ]

    for index, value in enumerate(matches):
        print(value.match(phone_number))
        if value.match(phone_number) != None:
            return index + 1
    return -1


print(
    "aaaaaa",
    solution("010123456780101234567801012345678010123456780101234567801012345678"),
)
