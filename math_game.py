# Week 12 Activity 10
# S10267572C Hector Sim Zi Sheng


from random import randint

def menu():
    print("(1) Addition")
    print("(2) Subtraction")
    print("(3) Multiplication")
    print("(4) Division")
    print("(5) Random Arithmetic Problem")
    choice = int(input("Choose the type of arithmetic problem you wish to practice: "))

    return choice

def print_incorrect_msg(random_message):
    wrong_ans = ["No. Please try again.", "Wrong. Try once more.", "Don\'t give up!", "No. Keep trying."]
    print(f"{wrong_ans[random_message]}")


def print_correct_msg(random_message):
    correct_ans = ["Very good!", "Excellent!", "Nice work!", "Keep up the good work!"]
    print(f"{correct_ans[random_message]}")

symbolList = ["+", "-", "*", "/"]
while True:
    choice = menu()
    num1 = randint(1,10)
    num2 = randint(1,10)
    random_message = randint(0,3)

    while num1 % num2 != 0:
        num1 = randint(1,10)
        num2 = randint(1,10)


    if choice == 5:
        randomChoice = randint(0,3)
        operand = symbolList[randomChoice]
        expression = f"{num1} {operand} {num2}"
        result = eval(expression)
        student_answer = input(f"How much is {num1} {operand} {num2}?: ")

        random_message = randint(0,3)
        if student_answer == result:
            print_correct_msg(random_message)
            break
        else:
            print_incorrect_msg(random_message)
            continue
    
    operand = symbolList[choice]
    expression = f"{num1} {operand} {num2}"
    result = eval(expression)
    student_answer = input(f"How much is {num1} {operand} {num2}?: ")

    random_message = randint(0,3)
    if student_answer == result:
        print_correct_msg(random_message)
        break
    else:
        print_incorrect_msg(random_message)
        continue

 