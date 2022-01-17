print('Вводите строки для записи в файл, для прекращения введите пустую строку')
with open('data.txt', 'w', encoding='utf-8') as f_prompt:
    while True:
        text = input()
        if not text:
            break
        else:
            f_prompt.write(f'{text}\n')
# with open('data.txt', 'r') as f:
#     for i in f:
#         print(i)
