dictionary = {'Rahul':44,'Himanshu':40,'Manish':65,'Alice':85}
a = input("Enter the student's name: ")
if (a in dictionary) == True:
    print(a+"'s marks:",dictionary[a])
else:
    print("Student not found.")