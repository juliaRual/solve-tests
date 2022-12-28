from spmi import tests
import random

database = tests('test.txt')


while True:
    q = random.choice(database)
    true_answer = None
    true_answer_text = None
    for elem in range(1, len(q)):
        if q[elem][0] == '@':
            true_answer = elem
            true_answer_text = q[elem][1:]
            q[elem] = q[elem][1:]
    text = f"""
{q[0]}

{q[1]}
{q[2]}
{q[3]}
{q[4]}
"""
    x = input(text)
    if x == true_answer:
        print("[+] Correct!")
    else:
        print("[-] Incorreect! see: " + true_answer_text)