"""
Area Calculator:
Ask a user to select a shape to calculate
the area of that shape and print the output
"""
print("Area Calculator starting...\n")
option = input("Enter C for Circle or T for Triangle: ")
option = option.lower()
if option == "c" and option.isalpha():
    radius = float(input("Please enter the Radius of the circle: "))
    area = 3.14159 ** radius
    print(f"The area of your circle is {area}")
elif option == "t" and option.isalpha():
    base = float(input("Please enter the Base of the triangle: "))
    height = float(input("Please enter the Height of the triangle: "))
    area = (base/2)*height
    print(f"the area of the triangle is {area}")
else:
    print("You haven't chosen a viable shape")
print("Area Calculator closing...")
