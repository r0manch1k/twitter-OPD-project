import re
    

def validateEmail(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pat, email):
        return ""
    return "Invalid email"

    
def validateUsername(username):
    if len(username) < 5 or len(username) > 32:
        return "Username must be between 5 and 32 characters long"
        
    for i in r"""-+={}""[]<>!#£%^&*()~`'?/|\:;""":
        if username.find(i) > 0:
            if i == " ":
                return "Username contains an invalid character -> " + "(space)"
            else:
                return "Username contains an invalid character -> " + i
        
    for i in username:
        if (i in [chr(j) for j in range(ord('a'), ord('z') + 1)]) or \
        (i in [chr(j) for j in range(ord('A'), ord('Z') + 1)]):
            pass
        else:
            return "Username must contain only Latin letters"

    return ""

    
def validateName(name):
    if len(name) < 4 or len(name) > 15:
        return "Name must be between 5 and 32 characters long"
        
    for i in r"""-+={}""[]<>!#£%^&*()~`'?/|\:;""":
        if name.find(i) > 0:
            return "Name contains an invalid character -> " + i

    return ""


def validatePassword(password):
    if len(password) < 8 or len(password) > 16:
        return "Password must be between 8 and 16 characters long"

    flag = False
    for i in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
        if password.find(i) > 0:
            flag = True
            break
    if not flag:
        return "Password must contain Latin lowercase letters"

    flag = False
    for i in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:
        if password.find(i) > 0:
            flag = True
            break
    if not flag:
        return "Password must contain Latin uppercase letters"

    flag = False
    for i in [str(i) for i in range(0, 10)]:
        if password.find(i) > 0:
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
        return "Password must contain special characters -> []_@$"

    for i in r"-+={}<>!#£%^&*()~` '?/|\:;":
        if password.find(i) > 0:
            return "Password contains an invalid character -> " + i

    return ""

    
def validateInfo(info):
    if len(info) > 50:
        return "Info must be less than 50 characters long"
        
    for i in r"""'""'""":
        if info.find(i) > 0:
            return "Info contains an invalid character -> " + i
        
    return ""


def validateText(text):
    if len(text) > 100 or text == 0:
        return "Text must be between 1 and 100 characters long"
        
    for i in r"""'""'""":
        if text.find(i) > 0:
            return "Text contains an invalid character -> " + i
        
    return ""