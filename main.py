import sys
import twitter
from datetime import datetime, timezone
import schedule
import time

def job():
    message = 'I am live in Heroku and I am suppose to tweet every hour! ' + datetime.utcnow().strftime("%a, %b, %D - %T")
    api = twitter.Api(consumer_key='kWTqtf716ZGDUvw9YEXbSU7o3',
                      consumer_secret='g6sIaAm9Ku5LbsC28Ub7hnvvBTznVjdzzKprCgVqnixTGR4E9G',
                      access_token_key='878885859772162049-3jrDmGf8sxb7rs7b8HvYpUrpCl3kjF3',
                      access_token_secret='G9XteyJXBmdeNJfDURScrf8DVZVYSCEy8Ug7IfrqNnVuC',)
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
