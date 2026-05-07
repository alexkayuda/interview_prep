def http_error(status : int) -> str:
    match status:
        case 200:
            return "All is good!"
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Unauthorized"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        

if __name__ == "__main__":
    print(http_error(200))