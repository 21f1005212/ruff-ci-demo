import os
import sys


def analyze():
    result = os.path.join(sys.prefix, "data")
    return result


if __name__ == "__main__":
    print(analyze())
