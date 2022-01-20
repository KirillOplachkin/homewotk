import re



'''
\d -- Он ищет подряд стоящие числа [0 - 9]
\D -- Он ищет любые, но не числа
\w -- Ищет дюбой алфавитный символ [A-Z a-z]
\W -- Любой не алфавитный символ
\s -- ищет пробелы
\S -- специальные символы
'''

file_path = 'MOCK_DATA.txt'
result_fio = 'fio.txt'
result_email = 'email.txt'
result_ex = 'extension.txt'
result_colour = 'colour.txt'


file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file_fio = open(result_fio, mode='w', encoding='Latin-1')
result_file_email = open(result_email, mode='w', encoding='Latin-1')
result_file_ex = open(result_ex, mode='w', encoding='Latin-1')
result_file_colour = open(result_colour, mode='w', encoding='Latin-1')

my_text_file = file_reader.read()

what_search = r'[\w_-]+@[\w_-]+.[\w.]+'
results = re.findall(what_search, my_text_file)

#почта
for item in results:
    print(item)
    result_file_email.write(item + '\n')

print(f'Total results of file: {str(len(results))}')


what_search = r'#[\d[a-z]\w+'
results = re.findall(what_search, my_text_file)

for item in results:
    print(item)
    result_file_colour.write(item + '\n')
print(f'Total results of file: {str(len(results))}')

what_search = r"[A-Z][a-z_-]+[\s][de\sA-Z'\s]+[a-zA-Z]+"
results = re.findall(what_search, my_text_file)
#фио
for item in results:
     print(item)
     result_file_fio.write(item + '\n')
print(f'Total results of file: {str(len(results))}')

#расширение

what_search = r'[A-Z\s]+[a-zA-Z]+[.][a-z\d]+'
results = re.findall(what_search, my_text_file)

for item in results:
     print(item)
     result_file_ex.write(item + '\n')
print(f'Total results of file: {str(len(results))}')




