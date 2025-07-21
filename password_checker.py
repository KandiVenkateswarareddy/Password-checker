import re

# Take user input
password = input("Enter your password: ")

#  Define conditions using regex
def check_password_strength(password):
    # Initialize strength score
    score = 0
    feedback = []

    # Check length (at least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !@#$%^&*).")

    #  Provide feedback based on score
    if score == 5:
        return "Strong", feedback
    elif score >= 3:
        return "Medium", feedback
    else:
        return "Weak", feedback

# Check the password and print result
strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions:")
    for suggestion in feedback:
        print(f"- {suggestion}")