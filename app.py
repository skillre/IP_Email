from flask import Flask, request
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/send-ip', methods=['POST'])
def send_ip_via_email():
    # 获取POST请求中的参数
    recipient = request.form.get('recipient')
    smtp_server = request.form.get('smtp_server')
    port = request.form.get('port', 587)
    username = request.form.get('username')
    password = request.form.get('password')
    
    # 获取公网IP
    ip_response = requests.get("https://api.ipify.org")
    ip = ip_response.text
    
    # 构造邮件
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = 'Your Current Public IP Address'
    body = f'Your current public IP address is: {ip}'
    msg.attach(MIMEText(body, 'plain'))

    # 发送邮件
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(username, password)
    text = msg.as_string()
    server.sendmail(username, recipient, text)
    server.quit()

    return {'status': 'success', 'message': 'Email sent'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

