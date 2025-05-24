def add(x,y):            #addition
    return x + y

def subtract(x,y):      #subtraction
    return x - y

def multiply(x,y):      #multiplication
    return x * y

def divide(x,y):        #division
    if y == 0:
        return "Error: can't divide by zero."
    return x / y

def format_number(n):
    if isinstance(n,float) and n.is_integer():
        return str(int(n))
    return str(n)

def display_result(x_val,op,y_val,result):
    formatted_result = format_number(result)
    expression = f"{format_number(x_val)} {op} {format_number(y_val)} = {formatted_result}"
    print(formatted_result)
    return expression


def calc():

    operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "x" : multiply,
        "/" : divide
    }

    history = []
    last_result = None
    quit_command = ["exit","quit"]
    help_command = (
        "history -> to view calculation history\n"
        "clear -> to clear calculation history\n"
        "quit/exit -> to exit program"
    )

    while True:

        user_input = input("> ").strip().lower()

        if user_input in quit_command:
            break

        elif user_input == "help":
            print(help_command)
            continue

        elif user_input == "history":
            if not history:
                print("No history yet.")
            else:
                print("History")
                for record in history:
                    print(record)
            continue

        elif user_input == "clear":
            if not history:
                print("No history here.")
            else:
                history.clear()
                print("History cleared.")
            continue

        tokens = user_input.split()
        if len(tokens) != 3:
            print("Invalid input. Please enter valid input.")
            continue

        x,op,y = tokens

        try:
            x_val = last_result if x == "ans" else float(x)
            y_val = last_result if y == "ans" else float(y)

        except ValueError:
            print("Invalid value. Please enter valid value.")
            continue


        if op in operations:
            result = operations[op](x_val,y_val)
        
        else:
            print("Invalid opertor")
            continue

        if isinstance(result,str) and result.startswith("Error"):
            print(result)
            continue

        else:
            last_result = result
            expression = display_result(x_val,op,y_val,result)
            history.append(expression)


if __name__ == "__main__":
    calc()