from pydantic import BaseModel, StrictStr, StrictInt


class OneMemeModel(BaseModel):
    id: StrictInt
    info: dict
    tags: list
    text: StrictStr
    updated_by: StrictStr
    url: StrictStr


class AllMemeModel(BaseModel):
    data: list[OneMemeModel]
