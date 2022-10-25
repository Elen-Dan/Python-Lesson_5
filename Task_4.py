'''
4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
 Входные и выходные данные хранятся в отдельных текстовых файлах.
'''
with open('origin.txt', 'r') as data:
    my_text = data.read()

def fnc_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
    return encoding

encoding = fnc_encode(my_text)
print(encoding)

with open('encoded.txt', 'r') as data:
    my_text2 = data.read()

def fnc_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

decode = fnc_decode(my_text2)
print(decode)