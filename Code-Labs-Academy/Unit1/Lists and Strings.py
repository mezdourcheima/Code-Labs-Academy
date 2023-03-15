#Create a list that contains all the even numbers between 1 and 299.

list = []
list_1 = []
for i in range (1,299):
    if (i % 2) == 0 :
        list.append(i)

print("\nThe list is : ",list)

#Iterate through the previously created list and print first the length of the list then all the squared values of the list.

print("\nThe length of the list is : ",len(list))

for j in list:
    list_1.append(j**2)

print("\nThe squared values of the list are : ", list_1)

#In one line check if 57 is in the list using one line of python.

print(57 in list) # Returns true if 57 is in the list and False if not


