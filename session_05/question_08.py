s = input('Enter text: ')
a = s.split()

letters = 0
digits = 0
spaces = 0
upper = 0
lower = 0
longest = 0
longest_word = ''
shortest_word = a[0]
char = {}
max_count = 0
most_char = ''
words = {} 
max_word = 0
most_word = ''

total_characters = len(s)
print('Total characters : ' , total_characters )

total_words = len(a)
print('Total words : ' , total_words )

for i in s : 
    if i.isalpha():
        letters = letters + 1
print('Total letters : ' , letters )

for i in s : 
    if i.isdigit():
        digits = digits + 1
print('Total digits : ' , digits )

for i in s : 
    if i == ' ':
        spaces = spaces + 1
print('Total spaces : ' , spaces )

for i in s : 
    if i.isupper():
        upper = upper + 1
print('Total uppercase : ' , upper )


for i in s : 
    if i.islower():
        lower = lower + 1
print('Total lowercase : ' , lower )


for i in a : 
    if len(i) > longest :
        longest = len(i)
        longest_word = i
print('Longest word : ' , longest_word )

for i in a : 
    if len(i) < len(shortest_word) :
        shortest_word= i
print('Shortest word : ' , shortest_word )


for i in s :
   if i in char :
        char[i] = char[i] + 1
   else : 
        char[i] = 1

for i in char:
    if i.isalpha():
       if char[i] > max_count :
           max_count = char[i]
           most_char = i
        
print('Most repeated character : ', most_char)

for i in a :
    if i in words:
        words[i] = words[i] + 1
    else :
        words[i] = 1

for i in words:
    if words[i] > max_word :
        max_word  = words[i]
        most_word = i
print('Most repeated word : ' , most_word)
        
    
    
    
    