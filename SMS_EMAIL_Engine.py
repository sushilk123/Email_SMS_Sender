#!/usr/bin/env python
# coding: utf-8

# In[3]:


def SendEmail(TO,FROM,PASSWORD,SUBJECT,MESSAGE):
    import smtplib,ssl  #Python’s built-in module for sending emails to any Internet machine with an SMTP or ESMTP listener daemon.
    import os
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    context = ssl.create_default_context() # Create a secure SSL context
    
    # Try to log in to server and send email
    try:
        smtpserver.ehlo()  # (Extended Hello)=>  tells the server that the client want to use the Extended SMTP (ESMTP) protocol.
        smtpserver.starttls(context=context) #(Start Transport Layer Security)
        smtpserver.ehlo
        smtpserver.login(FROM, PASSWORD)
        header = 'To: ' + TO + '\n' + 'From: ' + FROM + '\n' + 'Subject: ' + SUBJECT + '\n'

        text = f'''
        {MESSAGE}
        
        Regards,
        Sushil
        www.sushilkhairnar.com
        '''
        MESSAGE = header + text
        smtpserver.sendmail(FROM, TO, MESSAGE)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    return ('Email sent Successfully!')
    smtpserver.close()


# In[5]:


def SendSMS(phone_number,MESSAGE):
    import requests
    import os
    url = "https://www.fast2sms.com/dev/bulk"
    authorization_key = os.environ['FAST2SMS_API_AUTHORIZATION_KEY']
    sender_id='SMSINI'
    message = f'''
        {MESSAGE}
        
        Regards,
        Sushil
        www.sushilkhairnar.com
        '''
    payload = f"sender_id={sender_id}&message={message}&language=english&route=p&numbers={phone_number}"
    headers = {
    'authorization': authorization_key,
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return (response.text)


# In[ ]:




