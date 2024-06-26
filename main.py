import random
import win32com.client as win32

from selenium_sadness import ask_gpt

outlook = win32.Dispatch('outlook.application')

# email variable setup --
# the email it sends to and the body and subject options
recipient = 'bspatrick@wpi.edu' #'bspatrick@wpi.edu'

subjects = [
    'pretty please',
    'nominations',
    'reply',
    'Brooooooooke',
    'why do you do this to me',
]

bodies = [
    'What are the chances you even read these?https://docs.google.com/forms/d/e/1FAIpQLSehWmN_JIDX881XQxSNoRF-d6fVwwGMoI3I4uRhI2PkSuDPEw/viewform?usp=sf_link',
    'Brooke https://docs.google.com/forms/d/e/1FAIpQLSehWmN_JIDX881XQxSNoRF-d6fVwwGMoI3I4uRhI2PkSuDPEw/viewform?usp=sf_link'
    'https://docs.google.com/forms/d/e/1FAIpQLSehWmN_JIDX881XQxSNoRF-d6fVwwGMoI3I4uRhI2PkSuDPEw/viewform?usp=sf_link'
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


async def main():
    print("test")
    ask_gpt()