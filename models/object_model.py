from pydantic import BaseModel


class ResponseModel(BaseModel):
    id: int
    info: dict
    tags: list
    text: str
    updated_by: str
    url: str


class GetAllResponseModel(BaseModel):
    data: list[ResponseModel]
