def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

x = int(input("Enter Grade: "))
print(f"Your grade is : {get_grade(x)}")



'''def is_even(num):
    return num % 2 == 0

x = int(input("Enter a number: "))
print(f"{x} is even: {is_even(x)}")'''