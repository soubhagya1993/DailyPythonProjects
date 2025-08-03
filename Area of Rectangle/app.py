# In this project, you'll create a Python program that calculates both the area and the perimeter of a 
# rectangle using separate functions. This is a foundational exercise that helps reinforce the use of functions, 
# arithmetic operations, and code organization.



def rectangle_area(length,breath):
    rect_area = length * breath
    print(f"Area of Rectangle is {rect_area}")

def rectangle_perimeter(length,breath):
    rect_peri = 2 * (length + breath)
    print(f"Perimeter of Rectangle is {rect_peri}")

rectangle_area(10,3)

rectangle_perimeter(10,3)