def original_euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the 1st number (Greater than 2nd number): "))
num2 = int(input("Enter the 2nd number: "))

print(f"GCD of {num1} and {num2}:", original_euclidean_gcd(num1, num2))