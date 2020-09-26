
def function():
    x=int(input('Please enter number'))
    totalSum = 0
    for i in range(x+1):
        totalSum += i
    return(totalSum)
print(function())