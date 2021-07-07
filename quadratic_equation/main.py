#www.github.com/LycusFelicius
from math import *
#result func
def result(result_value_a, result_value_b):
    result_a = str(result_value_a)
    result_b = str(result_value_b)
    print ("x : " + result_a + " or x : " + result_b)
#main func
def main():
    print("Roots Quadratic Equation Solver")
    #input value
    val_a = float(input("Enter value a : ") or "0")
    val_b = float(input("Enter value b : ") or "0")
    val_c = float(input("Enter value c : ") or "0")
    #return if value unknown or missing
    if val_a == 0 or val_b == 0 or val_c == 0:
        return
    #result a
    result_up_a = -val_b + sqrt((val_b * val_b) - (4 * val_a * val_c))
    result_down_a = 2 * val_a
    result_value_a = result_up_a / result_down_a
    #result b
    result_up_b = -val_b - sqrt((val_b * val_b) - (4 * val_a * val_c))
    result_down_b = 2 * val_a
    result_value_b = result_up_b / result_down_b
    result(result_value_a, result_value_b)
main()