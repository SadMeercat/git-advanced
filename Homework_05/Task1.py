# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

line = 'Абвгдейка - это передача'.lower()

words = line.split(' ')

fragment = 'абв'
# новый список оставшихся слов
new_words = []
for word in words:
     if fragment not in word:
         new_words.append(word)

line = ' '.join(new_words)
print (line)