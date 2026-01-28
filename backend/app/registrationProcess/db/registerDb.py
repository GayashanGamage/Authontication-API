
def check_duplicate_email(email: str, db):
    """
    check provided email is already registered in the users collection
    
    :param email: provided email·
    :param db: database connection
    """
    # check the email on 'users' collection
    data = db.users.find_one({"email": email})
    # if exists, retunr True
    if data:
        return True
    # else return False
    else:
        return False
    
def insert_user(userData, db):
    # Insert the user data into the 'users' collection
    data = db.users.insert_one(userData.model_dump(mode='json'))
    # if successful, return the inserted_id
    if data.inserted_id:
        return data.inserted_id
    # else return None
    else:
        return None
    
def insert_otp(otpData, db):
    # Insert the OTP data into the 'otps' collection
    data = db.otp.insert_one(otpData.model_dump(mode='json'))
    # if successful, return the inserted_id
    if data.inserted_id:
        return data.inserted_id
    # else return None
    else:
        return None