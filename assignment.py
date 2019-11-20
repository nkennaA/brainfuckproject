def askName():
    x = input("What is your name brodie?")
    print("Hello " + x)
def arrayContains(arr, item):
    if item in arr:
        return True
    return False
def sumOfNumbers(n):
    j = 0
    for i in range(n+1):
        j+=i
    return j
