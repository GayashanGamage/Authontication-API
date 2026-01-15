from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def helth_check():
    return JSONResponse(status_code=200, content={"message": "Service is up and running!"})