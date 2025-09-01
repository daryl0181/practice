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
        print("2 subtract")
        print("3 exit")
        print("4 multiply")
        print("5 divide")
        print("6 modulus")
        print("7 new input")
        print("0 quit")

        while True:
            choice = input("Enter your choice:  ")
            if choice == "1":
                numbers = list(map(float, user_input.split()))
                if len(numbers) == 2:
                    print(f"Result: {numbers[0] + numbers[1]}")
                else:
                    print("Please enter exactly two numbers.")
            elif choice == "2":
                numbers = list(map(float, user_input.split()))
                if len(numbers) == 2:
                    print(f"Result: {numbers[0] - numbers[1]}")
                else:
                    print("Please enter exactly two numbers.")
            elif choice == "3":
                print(f"Result: {numbers[0] * numbers[1]}")
            elif choice == "4":
                print(f"Result: {numbers[0] / numbers[1]}")
            elif choice == "5":
                print(f"Result: {numbers[0] % numbers[1]}")
            elif choice == "6":
                break
            elif choice == "7":
                user_input = input("Enter two number: ")
            elif choice == "0":
                print("Goodbye!")
                return
            else:
                print("Invalid chocice")


if __name__ == "__main__":
    main()
