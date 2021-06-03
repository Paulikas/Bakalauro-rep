import os

from .settings import LOGS_PATH, LOG_ON


def log(func):
    '''
        Function decorator for logging
    '''
    def wrapper(*args, **kwargs):
        if LOG_ON:
            path = os.path.join(LOGS_PATH, "logs.txt")

            with open(path, "a") as f:
                message = ("Function name: "+func.__name__ + " Function parameter: " +
                           " ".join([str(arg) for arg in args])+"\n")

                f.write(message)
        result = func(*args, **kwargs)
        return result

    return wrapper


def log_message(message):
    if LOG_ON:
        path = os.path.join(LOGS_PATH, "logs.txt")

        with open(path, "a") as f:
            f.write(message + "\n")


def log_error(file_name: str, exception: Exception):
    path = os.path.join(LOGS_PATH, "Error_log.txt")

    with open(path, "a") as f:
        f.write("Error with file: "+file_name +
                " with exception:"+exception+"\n")
