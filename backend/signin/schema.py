from pydantic import BaseModel

class SignInSchema(BaseModel):
    firstName : str
    lastName : str
    email : str