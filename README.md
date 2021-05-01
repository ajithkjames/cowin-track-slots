# cowin-track-slots
Tracking vaccine slots by pincode and send notifications through IFTTT.

## Requirements
Create a virtual env and install the requirements.

Run `pip install -r requirements.txt`

Create an IFTTT account and configure it to recieve notifications on your phone. Use this guide for the setup : [Configure IFTTT](https://betterprogramming.pub/how-to-send-push-notifications-to-your-phone-from-any-script-6b70e34748f6)

## How to run
Run `python3 cowin_slot.py <pincode> <IFTTT TOKEN>`
