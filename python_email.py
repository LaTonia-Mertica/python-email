import smtplib

# conn = smtplib.SMTP('smtp.gmail.com', 587)
conn = smtplib.SMTP('smtp-mail.outlook.com', 587)
print('Hello Code World')
type(conn)
try:
    conn.ehlo()
    conn.starttls()
    conn.login('enter sender email here in these quotes', 'enter sender password in these quotes')
    conn.sendmail('enter sender email here in these quotes', 'enter recipient email here in these quotes','Subject:Subject line message goes here before double newlines\n\nEmail body text goes here inside end quote while after the double newlines')
except Exception as error:
        # print error message to stdout
    print(error)
finally:
    conn.quit()
