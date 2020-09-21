# Module 15 - Email: Sending Emails

import smtplib #S(imple) M(ail) T(ransfer) P(rotocol) LIB(rary)

conn = smptlib.SMTP('smtp.gmail.com', 587) # smtp for Gmail & port number.
conn.ehlo() # Handshake to connect to gmail.
conn.start
