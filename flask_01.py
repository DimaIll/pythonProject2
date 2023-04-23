@app.route("users/<uid>")
def profile(uid):
    print(uid)
    print(type(uid))
    return " "