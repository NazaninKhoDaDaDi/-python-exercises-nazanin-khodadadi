text = input('Enter your text: ')

def analyze_text(text):
    words = text.split()

    a = []
    for i in text:
        if i.isalpha():
            a.append(i)

    b = []
    for i in text:
        if i.isdigit():
            b.append(i)

    c = []
    for i in text:
        if i.isupper():
            c.append(i)

    d = []
    for i in text:
        if i.islower():
            d.append(i)

    letter_count = {}
    maximum = 0
    most_letter = ''

    for i in text:
        if i.isalpha():
            if i in letter_count:
                letter_count[i] = letter_count[i] + 1
            else:
                letter_count[i] = 1

    for i in letter_count:
        if letter_count[i] > maximum:
            maximum = letter_count[i]
            most_letter = i

    word_count = {}
    max_word = 0
    most_word = ''

    for i in words:
        if i in word_count:
            word_count[i] = word_count[i] + 1
        else:
            word_count[i] = 1

    for i in word_count:
        if word_count[i] > max_word:
            max_word = word_count[i]
            most_word = i

    new_words = []

    for i in words:
        if i.isalpha():
            new_words.append(i)

    longest = ''
    max_length = 0

    for i in new_words:
        if len(i) > max_length:
            max_length = len(i)
            longest = i

    shortest = new_words[0]
    min_length = len(new_words[0])

    for i in new_words:
        if len(i) < min_length:
            min_length = len(i)
            shortest = i

    palindrome_count = 0

    for i in words:
        if i == i[::-1]:
            palindrome_count += 1

    result = {
        'words': len(words),
        'letters': len(a),
        'digits': len(b),
        'most_common_letter': most_letter,
        'most_common_word': most_word,
        'longest_word': longest,
        'shortest_word': shortest,
        'palindrome_words': palindrome_count,
        'uppercase': len(c),
        'lowercase': len(d)
    }

    for i in result:
        print(i, ':', result[i])


analyze_text(text)
