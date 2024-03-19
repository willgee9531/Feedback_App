import smtplib
from email.mime.text import MIMEText

def send_mail(school, category, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '1537abc29690b5'
    password = '38f277c19ea820'
    message = f'''<h3>New Feedback Submission</h3>
    <ul><li>Name of school: {school}</li>
    <li>Category: {category}</li>
    <li>Rating: {rating}</li>
    <li>Comments: {comments}</li>
    </ul'''

    sender_email = 'willgee9531@gmail.com'
    receiver_email = 'will_gee85@yahoo.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'FingerNotes Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send mail
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

    