import art
print(art.logo)
print("\n"*3)
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operation = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

def calculator():
    first_number = float(input("What's the first number? "))
    continue_or_no = True
    while continue_or_no:
        for symbol in operation:
            print(symbol)
        choose_operation = input("Pick an operation: ")
        second_number = float(input("What's the second number? "))
        fin_num = operation[choose_operation](first_number, second_number)
        print(f"{first_number}{choose_operation}{second_number} = {fin_num}")
        recalculation = input(
            f"Type 'y' to continue calculating with {fin_num}, or type 'n' to start a new calculation: ")
        if recalculation == "y":
            first_number = fin_num
        else:
            continue_or_no = False
            print("\n" * 10)
            calculator()
calculator()
