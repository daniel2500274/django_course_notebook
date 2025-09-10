age = 25
licensed = False

if age >= 18 and licensed:
    print("You are eligible to drive.")
elif age < 18:
    print("You are not eligible to drive.")
else:
    print("You need a driving license to drive.")

is_student = False
membership = True

if is_student or membership:
    print("You are eligible for a discount.")
else:
    print("No discounts available.")

is_admin = False

if not is_admin:
    print("Access denied. its only for admins.")
else:
    print("Access successfully")