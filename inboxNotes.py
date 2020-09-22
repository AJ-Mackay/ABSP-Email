# Module 15 - Email: Checking Your Email Inbox

# I(nternet) M(essage) A(ccess) P(rotocol)

import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True) # Domain name, "ssl=True" lets gmail know that we want to use SSL Encryption.
conn.login('username/email address', 'password') # Returns Bytes data "b' [email address goes here] authenticated (Success)'".
conn.select_folder('INBOX', readonly=True) # Desired message folder, setting "readonly=True" prevents you from accidentally deleting emails.
UIDs = conn.search(['SINCE 20-Aug-2015']) # Returns the Unique IDs of all Emails received since the date entered as integers.
rawMessage = conn.fetch([integer], ['BODY[]', 'FLAGS']) # The integers for the desired emails go in the first list, separated by commas if more than one is desired.

import pyzmail

message = pyzmail.PyzMessage.factory(rawMessage[integer][b'BODY[]']) # The integer of the message goes in the first list.
message.get_subject() # Returns the subject of the message.
message.get_addresses('from') # Returns a tuple [('name of sender if set(email address if not)', 'email address of sender')].

message.text_part # Returns "MailPart<*text/plain len=XX>" if the message was just text, XX = length (number of characters).
message.html_part # Returns None if the message did not contain HTML. ("message.html_part == None" returns True).
message.text_part.get_payload().decode('UTF-8') # Returns a string of the message text. 99% of the time UTF-8 is used for encoding.

### Some Basic IMAP Search Keys ###
# 'ALL' = Returns all messages in the folder.

# 'BEFORE date'
# 'ON date'
# 'Since date'
### Date MUST be in the format DD-MMM-YYYY, e.g 05-Jul-2015 ###

# 'SUBJECT string'
# 'BODY string'
# 'TEXT string'
### "TEXT" searches both the subject and the body of the message ###
### if the search term is multiple words with spaces, wrap it in double quotes e.g 'Text "words to look for"'  ###

### To see all the available folders: ###
# conn.list_folders() # Returns tuples of Bytes data, the name of the folder is the third item e.g [((b'\\HasNoChildren',), b'/', 'Drafts'), ((b'\\HasNoChildren',), b'/', 'INBOX')] 

### Example: To delete messages ###
conn.select_folder('INBOX', readonly=False) # Allows modifications
UIDs = conn.search(['ON 24-Aug-2015']) # Searches for all the Emails that arrived on the date given.
UIDs # Returns a list of Unique IDs as integers.
conn.delete_messages([integers]) # Deletes the selected messsages when the integers are passed as a list.
# conn.delete_messages(UIDs) Could also be used to delete all the messages that were recieved on 24th August 2015.

### Further Reading: ###
# https://imapclient.readthedocs.org
# http://www.magiksys.net/pyzmail
# https://automatetheboringstuff.com/chapter16
