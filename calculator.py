def main():
    
    def calculate(a, b, operation):
        if operation == '+':
            return a +b
        elif operation == '-':
            return a -b
        elif operation == '*':
            return a * b
        elif operation == '/':
            if b !=0:
                return a / b
            else:
                return "Error:  zero is not allowed ."
        else:
            return "Error: Invalid operation enter valid operation."

    
    print("Welcome to the sai's calculator!")

    try:
        a = float(input("Enter the first number: "))
        b= float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return


   

    operation = input("Enter the operation: ").strip()

    
    result = calculate(a, b, operation)
    print("The result is:", result)

if __name__ == "__main__":
    main()

