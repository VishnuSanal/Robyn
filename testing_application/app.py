from typing import Optional

from robyn import Robyn, Request
from robyn.types import RequestBody, QueryParam

app = Robyn(__file__)


class CreateItemBody(RequestBody):
    name: Optional[str]
    description: str
    price: float
    tax: float


class CreateItemQueryParams(QueryParam):
    _id: int
    desc: Optional[str]


@app.post("/upload/file")
def create_item(request: Request, body_item: CreateItemBody, query: CreateItemQueryParams):
    return request.__repr__()


app.start()
