#!/bin/python3
import yaml, os, argparse
parser = argparse.ArgumentParser(description='Quiz App')
parser.add_argument('-f', '--file', help='YAML file to load', required=True)
args = parser.parse_args()

os.system('clear')
lsts = yaml.load_all(open(args.file,'r'), Loader=yaml.FullLoader)

coll = [ x for x in lsts ]
correct = 0
for qnum, lst in enumerate(coll):
    question = lst['q']
    options = lst['o']
    answers = str(lst['a'])
    print(f"[{qnum}/{len(coll)}]")
    print(question)

    coll_options = []
    for num, option in enumerate(options):
        print(f"{num}: {option}")
        coll_options.append(str(num))
    choose = input(f"Enter {','.join(coll_options)}: ")
    if ',' in answers:
        print(f"There are {list(answers).count(',') + 1} options")
    if choose == answers:
        print("Correct")
        correct += 1
    else:
        print('Incorrect')
    input("Press Enter to continue...")
    os.system('clear')
    continue
os.system('clear')
print(f"Correct: {correct}/{len(coll)}")
