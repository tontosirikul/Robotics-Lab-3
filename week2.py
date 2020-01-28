def validate_pin(pin):
    if len(pin) == 6 or len(pin) == 4:
        for letter in pin:
            if letter.isdigit() == False:
                return False
        return True
    else:
        return False




print(validate_pin(input("")))