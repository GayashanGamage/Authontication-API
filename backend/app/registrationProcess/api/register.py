from fastapi import APIRouter, Request, Depends, HTTPException
from .schema import SignInSchema
from  .service import signinService
from ..dependencies.db import get_database
from ..dependencies.email import get_brevo_client as brevo_client

router = APIRouter(prefix='/signin', tags=['signin'])

def checkIp(request : Request):
    if request.client.host == '127.0.0.1':
        raise HTTPException(status_code=403, detail="Forbidden")

@router.post("/signin")
async def signin(data : SignInSchema, db = Depends(get_database), brevo_client = Depends(brevo_client)):
    return signinService(data, db, brevo_client)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# from user_agents import parse
# user_agent = data.headers.get('user-agent', '')
# print(user_agent.split(' ')[0])
# ua = parse(user_agent)
# print(ua.os.family)
# print(data.client.host)
