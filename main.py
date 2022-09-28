import imaplib
from settings import *


# This data is taken from a file settings.py
# FOLDERS = ['"INBOX"', '"[Gmail]/&BB4EQgQ,BEAEMAQyBDsENQQ9BD0ESwQ1-"']
# mail_pass = ""
# username = ""
# imap_server_port = ("imap.gmail.com", 993)
# date_range='(SINCE "01-Jan-2016" BEFORE "30-dec-2020")'


def main():
    with imaplib.IMAP4_SSL(*imap_server_port) as imap:
        imap.login(username, mail_pass)
        for folder in FOLDERS:
            imap.select(folder)
            data = imap.search(None, date_range)[1]
            data = data[0].split()
            while data:
                print(data)
                for i in range(10):
                    try:
                        item = data.pop()
                    except IndexError:
                        break
                    print(item)
                    imap.store(item, '+FLAGS', '\\Deleted')
                imap.expunge()


if __name__ == '__main__':
    main()
