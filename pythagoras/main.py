from math import sqrt
#result func
def result(result_value):
    result = str(result_value)
    print ("Result : " + result)
print ("left unknown value empty or enter with 0")
#input value
val_a = int(input("Enter value a : ") or "0")
val_b = int(input("Enter value b : ") or "0")
val_c = int(input("Enter value c : ") or "0")
#calculating
if val_c == 0 and val_b != 0 and val_a != 0:
    result_value = sqrt(val_a * val_a + val_b * val_b)
    result(result_value)
elif val_a == 0 and val_b != 0 and val_c != 0:
    result_value = sqrt((val_c * val_c) - (val_b * val_b))
    result(result_value)
elif val_b == 0 and val_a != 0 and val_c != 0:
    result_value = sqrt(val_c * val_c - val_a * val_a)
    result(result_value)
else:
    print('Please enter a value between a, b, c')
