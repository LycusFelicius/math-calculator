#formula : (M1 X C1) (T1-Ta) = (M2 X C2) (Ta-T2)
from math import *
#result func
def result(result_value):
    result = str(result_value)
    print ("Result : " + result)
def main():
    print ("left the unknown value empty or enter with 0")
    #input value
    val_m1 = float(input("Enter value M1 : ") or "0")
    val_m2 = float(input("Enter value M2 : ") or "0")
    val_c1 = float(input("Enter value C1 : ") or "0")
    val_c2 = float(input("Enter value C2 : ") or "0")
    val_delta1 = float(input("Enter value ∆T1 : ") or "0")
    val_delta2 = float(input("Enter value ∆T2 : ") or "0")
    val_t1 = float(input("Enter value T1 : ") or "0")
    val_t2 = float(input("Enter value T2 : ") or "0")
    #calculating
    if val_delta1 == 0 and val_delta2 == 0 and val_t1 != 0 and val_t2 != 0:
        val_mc1 = val_m1 * val_c1
        val_mc2 = val_m2 * val_c2
        val_dt1 = val_mc1 * val_t1
        val_dt2 = val_mc2 * val_t2
        result_value = (val_dt1 + val_dt2) / (val_mc1 + val_mc2)
        result(result_value)
main()