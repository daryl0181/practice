print(" This is for practice purpose ")
print("------------------------------")
print("------------------------------")


def vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for c in text if c in vowels)
    consonant_count = sum(1 for c in text if c.isalpha() and c not in vowels)
    return vowel_count, consonant_count

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def main():
    while True:
        user_input = input("Enter something: ")
        print("Choose an option:")
        print("1 count vowels and consonants")
        print("2 if palindrome")
        print("3 exit")

        while True:
            choice = input("Enter your choice:  ")
            if choice == "1":
                v, c = vowels_consonants(user_input)
                print(f"Vowels: {v}, Consonants: {c}")
            elif choice == "2":
                print("Palindrome!" if is_palindrome(user_input) else "Not a palindrome.")
            elif choice == "3":
                print(f"Uppercase: {user_input.upper()}")
            elif choice == "4":
                print(f"Lowercase: {user_input.lower()}")
            elif choice == "5":
                print(f"Reverse ; {user_input[::-1]}")
            elif choice == "6":
                print(f"Word Count: {len(user.input.split())}")
            elif choice == "7":
                break
            elif choice == "0":
                print("Goodbye!")
                return
            else:
                print("Invalid chocice")

if __name__ == "__main__":
    main()