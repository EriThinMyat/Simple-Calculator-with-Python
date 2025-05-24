def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error: can't divide by zero"
    return x / y

def format_number(n):
    if isinstance(n,float) and n.is_integer():
        return str(int(n))
    return str(n)

def calc():

    while True:

        x = input(">")
        if x.lower() in ["exit","quit"]:
            break

        op = input(">").strip().lower()
        if op in ["exit","quit"]:
            break

        y = input(">")
        if y.lower() in ["exit","quit"]:
            break

        try:
            x_display = float(x)
            y_display = float(y)

        except ValueError:
            print("Invalid input. Please enter valid value.")
            continue

        if op == "+":
            result = add(x_display,y_display)

        elif op == "-":
            result = subtract(x_display,y_display)

        elif op in ["x","*"]:
            result = multiply(x_display,y_display)

        elif op == "/":
            result = divide(x_display,y_display)

        else:
            print("Invalid operator")
            continue

        if isinstance(result,str):
            print(result)
        else:
            print(format_number(result))


if __name__ == "__main__":
    calc()