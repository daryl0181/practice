def main():
    while True:
        user_input = input("Enter two number: ")
        if user_input.isdigit():
            print("Please enter two numbers separated by space.")
            continue
        elif len(user_input.split()) != 2:
            print("Please enter exactly two numbers.")
            continue
        print("Choose an option:")
        print("1 add")

        while True:
            choice = input("Enter your choice:  ")
            numbers = list(map(float, user_input.split()))
            if choice == "1":
                print(f"Result: {numbers[0] + numbers[1]}")
            else:
                print("Invalid choice")
                break
                
if __name__ == "__main__":
    main()