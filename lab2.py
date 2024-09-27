def main():
    while True:
        try:
            fahrenheit = int(input("Enter temperature in F: "))
            celsius = (fahrenheit - 32) * 5.0 / 9.0
            celsius = round(celsius, 1)
            print(f"Temperature in C: {celsius}")
            proceed = input("Want to proceed? y/n: ").strip().lower()
            if proceed != 'y':
                break
        except ValueError:
            print("Please enter a valid integer for temperature.")
if __name__ == "__main__":
    main()