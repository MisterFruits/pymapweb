"""
Model for IMAP in python
"""
#import email

class Account(object):
    """Mail account"""
    def __init__(self, name, mails=None):
        super(Account, self).__init__()
        self.name = name
        self.mails = mails or []

    def __str__(self):
        return 'Account %s: %d mails' % (self.name, len(self.mails))

class Mail(object):
    """Mail"""
    def __init__(self, header, body, attachements=None):
        super(Mail, self).__init__()
        self.header = header
        self.body = body
        self.attachements = attachements or []

    def __str__(self):
        return self.header.__str__()

class Header(object):
    """Mail header"""
    def __init__(self, subject, sender, recievers):
        super(Header, self).__init__()
        self.subject = subject
        self.sender = sender
        self.recievers = recievers

    def __str__(self):
        return "%s from %s" % (self.subject, self.sender)
