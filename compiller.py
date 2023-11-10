import os
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("файл", type=str)

args=parser.parse_args()


with open(args.файл, 'r', encoding='utf-8') as file:
    code = file.read()

    commands = {'промолвить': 'print',
                'коли': 'if',
                'отнюдь': 'else',
                'целина': 'int',
                'внемлить': 'input',
                'списокъ': 'list',
                'перепись': 'dict',
                'бить_ящеровъ': 'break',
                'добить_ящеровъ': 'continue',
                'правда': 'true',
                'кривда': 'false',
                'казнь': 'del',
                'воздать': 'return',
                'внедрить': 'import',
                'получи_басурманъ': 'raise',
                'пытать_ящера': 'try',
                'поймать_ящера': 'except',
                'народный': 'global',
                'царский': 'nonlocal',
                'хуторъ': 'def',
                'много_букавъ': 'str',
                'мерило': 'len',
                'розсудъ': 'bool',
                'дробь': 'float',
                'изъ': 'from',
                'для':'for',
                'въ': 'in',
                'перебрать': 'range'
                }
    new_code=code

    for i in commands: new_code=new_code.replace(i, commands[i]);

    with open('temp.py', 'w', encoding='utf-8') as temp:
        temp.write(new_code)
os.system('python temp.py')