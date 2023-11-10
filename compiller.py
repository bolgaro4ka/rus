import os
import argparse
'''
parser=argparse.ArgumentParser()
parser.add_argument("файл", type=str)

args=parser.parse_args()
'''

with open('тест.русь', 'r', encoding='utf-8') as file:
    code = file.read()

    commands = {'промолвить': 'print',
                'коли': 'if',
                'отнюдь': 'else',
                'целина': 'int',
                'внемлить': 'input',
                'список': 'list',
                'перепись': 'dict',
                'бить_ящеров': 'break',
                'добить_ящеров': 'continue',
                'правда': 'true',
                'кривда': 'false',
                'казнь': 'del',
                'воздать': 'return',
                'внедрить': 'import',
                'получи_басурман': 'raise',
                'пытать_ящера': 'try',
                'поймать_ящера': 'except',
                'народный': 'global',
                'царский': 'nonlocal',
                'хутор': 'def',
                'много_букав': 'str',
                'мерило': 'len',
                'розсуд': 'bool',
                'дробь': 'float',
                'из': 'from'

                }
    new_code=code

    for i in commands: new_code=new_code.replace(i, commands[i]);

    with open('temp.py', 'w', encoding='utf-8') as temp:
        temp.write(new_code)
os.system('python temp.py')