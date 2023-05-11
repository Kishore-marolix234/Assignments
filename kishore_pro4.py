""" 4.to check given input number is equal to 20,80,500 """
#taking the user input
num = int(input("Enter the number: "))
#check if num is equal to 20
if num==20:
    print("The number is equal to 20")#print this statement if above condition is satisfied
#check if num is equal to 80    
elif num==80:
    print("The number is 80") #print this statement if above condition is satisfied
#check if num is equal to 500    
elif num==500:
    print("The number is 500") #print this statement if above condition is satisfied
else:
    #this statement is printed if none of the above condition satisfied
    print("Please give the input among 20,80 and 500 only")            