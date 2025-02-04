
def parseUrl(url: str):
    parsedURL= {}

    # protocol: http/s, ftp -> ://
    # username:password     -> @
    # hostname: site.com    -> site.com
    # port 90               -> :80
    # path test.com/user    -> /user
    # query ?userId=12      -> ?...&...
    # hash                  -> #list

    # print(url)
    # extract protocol
    splitUrl = url.split("://", 1)
    if len(splitUrl) > 1:
        parsedURL["protocol"] = splitUrl[0]
        url = splitUrl[1]

    # print(url)
    # extract username and password
    splitUrl = url.split("@", 1)
    if len(splitUrl) > 1:
        parsedURL["credentials"] = {"username" : splitUrl[0].split(":")[0], "password" : splitUrl[0].split(":")[1]}
        url = splitUrl[1]

    # print(url)
    # extract host
    splitUrl = url.split(":", 1)
    if len(splitUrl) > 1:
        parsedURL["host"] = splitUrl[0]
        url = splitUrl[1]

    # print(url)
    # extract port
    splitUrl = url.split("/", 1)
    if len(splitUrl) > 1:
        parsedURL["port"] = splitUrl[0]
        url = splitUrl[1]

    # print(url)
    # extract Path
    splitUrl = url.split("?", 1)
    if len(splitUrl) > 1:
        parsedURL["path"] = splitUrl[0]
        url = splitUrl[1]

    # print(url)
    # extract Query
    splitUrl = url.split("#", 1)
    if len(splitUrl) > 1:
        parsedURL["query"] = splitUrl[0]
        url = splitUrl[1]

    print(url)
    # extract hash
    # splitUrl = url.split("#", 1)
    # if len(splitUrl) > 1:
    #     parsedURL["query"] = splitUrl[0]
    #     url = splitUrl[1]

    print(parsedURL)



if __name__ == "__main__":
    parseUrl("https://google.com")
    # parseUrl("https://google.com/users")
    #parseUrl("ftp://testUser:testPassword@google.com:21/users?userId=1234&location=Texas#ListsOfCities")