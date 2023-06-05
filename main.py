import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_cal(height,width,coverage):
    result = math.ceil((test_h * test_w) / coverage)
    print(f"You will need {result} cans of paint")

paint_cal(test_h,test_w,coverage)