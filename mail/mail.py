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
    except:
        print('Login failed')

    
if __name__=='__main__':
    credentials=get_credentials()
    make_connection(credentials)
