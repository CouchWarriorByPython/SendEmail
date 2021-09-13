import smtplib
from email.mime.text import MIMEText


def send_email(message):
    sender = 'Your email'
    password = 'Your pass'
    with open('Path your file with email address', 'r') as f:
        emails = []
        for line in f.readlines():
            emails.append(line)
        f.close()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'Title your message'
        server.sendmail(sender, emails, msg.as_string())

        return 'The message was sent successfully!'
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    message = input('Type your message: ')
    print(send_email(message))


if __name__ == '__main__':
    main()


