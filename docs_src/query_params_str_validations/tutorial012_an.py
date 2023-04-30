from typing import List

from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[List[str], Query()] = ["foo", "bar"]):
    return {"q": q}
