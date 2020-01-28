def validate_pin(pin):
    if len(pin) == 6 or len(pin) == 4:
        if pin.isdigit() == False:
            return False
        return True
    else:
        return False

#print(validate_pin(input()))
