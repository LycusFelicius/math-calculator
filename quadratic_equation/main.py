#www.github.com/LycusFelicius
from math import sqrt
#result func
def result(result_value_a, result_value_b):
    result_a = str(result_value_a)
    result_b = str(result_value_b)
    print ("x : " + result_a + " or x : " + result_b)
#input value
def main():
    print("Roots Quadratic Equation Solver")
    #input
    val_a = int(input("Enter value a : "))
    val_b = int(input("Enter value b : "))
    val_c = int(input("Enter value c: "))
    #return if value unknown or missing
    if not val_a or not val_b or not val_c:
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