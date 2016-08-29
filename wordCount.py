def main():
    userText = input('TEXT: ')
    word_count = {}
    for word in userText.split():
        word_count[word] = word_count.get(word, 0) + 1

    max_len = len(max(word_count, key=len))
    for word in sorted(word_count.keys()):
        print('{:{}} : {}'.format(word, max_len, word_count[word]))

main()
