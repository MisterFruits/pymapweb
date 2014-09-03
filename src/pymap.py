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

class Mail(email.message.Message):
    """docstring for Mail"""
    def __init__(self, subject, senders, body, attachements = None):
        super(Mail, self).__init__()
        self.subject = subject
        self.senders = senders
        self.body = body
        self.attachements = attachements

def get_random_mail():
    subject = gen_text(5, 'Subject %s')
    senders = [gen_text(5, 'Sender%d %s' % el) for el in random.randrange(3)]
    body = gen_text(random.randint(500,600))
    return Mail(subject, senders, body)

def get_random_account():
    mails = [get_random_mail() for el in random.randrange(3,6)]
    return Account(gen_text(3, '%sacc'), mails)

def gen_text(length=8, formatter='', chars=string.ascii_letters + string.digits):
    return ''.join([random.choice(chars) for i in range(length)])

if __name__ == '__main__':
    pass
