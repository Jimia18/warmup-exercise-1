#Create a program to calculate the area of a triangle (1/2*base*height)
#Base and height shoud be entered using the keyboard

def area_of_a_triangle():

     base = int(input("\nEnter the base of the triangle: "))
     height = int(input("Enter the height of the triangle: "))

     area =((1/2) * base * height)

     print(f"The area of the triangle of base{base} and height{height} is {area:.3f}")

area_of_a_triangle()
