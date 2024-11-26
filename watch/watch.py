import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^.+"https?://(?:www.)?youtube.com/embed/(.+?)"', s, re.IGNORECASE):
        url = "https://youtu.be/" + matches.group(1)
        return url
    else:
        return None

if __name__ == "__main__":
    main()
