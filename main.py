import sys
import twitter
from datetime import datetime, timezone
import schedule
import time
import json
import os

def job():
    message = 'I am live in Heroku and I am suppose to tweet every hour! ' + datetime.utcnow().strftime("%a, %b, %D - %T")
    api = twitter.Api(consumer_key= os.environ['c_key'],
                      consumer_secret=os.environ['c_sec'],
                      access_token_key=os.environ['a_key'],
                      access_token_secret=os.environ['a_sec'],)
    try:
        status = api.PostUpdate(message)
    except UnicodeDecodeError:
        print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
        print("Try explicitly specifying the encoding with the --encoding flag")
        sys.exit(2)
    print("%s just posted: %s" % (status.user.name, status.text))


def main():
    schedule.every(1).hour.do(job)

    while True:
        schedule.run_pending()
        print("I am runnning")
        time.sleep(1)


if __name__ == "__main__":
    main()
