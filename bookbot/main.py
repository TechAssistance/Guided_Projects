def countWords(file_content):
    words = file_content.split()
    countBoi = 0
    for word in words:
        countBoi += 1
    return countBoi

def countLetters(file_content):
    lettersDic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0,}
    lowcase = file_content.lower()
    count = 0
    for letter in lettersDic:
        lettersDic[letter] = lowcase.count(letter)
    for letter in lettersDic:
        count += lettersDic[letter]
    return count, lettersDic


filename = "books/frankenstein.txt"
with open(filename) as f:
    file_content = f.read()
    total_words = countWords(file_content)
    totalLetterCount, indvletterCount = countLetters(file_content)
    print(f"----- BEGIN REPORT FOR {filename} -----")
    print(f"{total_words} words found in the document")
    print(f"{totalLetterCount} letters were found in the document")
    for letter in indvletterCount:
        print(f"The {letter} character was found {indvletterCount[letter]} times")
    
    print("------ END OF REPORT -----")
