from math import sqrt
#result func
def result(result_value):
    result = str(result_value)
    print ("Result : " + result)
print ("fill unknown value with 0")
#input value
val_a = int(input("Enter value a : "))
val_b = int(input("Enter value b : "))
val_c = int(input("Enter value c: "))
if val_c == 0:
    result_value = sqrt(val_a * val_a + val_b * val_b)
    result(result_value)
elif val_a == 0:
    result_value = sqrt((val_c * val_c) - (val_b * val_b))
    result(result_value)
elif val_b == 0:
    result_value = sqrt(val_c * val_c - val_a * val_a)
    result(result_value)
else:
    print('Please select a value between a, b, c')
