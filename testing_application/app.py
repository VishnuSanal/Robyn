# from robyn import Robyn
#
# app = Robyn(__file__)
#
#
# @app.get("/")
# async def h(request):
#     return "Hello, world!"
#
#
# app.start(port=8080)


from robyn import Robyn

app = Robyn(__file__)


@app.before_request("/")
def b(r):
    return r


@app.extra("/", method="PURGE")
def hello():
    return "goodbye"


if __name__ == "__main__":
    app.start(port=8081)
