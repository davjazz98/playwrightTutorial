

# Without assertion
def my_devision_1(num1, num2):
    return num1/num2

print(my_devision_1(10,2))

# With assertion
def my_devision_2(num1, num2):
    assert num2 != 0, f"You can't divide number on zero!"
    return num1/num2

print(my_devision_2(10,0))