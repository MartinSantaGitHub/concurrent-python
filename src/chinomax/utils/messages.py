def get_header_text(name: str):
    message = f'''
    Supermarket: {name}
    ----------------------------------------------
    NOTE: The time is measured in seconds
    ----------------------------------------------
    '''

    return message


def show_canceled_exception_message():
    message = f'''
    ******************************
    The operation has been canceled
    ******************************
    '''

    return message


def show_unexpected_error_message():
    message = f'''
    ******************************
    An unexpected error has occurred
    ******************************
    '''

    return message
