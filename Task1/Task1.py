# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Напишите текст для удаления лишнего слова \n')
words = list(input('Введите слово или несколько слов через пробел для удаления из текста \n').split())
txt = text.split()
resultwords  = [word for word in txt if word.lower() not in words]
result = ' '.join(resultwords)
print(result)