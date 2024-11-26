
def main():
    ans = input("Input: ")
    ans = shorten(ans)
    print("Output: " + ans)



def shorten(word):
    new_ans = ""
    for i in range(len(word)):
        if word.lower()[i] not in ["a", "e", "i", "o", "u"]:
            new_ans += word[i]
    return new_ans


if __name__ == "__main__":
    main()
