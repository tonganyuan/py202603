def createUser(name,age,**user):
    user["username"] = name
    user['age'] = age
    return user