import re


def password_evaluator(pwd):
    recommended_length = len(pwd) >= 12  # 12 or more characters in password
    alternating_caps = len([letter for letter in pwd if letter.isupper()]) >= 3  # 3 or more uppercase letters
    include_numbers = len([num for num in pwd if num.isdigit()]) >= 3  # 3 or more digits in password
    include_special_chars = len(re.findall(r"[^A-Za-z\d]", pwd)) >= 1  # 1 or more special symbols
    conditions = [recommended_length, alternating_caps, include_numbers, include_special_chars]

    if all(conditions):  # Checks that all conditions are True
        return True

    global issues

    issues = []
    if not recommended_length:
        message = "Password length is shorter than the recommended one."
        issues.append(message)
    if not alternating_caps:
        message = "Password does not contain 3 or more uppercase letters."
        issues.append(message)
    if not include_numbers:
        message = "Password does not contain 3 or more digits."
        issues.append(message)
    if not include_special_chars:
        message = "Password does not contain 1 or more special symbols."
        issues.append(message)
    return False


def password_advisor(pwd):
    if password_evaluator(pwd):
        return "Password is strong!"
    new_line = '\n'
    return f"Password is weak! It is highly recommended to strength your password.\nIssues:\n" \
           f"{new_line.join(str(issues.index(x) + 1) + '.' + x for x in issues)}"


password = input("Please enter a password for security evaluation:\n")
print(password_advisor(password))