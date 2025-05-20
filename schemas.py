from pydantic import BaseModel

class MessageBase(BaseModel):
    sender: str
    receiver: str
    content: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int

    class Config:
        orm_mode = True
