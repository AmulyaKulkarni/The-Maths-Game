import random

MIN_NUMBER = 1
MAX_NUMBER = 10
NUM_QUESTION = 4


def ask_question():
    a = random.randint(MIN_NUMBER,MAX_NUMBER)
    b = random.randint(MIN_NUMBER,MAX_NUMBER)
    o = random.randint(0,1)
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    answer_str = input(f"Compute: {a} {operator_str} {b} = ")
    answer_int = int(answer_str)
    compute = a+b
    if o == 1:
        compute = a*b
    if answer_int == compute:
        return True

    return False

num_points = 0

for i in range(0, NUM_QUESTION):
    print(f"Question No.{i+1} out of {NUM_QUESTION}:")
    if ask_question():
        print("Right answer")
        num_points += 1
    else:
        print("Wrong answer")

    print()

print(f"Your points: {num_points} out of {NUM_QUESTION}")

adverage = int(NUM_QUESTION/2)
if num_points == NUM_QUESTION:
    print("Excellent!")
elif num_points == 0:
    print("Improve your maths")
elif num_points > adverage:
    print("Good!")
else:
    print("You can do better!")
