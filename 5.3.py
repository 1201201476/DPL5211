#Student ID:1201201476
#Student Name: Eng Hong Chee

#Display the menu. 
#Ask the user to enter their choice [1 or 2]. 
#Using a switch-case statement: 
#If choice is 1 call function get_cm(). 
#If choice is 2 call function get_meter(). 
#Else print “Invalid choice"

def get_cm():
    cm=float(input("Please enter a value for centimeter : "))
    m=cm_to_meter(cm)
    print("For {} cm is equal to {} meter".format(cm,m))

def cm_to_meter(centimeter):
    meter=centimeter/100
    return meter

def get_meter():
    m=float(input("Please enter a value for meter : "))
    cm=m_to_cm(m)
    print("For {} meter is equal to {} cm".format(m,cm))

def m_to_cm(meter):
    centimeter=meter*100
    return centimeter

print("====================================== ")
print("                MENU ")
print("====================================== ")
print("  1.    Convert centimeter to meter ")
print("  2.    Convert meter to centimeter ")
print("======================================") 

choice=int(input("Enter your choice : ")) 

if (choice==1):
    get_cm()
elif(choice==2):
    get_meter()
else:
    print("Invalid Value!!")
