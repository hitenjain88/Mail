import email,imaplib


def get_credentials():
    username=input('Enter the Username : ')
    password=input('Enter the Password : ')
    return [username,password]


def make_connection(cred):
    con=imaplib.IMAP4_SSL('imap.gmail.com')
    try:
        con.login(cred[0],cred[1])
        print('Login Successful')
        con.select('inbox')
        typ, data=con.search(None,'ALL')
        index=data[0].split()
        for i in index[::-1]:
            typ,data=con.fetch(i,'(RFC822)')
            for word in data:
                if isinstance(word,tuple):
                    msg=email.message_from_bytes(word[1])
                    email_subject=msg['subject']
                    email_from=msg['from']
            for word in msg.walk():
                if word.get_content_type()=='text/plain':
                    body=part.get_payload(decode=True)
                    msg1=body.decode('utf-8')
            message.append(msg1)
            subject.append(email_subject)
            From.append(email_from)
    except Exception as e:
        print(str(e))

    
if __name__=='__main__':
    message=[]
    From=[]
    subject=[]
    credentials=get_credentials()
    make_connection(credentials)
