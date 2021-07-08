def choices(choice):
    if choice == 1:
        import sys
        sys.path.append("./pythagoras")
        import pythagoras_py
        pythagoras_py
    elif choice == 2:
        import sys
        sys.path.append("./quadratic_equations")
        import quadratic_py
        quadratic_py
    elif choice == 3:
        import sys
        sys.path.append("./black_principle")
        import blackprinciple_py
        blackprinciple_py
def main():
    print ("What are you looking for?")
    print ("1) Pythagoras")
    print ("2) Quadratic Equations")
    print ("3) Black Principle")
    choice = int(input(">>> ") or "0")
    if choice < 1 or choice > 3:
        print ("Make sure you choose the right number")
        return
    choices(choice)
main()