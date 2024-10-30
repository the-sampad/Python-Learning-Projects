import datetime as dt
import random
import smtplib
day_name_day = dt.datetime.today().strftime('%A')
data = open('quotes.txt','r')
quotes =  data.readlines()
quote = random.choice(quotes)
quote_day = 'Tuesday'
my_email = 'sampadedge@gmail.com'
if day_name_day == quote_day:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password='Sampad@2000')
        connection.sendmail(
            from_addr = my_email,
            to_addrs = 'sampad.secondary@gmail.com',
            msg = f'Subject:Quote sending test from python\n\n{quote}'
        )
else:
    print(f'Sorry today is {day_name_day} not {quote_day}')





