def message_valid (message):
    if len(message) < 1 or len(message) > 99:
        return False
    else:
        return True
