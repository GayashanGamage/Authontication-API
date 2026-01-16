from fastapi import APIRouter, Request, Depends, HTTPException
from . import db
from fastapi.responses import JSONResponse
from .schema import SignInSchema
from user_agents import parse

router = APIRouter(prefix='/signin', tags=['signin'])

def checkIp(request : Request):
    if request.client.host == '127.0.0.1':
        raise HTTPException(status_code=403, detail="Forbidden")

@router.post("/signin")
async def signin(checkIp = Depends(checkIp)):
    return JSONResponse(status_code=200, content={"message": "Signin endpoint reached"})
    # user_agent = data.headers.get('user-agent', '')
    # print(user_agent.split(' ')[0])
    # ua = parse(user_agent)
    # print(ua.os.family)
    # print(data.client.host)
