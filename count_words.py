def count_words(s):
    # for words in s:
    #     print(words)
    count = 0
    wordsArray = s.split()
    for word in wordsArray:
        for match in range(len(wordsArray)):
            if wordsArray[match] == word:
                count = count + 1
        print(word, count)
        count = 0

def test_run():
    print(count_words("cat bat mat cat bat cat at"))

test_run()
