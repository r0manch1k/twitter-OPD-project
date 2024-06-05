def generateResult(error: str = None, error_type: str = "no errors", data = None):
    result = dict()
    result["data"] = data
    if error_type == "no errors":
        result["errors"] = None
        return result

    result["errors"] = dict()
    if error_type == "connection":
        result["errors"][error_type] = error
    else:
        result["errors"]["connection"] = None
    if error_type == "format":
        result["errors"][error_type] = error
    else:
        result["errors"]["format"] = None
    return result
