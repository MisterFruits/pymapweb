"""
Model for IMAP in python
"""
import email
import random
import string

class Account:
    """docstring for Account"""
    def __init__(self, name, mails):
        self.name = name
        self.mails = mails

class Mail:
    """docstring for Mail"""
    def __init__(self, subject, sender, recievers, body, attachements = None):
        super(Mail, self).__init__()
        self.subject = subject
        self.sender = sender
        self.recievers = recievers
        self.body = body
        self.attachements = attachements

    def __str__(self):
        return self.subject

def get_random_mail():
    subject = gen_text(5, 'Subject %s')
    sender = gen_text(5, 'Sender %s')
    recievers = [gen_text(5, 'Reciever%d %%s' % el) for el in range(random.randint(1,3))]
    body = gen_text(random.randint(500, 600))
    return Mail(subject, sender, recievers, body)

def get_random_account():
    mails = [get_random_mail() for el in range(random.randint(3,6))]
    return Account(gen_text(3, '%sacc'), mails)

def gen_text(length=8, formatter='', chars=string.ascii_letters + string.digits):
    return ''.join([random.choice(chars) for i in range(length)])

if __name__ == '__main__':
    test = [get_random_account() for el in range(4)]

