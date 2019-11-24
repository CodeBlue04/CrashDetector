import smtplib

import flask
from flask_mail import Mail, Message

""" 

Many thanks to Mike Richards for helping to write and test this code! 

"""

app = flask.Flask("CrashDetectorServer")
mail = Mail(app)

# ------------------------------
# - receive data from Core:
imei = 300434063189070

@app.route('/', methods=['POST'])
def parse_request():
    if True:
        imei_test = flask.request.form['imei']
        momsn = flask.request.form['momsn']
        transmit_time = flask.request.form['transmit_time']
        iridium_latitude = flask.request.form['iridium_latitude']
        iridium_longitude = flask.request.form['iridium_longitude']
        iridium_cep = flask.request.form['iridium_cep']
        data = flask.request.form['data']
        flask.make_response("200")
        parseData([data, iridium_latitude, iridium_longitude, iridium_cep, transmit_time])
    return "Your RockBlock's IMEI number"


# -----------------------------
# - Mail stuff
EMAIL_ADDRESS = "email@domain.com"
EMAIL_PASSWORD = "Password"

mail_settings = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 465,
    'MAIL_USE_TLS': False,
    'MAIL_USE_SSL': True,
    'MAIL_USERNAME': "email@domain.com",
    'MAIL_PASSWORD': "Password",
}
app.config.update(mail_settings)


def parseData(dataArray):
    message = bytes.fromhex(dataArray[0])  # in hex, need to switch to ascii
    irLat = dataArray[1]
    irLon = dataArray[2]
    irCEP = dataArray[3]
    time = dataArray[4]
    # xG, yG, zG, gyroXangle, gyroYangle, gyroZangle, temperature, lat, long, time, speed, SOS = message.split(',')
    #
    # if (SOS == True):
    #     output = "SOS! " + time + " Latitude: " + str(lat) + " Longitude: " + str(long) + ". Please send help!"
    # elif (abs(xG) > 1 or abs(yG) > 1.5 or abs(zG) > 3 or abs(gyroXangle) > 181 or abs(gyroYangle) > 181 or
    #       abs(gyroZangle) > 181) and float(temperature) > 70:
    #     output = "AutoMsg: Crash with fire! Time: " + time + " gX: " + "%.1f" % xG + " gY: " + \
    #              "%.1f" % yG + " gZ: " + "%.1f" % zG + " Lat: " + str(lat) + \
    #              " Lon: " + str(long) + " Speed: " + str(speed)
    # elif (abs(xG) > 1 or abs(yG) > 1.5 or abs(zG) > 3 or abs(gyroXangle) > 181 or abs(gyroYangle) > 181 or
    #       abs(gyroZangle) > 181 and float(temperature) < 70):
    #     output = "AutoMsg: Crash! Time: " + time + " gX: " + "%.1f" % xG + " gY: " + \
    #              "%.1f" % yG + " gZ: " + "%.1f" % zG + " Lat: " + str(lat) + \
    #              " Lon: " + str(long) + " Speed: " + str(speed) + " Temp: " + str(temperature)
    # elif float(temperature) > 70:
    #     output = "AutoMsg: Fire! Time: " + +  time + " Lat: " + str(lat) + " Lon: " + str(long)
    output = "Success!"
    sendMessage("email@domain.com", output)


def sendMessage(address, message):
    contactList = ["email address or SMS contact info"]
    with Emailer() as emailer:
        for recipient in contactList:
            emailer.send_email("email@domain.com", recipient, "Subject", message)
    return


class Emailer:
    "Sends emails. Use via 'with' statement"
    def send_email(self, from_, to, subject, body):
        email_text = f"""\
        From: {from_}
        To: {to}
        Subject: {subject}

        {body}
        """
        self.server.sendmail(from_, to, email_text)

    def __enter__(self):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.server.ehlo()
        self.server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.server.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80")
