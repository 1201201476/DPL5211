#Student ID:1201201476
#Student Name: Eng Hong Chee

def rectangle():
    area_rec=length*width
    print("\nRectangle area : ",area_rec)
    return area_rec

def triangle():
    area_tri=(0.5)*length*width
    print("Trianle area : ",area_tri)
    return area_tri

i=0
while(i<2):
    i=i+1
    width=float(input("\n\nEnter width : "))
    length=float(input("Enter length : "))
    rectangle()
    triangle()
