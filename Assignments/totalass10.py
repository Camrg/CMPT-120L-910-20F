import argparse
parser = argparse.ArgumentParser()

# This is prefered
parser.add_argument("-r", "--reverse", help="This will reverse the order of the array", action="store_true")

# This is considered poor practice.
parser.add_argument("number", help="This number will printed from one to the number")   
args = parser.parse_args()



# Factorial

# Provide a number and we'll calculate the factorial of that number.
def array_of_numbers(number):
    total = 0
    for i in range(number):
        num = i+1
        total = total + num
        print(num)
    return total

print(array_of_numbers(int(args.number)))
