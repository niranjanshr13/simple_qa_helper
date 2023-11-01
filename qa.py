#!/bin/python3
import yaml, os
os.system('clear')
lsts = yaml.load_all(open('yaml.yml','r'), Loader=yaml.FullLoader)

coll = [ x for x in lsts ]
correct = 0
for qnum, lst in enumerate(coll):
    question = lst['q']
    options = lst['o']
    print(f"[{qnum}/{len(coll)}]")
    print(question)
    coll_options = []

    for num, option in enumerate(options):
        
        print(f"{num}: {option}")
        coll_options.append(str(num))
    choose = input(f"Enter {','.join(coll_options)}: ")
    if int(choose) == lst['a']:
        print("Correct")
        correct += 1
    else:
        print('nop')
    input("Press Enter to continue...")
    os.system('clear')
print(f"Correct: {correct}/{len(coll)}")