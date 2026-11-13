
# Signup Validator - Project Plan

## 1. Project Goal
Build a Python signup validation program that checks whether
user information meets specific requirements.

The program returns True if every value is valid and False
if at least one value is invalid.

## 2. Project Structure

- validation.py: Contains individual validation functions
  and the main sign_up function.
- main.py: Collects user input and displays the result.
- test_validation.py: Contains pytest tests.
- AGENTS.md: Contains instructions for AI assistants.
- PLAN.md: Contains the project plan.

## 3. Validation Functions

- is_valid_username(): Checks username length and characters.
- is_valid_email(): Checks the email format requirements.
- is_valid_password(): Checks password length, letters and numbers.
- is_valid_age(): Checks integer type and age range.
- is_valid_terms(): Checks whether terms were accepted.
- sign_up(): Combines all five validation functions.

## 4. Testing Strategy

Use pytest to test:
- Valid and invalid information.
- Minimum and maximum boundaries.
- Incorrect data types.
- Edge cases for every validation function.

## 5. Development Process

1. Create the project repository.
2. Set up project instructions.
3. Finalize the project plan.
4. Build validation.py.
5. Build main.py.
6. Write pytest tests.
7. Run tests and fix errors.
8. Commit changes and push to GitHub.
9. Prepare for the code defense.

## 6. Learning Goal

Understand every function, condition, and line of code
well enough to explain the entire project during the
10-minute code defense.
