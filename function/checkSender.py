
def checkSenders(request, token):
    headerToken = request.headers.get('x-gitlab-token')
    if (headerToken == None):
        raise Exception("The header doesn't contain the token key")
    if (headerToken != token):
        raise Exception("Incorrect|Invalid token")

    

