 #1 - Read all of the content of the file in one variable.
print("1 - Read all of the content of the file in one variable\n")
file = open("HomeWorks/Student_Names.txt")  #The file Student_Names and this file were created in a folder with the name of HomeWorks.

students = file.read()
print(students)

#2 - Write a list of random names to your file.
print("\n2 - Write a list of random names to your file.\n")
list = [ "Isla Phillips",
        "Judith Richard ",
        "Jameson Oneal ",
        "Braydon Beard ",
        "Howard Waller ",
        "Zavier Joseph ",
        "Haven Douglas ",
        "Hannah Hurley ", 
        "Alan Hahn ",
        "Jason Yates ", 
        "Phoenix Friedman ",
        "Christine Williamson"]

file = open("HomeWorks/Student_Names.txt" , "w")  #The file Student_Names and this file were created in a folder with the name of HomeWorks

for name in list :
    students = students + "\n" + name 
file.write(students)  

print(students)
# 3 - Read the first n lines of the file.
print("\n3 - Read the first n lines of the file.\n")

file = open("HomeWorks/Student_Names.txt" , "r")  #The file Student_Names and this file were created in a folder with the name of HomeWorks.
n = input("Give the number of lines you want to read : ")
lines = file.readlines()
N = int (n)
first_lines = lines[:N]
print(first_lines)

# 4 - Read the last n lines of the file.
print("\n4 - Read the last n lines of the file.\n")
file = open("HomeWorks/Student_Names.txt" , "r") #The file Student_Names and this file were created in a folder with the name of HomeWorks.
n = input("Give the number of lines you want to read : ")
lines_1 = file.readlines()
N = int (n)
last_lines = lines_1[-N:]
print(last_lines)

# 5 - Check if the name x is in the file.
print("\n5 - Check if the name x is in the file.\n")
file = open("HomeWorks/Student_Names.txt" , "r")  #The file Student_Names and this file were created in a folder with the name of HomeWorks.
name = input("Give the name you want to search for : ")
if name in file.read():
    print("\nYes, this name ' ",name,"' exists in the file")
else:
    print("\nThe name '",name,"' doesn't exist in the file")

#6 - Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
print("\n6 - Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.")
letters = ["A" ,"B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for lettre in letters:
    filename = lettre +".txt"
    File = open(filename,"x")
print("\nThe files has been created successfuly!!")
