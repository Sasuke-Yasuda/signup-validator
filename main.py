from validation import sign_up

username = input("Enter username: ")
email = input("Enter email: ")
password = input("Enter password: ")
age = input("Enter age: ")
accepted_terms = input("Accept terms? (yes/no): ")

try:
    age = int(age)
except ValueError:
    print("Age must be a whole number.")
else:
    accepted_terms = accepted_terms.lower() == "yes"

    result = sign_up(username, email, password, age, accepted_terms)

    print("Signup information valid:", result)