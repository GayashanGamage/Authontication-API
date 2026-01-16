from fastapi import FastAPI
from fastapi.responses import JSONResponse
from global_service.db import get_database
from signin.endpoints import router as signin_router
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI instance
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    'https://jwt-authontication.netlify.app/',
    'http://jwt-authontication.netlify.app/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Initialize the database connection
get_database() 


@app.get("/")
async def helth():
    return JSONResponse(status_code=200, content={"message": "Service is up and running!"})

# Include signin router
app.include_router(signin_router)