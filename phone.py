# Define two functions, isValidHKPhoneNumber and hasValidHKPhoneNumber,
# that returns whether a given string is
# a valid HK phone number and contains a valid HK phone number
# respectively (i.e. true/false values).

def is_valid_HK_phone_number(number):
    if len(number) != 9:
        return False
    if number[4] != ' ':
        return False
    if not number[:4].isdigit() or not number[5:].isdigit():
        return False
    return True
def has_valid_HK_phone_number(string):
    # Search for valid HK phone number pattern within the string
    for i in range(len(string) - 8):
        number = string[i:i+9]
        if is_valid_HK_phone_number(number):
            return True
    return False

