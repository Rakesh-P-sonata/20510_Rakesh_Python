def validateUP(u, p):
    if check_string(u) and check_string(p):
        if check_pass(p):
            return True
        else:
            return False
    return False


def check_string(x):
    if type(x) == str:
        return True
    else:
        return False


def check_pass(y):
    special = ['$', '@', '#', '%']
    val = True

    if len(y) < 8:
        val = False

    if not any(char.isdigit() for char in y):
        val = False

    if not any(char.isupper() for char in y):
        val = False

    if not any(char in special for char in y):
        val = False

    return val
