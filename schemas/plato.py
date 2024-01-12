from typing import Optional
from pydantic import BaseModel

class Plato(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    tipo: str
