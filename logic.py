import requests
from datetime import datetime
import random
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from template import getTemplate
import os


def getAllBlogs():
    try:
        response = requests.get("https://codeverse-chronicles.onrender.com/get-all-blogs?pageNumber=0&pageSize=100")
        blogs = response.json()
        return blogs        
    except Exception as e:
        print("Exception in fetching blogs")
        print(str(e))
        return []


def mapUserAndBlogs():
    try:
        articles = getAllBlogs()
        emails = [
            "ganapavarapuanusha@gmail.com",
            "ihere5053@gmail.com",
            "jayaaditya2003@gmail.com",
            "uma83857@gmail.com",
            "prudvinathch@gmail.com",
            "ravillaleelasai6642@gmail.com",
            "garabhargav@gmail.com",
            "sasidharreddyyennam@gmail.com",
            "venkatsatavahana@gmail.com",
            "suryareddy89143@gmail.com",
            "vpk9611@gmail.com",
            "debralloyd.51665@gmail.com"
            ]
        random.shuffle(articles)
        mapping = [{"email": e, "title": a["title"], "url": "https://codeverse-chronicles.vercel.app/blogPost/"+a["id"], 'imageURL':a['image'],'date':a['postedAt']}
           for e, a in zip(emails, articles)]
        return mapping
    except Exception as e:
        print("Exception on mapping user and blogs")
        print(str(e))
        return []

def sendEmails():
    try:

        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        SMTP_USERNAME = os.getenv("SMTP_USERNAME")
        SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
        from_addr = os.getenv("SMTP_USERNAME")
        subject='Latest Blog on Codeverse Chronicles'
        mappings = mapUserAndBlogs()
        
        for ma in mappings:
            current_datetime = datetime.now()
            try:
                content = getTemplate(blogURL=ma['url'],blogImgURL=ma['imageURL'],blogTitle=ma['title'],date=ma['date'])
                msg = MIMEMultipart("alternative")
                msg["From"] = from_addr
                msg["To"] = ma['email']
                msg["Subject"] = subject
                msg.attach(MIMEText(content, "html"))
                server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()  # Secure connection
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.sendmail(from_addr, ma['email'], msg.as_string())
                server.quit()
                print(str(current_datetime)+" ✅ Email sent successfully! to "+ma['email'])
            
            except Exception as e:
                print("Exception while sending email to "+ma['email'])
                print(str(e))
        return True
    except Exception as e:
        print("Exception on sendingEmails")
        print(str(e))
        return False
