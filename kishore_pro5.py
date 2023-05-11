""" 5.program to check student grades """
#taking user inputs
print("Enter Marks Obtained in 5 Subjects: ")
sub1 = int(input("Enter the marks of first subject:"))
sub2 = int(input("Enter the marks of second subject:"))
sub3 = int(input("Enter the marks of third subject:"))
sub4 = int(input("Enter the marks of fourth subject:"))
sub5 = int(input("Enter the marks of fifth subject:"))

tot = sub1+sub2+sub3+sub4+sub5 #taking total marks of subject
avg = tot/5 #taking average marks
# checking if avg is between 91 and 100
if avg>=91 and avg<=100:
    print("Your Grade is A1")#print this as output if condition satisfied

# checking if avg is between 81 and 91
elif avg>=81 and avg<91:
    print("Your Grade is A2")#print this as output if condition satisfied

# checking if avg is between 71 and 81
elif avg>=71 and avg<81:
    print("Your Grade is B1")#print this as output if condition satisfied

# checking if avg is between 61 and 71
elif avg>=61 and avg<71:
    print("Your Grade is B2")#print this as output if condition satisfied

# checking if avg is between 51 and 61
elif avg>=51 and avg<61:
    print("Your Grade is C1")#print this as output if condition satisfied

# checking if avg is between 41 and 51
elif avg>=41 and avg<51:
    print("Your Grade is C2")#print this as output if condition satisfied

# checking if avg is between 33 and 41
elif avg>=33 and avg<41:
    print("Your Grade is D")#print this as output if condition satisfied

# checking if avg is between 21 and 33
elif avg>=21 and avg<33:
    print("Your Grade is E1")#print this as output if condition satisfied

# checking if avg is between 0 and 21
elif avg>=0 and avg<21:
    print("Your Grade is E2")#print this as output if condition satisfied

#this block will execute if none of the above condition is satisfied    
else:
    print("Invalid Input!")#print this as output
