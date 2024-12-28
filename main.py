def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(wordcount(file_contents))


def wordcount(words):
    count = 0
    for word in words.split():
        count += 1
    return count

main()
