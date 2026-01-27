from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime, timedelta
from uuid import UUID
from random import randint

class SignInSchema(BaseModel):
    firstName : Optional[str] = Field(default=None, max_length=50)
    lastName : Optional[str] = Field(default=None, max_length=50)
    email : EmailStr
    password : str
    changePassword : bool = Field(default=False)
    creatdAt : Optional[None] = Field(default=datetime.utcnow)
    updatedAt : None
    verified : bool = Field(default=False)
    vefifiedAt : Optional[None] = None 
    revoked : bool = Field(default=False)

    @field_validator('password')
    def validate_email(cls, v):
        """
        validate the password length
        
        :param cls: base model
        :param v: password value
        """
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        else:
            return v
        
class OTP(BaseModel):
    userId : UUID
    creatdAt : Optional[None] = Field(default=datetime.utcnow)
    verified : bool = Field(default=False)
    attempt : int = Field(default=0)
    expireAt : datetime[None] = Field(default_factory=lambda: datetime.utcnow() + timedelta(minutes=10))
    status : bool = Field(default=False)
    code : int[None] = Field(default_factory=lambda: randint(100000, 999999))
    purpose : str = Field(default="email_verification")