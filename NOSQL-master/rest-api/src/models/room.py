from pydantic import BaseModel


class Room(BaseModel):
    id: str
    name: str
    host_name: str
    neighbourhood: str
    latitude: float
    longtude: float
    room_type: str
    price: int
    minimum_nights: int


class RoomUpdate(BaseModel):
    name: str
    host_name: str
    neighbourhood: str
    latitude: float
    longtude: float
    room_type: str
    price: int
    minimum_nights: int
