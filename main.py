import json

import nba


def main():
    news = nba.get_news(5)
    if (news == []):
        print("shempty")
        return 0

    for a in news:
        print(f"Site: {a['source']}")
        print(a['title'])
        print()

if __name__ == "__main__":
    main()
