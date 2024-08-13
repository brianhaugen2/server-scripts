"""
This script checks your public IP versus the IP saved in the log file (defined in config file).
Copy server-scripts/configs/template_pulbic_ip_update.json to server-scripts/configs/public_ip_update.json.
Update the config file (server-scripts/configs/public_ip_update.json) with needed information.

The log filepath is where we check what the previous IP address was to compare against the current IP address

Needed Information:
    - subject: subject for the email to be sent
    - to: gmail account email address to send email  
    - from: recipients of the sent email to notify of the IP change
    - secret: gmail app password/secret https://support.google.com/mail/answer/185833?hl=en
    - log_filepath: filepath to save a log file and keep history of the IP address

"""

import os
import json
import smtplib
import requests
from typing import List
from datetime import datetime
from email.mime.text import MIMEText


def get_public_ip():
    response = requests.get('https://api.ipify.org').text
    return response


def send_email(
    subject: str, 
    body: str, 
    sender: str, 
    recipients: List[str], 
    password: str,
):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Sent email on IP change")


if __name__ == "__main__":
    # read in config file
    config_fp = os.path.join(
        os.path.dirname(__file__), 
        "configs", 
        "public_ip_update.json"
    )
    with open(config_fp, "r") as f:
        config = json.load(f)


    # create log if doesn't exist
    if not os.path.exists(config["log_filepath"]):
        with open(config["log_filepath"], "w") as f:
            f.write("Start of log\n0.0.0.0\n")

    # grab the previous public IP from log file
    with open(config["log_filepath"], "r") as f:
        prev_public_ip = f.readlines()[-1][:-1]

    # log datetime
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print()
    print(date_time)

    # get current public IP
    public_ip = get_public_ip()

    # send email if IP address has changed
    if prev_public_ip != public_ip:
        body = f"Public IP changed from {prev_public_ip} to {public_ip}"
        print(body)
        send_email(
            config["subject"], 
            body, 
            config["from"], 
            config["to"], 
            config["secret"]
        )

    # finally append current IP to log to grab next time
    print(public_ip)

