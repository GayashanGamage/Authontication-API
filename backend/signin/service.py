from .db import check_duplicate_email, insert_user, insert_otp
from fastapi import HTTPException, status
from .email import send_email
from .schema import OTP
from fastapi.responses import JSONResponse

def signinService(userData, db, email_client):
    # check the email is already registered
    data = check_duplicate_email(userData.email, db)
    if data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email is already registered")
    # else insert into the database
    insert_data = insert_user(userData, db)
    if insert_data is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Error occurred while registering the user")
    # generate a random OTP
    otp_data = OTP(
        userId=insert_data['id']
    )
    
    # send verification to the email and save in to db
    send_mail = send_email(insert_data['firstName'], insert_data['email'], otp_data['code'], email_client)
    
    # store send vefification mail status in to db
    insert_opt_data = insert_otp(otp_data, db)
    if insert_opt_data is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Error occurred while generating OTP")
    
    # return success response
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content={"message": "User registered successfully. Please verify your email."})