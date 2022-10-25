'''
1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
'''

my_line = 'абвгдейка, абвгдейка, тест, фыварлг'

my_line = list(filter(lambda x: 'абв' not in x, my_line.split()))

print(' '.join(my_line))
