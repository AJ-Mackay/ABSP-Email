# Module 15 - Email: Sending Emails

import smtplib #S(imple) M(ail) T(ransfer) P(rotocol) LIB(rary)

conn = smtplib.SMTP('smtp.gmail.com', 587) # Domain name & port number.
conn.ehlo() # Handshake to connect. Returns a tuple: (Server code, Bytes Data which looks like a string starts with "b'")
conn.starttls() # Begins TLS encryption.
conn.login('email address', 'password')
conn.sendmail('from address', 'to address', 'Subject: Subject goes here\n\nMessage goes here') # Returns a dictionary of messages that failed to send, so hopefully "{}".
conn.quit() # Disconnects from the SMTP server.

### When using ".sendmail", the double linebreaks (\n) change from the Subject to the Body of the message. ###
### When using ".login", Gmail often requires App Specific Passwords. ###
