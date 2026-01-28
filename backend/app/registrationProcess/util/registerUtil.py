from fastapi import HTTPException, status

def send_email(firstName, email, code, email_client):
    # SendSmtpEmail | Values to send a transactional email
    send_smtp_email = email_client.SendSmtpEmail() 

    email_params = {
        "sender": {"name": "Auth Service", "email": "gayashan.randimagamage@gmail.com"},
        "to": [{"email": email, "name": firstName}],
        "subject": "Email Verification",
        'text_content' : f"Hello {firstName},\n\nYour verification code is: {code}\n\nThank you!",
    }

    try:
        # Send a transactional email
        api_response = email_client.send_transac_email(send_smtp_email)
        return True
    except Exception as e:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail=f"Error occurred while sending email: {str(e)}")