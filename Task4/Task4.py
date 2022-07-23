# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('Input_HWPS_5.txt', 'w') as file:
    str1 = "AAAbbDDDDDckkkerzzzz"
    file.write(f'{str1}')
    
with open('Input_HWPS_5.txt', 'r') as file: #Task4\Task4.py
        inp_ut = file.readline()

def encode(message):
    encoded_message = ""
    i = 0
    while (i <= len(message)-1):
        count = 1
        ch = message[i]
        j = i
        while (j < len(message)-1):
            if (message[j] == message[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message=encoded_message+str(count)+ch
        i = j+1
    return encoded_message

encoded_message=encode(inp_ut)
print(encoded_message)

with open('Encoded_HWPS_5.txt', 'w') as file:
    file.write(encoded_message)

def decode(our_message):
    decoded_message = ""
    i = 0
    j = 0
    # Разделение сообщения на счётчики
    while (i <= len(our_message) - 1):
        run_count = int(our_message[i])
        run_word = our_message[i + 1]
        # Отображение символа такого количества раз, сколько указано в счётчике
        for j in range(run_count):
            # Склейка декодированного сообщения
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message

decoded_message=decode(encoded_message)
print(decoded_message)

with open('Output_HWPS_5.txt', 'w') as file:
    file.write(decoded_message)

