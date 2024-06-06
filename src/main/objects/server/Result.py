def generateResult(error: str = None, error_type: str = "", data = None):
    result = dict()
    result["data"] = data
    if error_type == "":
        result["error"] = None
        return result

    result["error"] = dict()
    if error_type == "connection":
        result["error"][error_type] = error
    else:
        result["error"]["connection"] = None
    if error_type == "format":
        result["error"][error_type] = error
    else:
        result["error"]["format"] = None
    return result
