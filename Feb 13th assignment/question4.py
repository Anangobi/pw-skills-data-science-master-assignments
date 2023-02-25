x = (1, 2, 3, 4)
try:
    print(x[10])
except LookupError as e:
    print(f"{e}, {e.__class__}")

pylenin_info = {'name': 'Lenin Mishra',
                'age': 28,
                'language': 'Python'}
user_input = input('What do you want to learn about Pylenin==> ')

try:
    print(f'{user_input} is {pylenin_info[user_input]}')
except LookupError as e:
    print(f'{e}, {e.__class__}')
