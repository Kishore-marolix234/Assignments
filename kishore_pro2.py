""" Write a program that prompts the user to enter their age. If the age is less than 18,
the program should print a message saying that the user is not old enough to vote.
If the age is between 18 and 65, the program should print a message saying that
the user is eligible to vote. If the age is greater than 65,
the program should print a message saying that the user is eligible to vote, 
but they may choose to retire instead. """

Age = int(input("Enter the age of a person: "))#taking the user age as input
if (Age>0 and Age<18):#checking if the age is between 0 and 18 years
    print("User is not old enough to vote.")#print this output if above condition satisfied
elif(Age>=18 and Age<=65):#checking if the age is between 18 and 65 years
    print("The user is eligible to vote.")#print this output if above condition satisfied
elif(Age>65 and Age<=100): #checking if the age is between 65 and 100 years
    print("the user is eligible to vote,\n but they may choose to retire instead.")#print this output if above condition satisfied
else:
    print("Invalid Age")   #print this output if none of the above condition is satisfied.         