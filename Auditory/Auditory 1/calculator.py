#Напишете функција која ќе ги содржи функционалностите на едноставен аритметички калкулатор.

operators = ["+", "-", "*", "/", "%"]

def calculator(a, b, operator):
    if operator not in operators:
        return "Invalid operator"

    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b
    if operator == "%":
        return a % b

if __name__ == "__main__":
    a = float(input("Enter first number:"))
    operator = input("Enter an operator: ")
    b = float(input("Enter second:"))
    print(calculator(a, b, operator))
