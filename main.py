from fastapi import FastAPI
from typing import List
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/ping")
def ping():
    return "pong"
class car(BaseModel):
    id : str
    brand: str
    model: str
    characteristic: List[max_spid: int, max_fuel_capacity: int]
automobil: List[car] = []
@app.post("/cars")
def cars():
    return JSONResponse(content= {car}, status_code=201 )
    




@app.get("/cars")
def get_cars():
    return {"cars": [car.dict() for car in automobil]}


@app.get("/cars/{id}")
def update_task(id: int):
    if 0 <= id < len(automobil):
        automobil[id] = car
        return {"cars": [t.dict() for t in automobil]}
    return JSONResponse(content={"error": "Car non trouvée"}, status_code=404)


@app.put("/cars/{id}")
def update_task(id: int):
    if 0 <= id < len(automobil):
        automobil[id] = car
        return {"cars": [t.dict() for t in automobil]}
