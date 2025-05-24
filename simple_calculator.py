def calc():

    while True:
        try:
            x = float(input(">"))
            op = input(">").lower()
            y = float(input(">"))

        except ValueError:
            print("Invalid input. Please enter value only.")
            continue

        if op == "+":
            result = x + y
            print(result)
        elif op == "-":
            result = x - y
            print(result)
        elif op in ["x","*"]:
            result = x * y
            print(result)
        elif op == "/":
            if y == 0:
                print("Error:can't divide by zero.")
                continue
            result = x / y
            print(result)
        else:
            print("Invalid value.")

        next_calc = input("Do you want to continue? (y/n): ").lower()
        if next_calc in ["n","no"]:
            break

if __name__ == "__main__":
    calc()