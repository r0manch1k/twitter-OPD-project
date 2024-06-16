import re


def getValidString(string: str):
    new_string = string
    new_string = new_string.replace(chr(92), chr(92) + chr(92))
    new_string = new_string.replace(chr(39), chr(92) + chr(39))
    new_string = new_string.replace(chr(34), chr(92) + chr(34))
    return new_string


def validateEmail(email: str):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pattern, email):
        return ""
    return "Invalid email"

    
def validateUsername(username: str):
    if len(username) < 5 or len(username) > 32:
        return "Username must contain 5 - 32 symbols"
    
    for i in r"""-+={}"[]<>!#£%^&*()~`'?/|\:;""":
        if username.find(i) > 0:
            if i == " ":
                return "Username contain invalid symbol " + "(space)"
            else:
                return "Username contain invalid symbol " + i

    for i in username:
        if (i in [chr(j) for j in range(ord('a'), ord('z') + 1)]) or \
        (i in [chr(j) for j in range(ord('A'), ord('Z') + 1)]) or (i in [str(j) for j in range(10)]):
            pass
        else:
            return "Username must contain Latin letters"

    return ""

    
def validateName(name: str):
    if len(name) < 4 or len(name) > 15:
        return "Name must contain 4 - 15 symbols"

    return ""


def validatePassword(password: str):
    if len(password) < 8 or len(password) > 16:
        return "Password must contain 8 - 16 symbols"

    flag = False
    for i in [chr(j) for j in range(ord('a'), ord('z') + 1)]:
        if password.find(i) > 0:
            flag = True
            break
    if not flag:
        return "Password must contain lower letters"

    flag = False
    for i in [chr(j) for j in range(ord('A'), ord('Z') + 1)]:
        if password.find(i) > 0:
            flag = True
            break
    if not flag:
        return "Password must contain upper letters"

    flag = False
    for i in [str(j) for j in range(10)]:
        if password.find(i) >= 0:
            flag = True
            break
    if not flag:
        return "Password must contain digits"

    flag = False
    for i in "[_@$]":
        if password.find(i) > 0:
            flag = True
            break
    if not flag:
        return "Password must contain characters []_@$"

    for i in r"-+={}<>!#£%^&*()~` '?/|\:;":
        if password.find(i) > 0:
            return "Password contain invalid symbol " + i

    return ""

    
def validateInfo(info: str):
    if len(info) > 70:
        return "About must contain <= 70 symbols"
        
    return ""


def validateText(text: str):
    if len(text) > 100 or text == 0:
        return "Text must contain 1 - 100 symbols"
        
    return ""