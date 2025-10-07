from logic import sendEmails

def main():
    print("Started Cron Job")
    sendEmails()
    print("sent all emails")

main()
