# 1 - Write a Python function that checks whether a passed string is palindrome or not. A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def IsPalindrome(String):
    Str = String.replace(' ', '')
    length = len(Str)
    h = 0
    j = length - 1 
    while ((h < length) & (j >= 0) ):
        if( Str[h] != Str[j]):
            return print("\nThis String ",String," is not palindrome\n")
        h = h + 1
        j = j - 1 
    print("\nThis String ",String," is palindrome\n")
print("\n1 - Check whether a passed string is palindrome or not\n")
String = input("Enter a String : ")
IsPalindrome(String)
# 2 - Write a Python function that takes a number as a parameter and checks if the number is prime or not. A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def IsPrime(Number):
    cpt = 0
    for i in range (1 , Number + 1):
        if (Number % i == 0):
            cpt = cpt + 1
    if (cpt == 2 ):
        return print("\nThis number ",Number," is a prime\n")
    else:
        return print("\nThis number ",Number," is not a prime\n")
print("\n2 - Check if a number is prime or not.\n")
Number = int (input("Enter a number : "))
IsPrime(Number)
# 3 - Write a Python function to check whether a number is in a given range.
def IsInRange(Number , A , B):
    if (A < B):
        if ((Number >= A) & (Number <= B)):
            return print("\nThis number ",Number," is in the ragne [",A,B,"]\n")
        else:
            return print("\nThis number ",Number," is not in the ragne [",A,',',B,"]\n")
    else:
         return print("\nThis range is invalid!!\n")
print("\n3 - Check if a number is in a given range.")
Number = int(input("\nEnter a number : "))
a = int(input("\nGive the lower bound of the interval: "))
b = int(input("\nGive the upper bound of the interval: "))
IsInRange(Number, a, b )
# 4 - Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def Factorial(Number):
    Fact = 1
    if Number > 0 :
        for i in range (1 , Number+1):
            Fact = Fact * i
    return print("\nThe factorial of ",Number,"is ",Fact,"\n")
print("\n4 - Calculate the factorial of a number.\n")
Number = int(input("Give the Number that you want to calculate its factorial : "))
Factorial(Number)
# 5 - Write a Python program to reverse a string.
def ReverseString(String):
    newString = String[::-1]
    return print("\nThe string after the reverse operation is :",newString,"\n")
print("\n5 - Reverse a string.\n")
String = input("Give the string that you want to reverse : ")
ReverseString(String)
# 6 - Write a Python function to sum all the numbers in a list.
def SumList(List):
    sum = 0
    for n in List:
        sum = sum + n
    return print("The sum of all the elements in the list is : ", sum,"\n")
print("\n6 - The sum of all the numbers in a list.\n")
List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
SumList(List)
# 7 - Write a Python function to find the Max of three numbers.
def FindMax(a,b,c):
    Max = max(a,b)
    Maximum = max(Max,c)
    return print("\nThe maximum of ",a,",",b,"and",c,"is :", Maximum,"\n")
print("\n7 - Find the Max of three numbers.\n")
x = (input("Enter 3 numbers : (a space between each number is required!!) ").split())
a = int(x[0])
b = int(x[1])
c = int(x[2])

FindMax(a,b,c)