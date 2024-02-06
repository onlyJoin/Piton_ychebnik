import argparse

"""

required нужен для указания обязательности передачи аргумента

True - обязательно передавать

False - необязательно передавать

"""

parser = argparse.ArgumentParser()

parser.add_argument('--test', required=True, nargs='*', dest='argg')

args = parser.parse_args()

argg = args.argg
print(argg)

# python main.py 50 => Error

# python main.py --test 50 => ['50']
