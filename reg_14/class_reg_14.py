import re



'''
\d -- Он ищет подряд стоящие числа [0 - 9]
\D -- Он ищет любые, но не числа
\w -- Ищет дюбой алфавитный символ [A-Z a-z]
\W -- Любой не алфавитный символ
\s -- ищет пробелы
\S -- специальные символы
'''

file_path = 'demo_mock_data.txt'
result_file_path = 'result.txt'

file_reader = open(file_path, mode='r', encoding='Latin-1')
result_file = open(result_file_path, mode='w', encoding='Latin-1')
my_text_file = file_reader.read()

what_search = r'[\w_-]+(?!rsmedmoreie)@(?!intel)(?!yahoo)[\w_-]+.[\w.]+'
results = re.findall(what_search, my_text_file)

for item in results:
    print(item)
    result_file.write(item + '\n')

print(f'Total results of file: {str(len(results))}')


# what_search = r'[5-9]'
# results = re.findall(what_search, my_text)
# print(results)
