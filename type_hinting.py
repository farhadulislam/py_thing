# compatible only with py version 3.6 and above
import sys


def isElligible(platform: str, age: int) -> bool:
    if platform == "facebook" and age > 13:
        return True
    elif platform == "twitter" and age > 18:
        return False


def isElligible2(platform: str, age: int) -> bool:
    return (platform == "facebook" and age > 13) or (platform == "twitter" and age > 18)


print(isElligible("facebook", 18))
print(isElligible2("twitter", 20))

