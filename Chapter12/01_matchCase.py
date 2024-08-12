def match_Case(status):
    match status:
        case 200: return "OK"
        case 404: return "Not found"
        case 500: return "Internal Server Error"
        case _: return "Unknown status"


print(match_Case(404)) # Output: Not Found
print(match_Case(200)) # Output: OK
print(match_Case(500)) # Output: Internal Server Error
print(match_Case(403)) # Output: Unknown status