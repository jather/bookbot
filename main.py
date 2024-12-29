def main(book):
    print(f"--- Begin report of {book}")
    with open(book) as f:
        file_contents = f.read()
        print(f"{wordcount(file_contents)} words found in the document")
        letter_count = countletter(file_contents)
        letter_list = []
        for letter in letter_count:
            if letter.isalpha():
                letter_list.append([letter, letter_count[letter]])
        letter_list.sort()
        print(letter_list)



def wordcount(words):
    count = 0
    for word in words.split():
        count += 1
    return count

def countletter(words):
    lettercounts = {}
    lowercase_words = words.lower()
    for letter in lowercase_words:
        if letter in lettercounts:
            lettercounts[letter] += 1
        else:
            lettercounts[letter] = 1
    return lettercounts

main("books/frankenstein.txt")


