import os

# Always create History.txt in the same folder as this script
HISTORY_FILE = os.path.join(os.path.dirname(__file__), "History.txt")

def show_history():
    with open(HISTORY_FILE, 'r') as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("No History Found!")
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    open(HISTORY_FILE, 'w').close()
    print("History Cleared.")

def save_to_history(Equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(Equation + " = " + str(result) + "\n")

def calculate(user_input):
    try:
        # Only allow numbers and math operators
        allowed_chars = "0123456789+-*/(). "
        if not all(c in allowed_chars for c in user_input):
            print("Invalid characters in expression!")
            return

        # Evaluate the expression
        result = eval(user_input)

        # If result is whole number, display as int
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        print("Result:", result)
        save_to_history(user_input, result)

    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print("Invalid expression:", e)

def main():
    print('----- SIMPLE CALCULATOR (type history, clear, or exit) -----')
    while True:
        user_input = input("Enter expression or command (history, clear, exit): ")
        if user_input == 'exit':
            print("GoodBye!")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

#if __name__ == "__main__":
main()
