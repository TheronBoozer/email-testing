import random
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

# email variable setup --
# the email it sends to and the body and subject options
recipient = 'wtboozer@wpi.edu' #'bspatrick@wpi.edu'

subjects = [
    'pretty please',
    'nominations',
    'reply',
    'Brooooooooke',
    'why do you do this to me',
]

bodies = [
    'What are the chances you even read these?',
    'Brooke '
]

async def random_email():
    subject = subjects[int(random.random()*len(subjects))]
    body = bodies[int(random.random()*len(bodies))]

    await email(recipient, subject, body)
    
    
async def email(recipient, subject, body):
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.Body = body
    # mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

    # To attach a file to the email (optional):
    # attachment  = "Path to the attachment"
    # mail.Attachments.Add(attachment)

    mail.Send()