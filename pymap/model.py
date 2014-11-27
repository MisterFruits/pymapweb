"""
Model for Mails accounts in python
"""
import re
from . import utils

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

class ImapAccount(Account):
    """An account for IMAP protocol"""
    def __init__(self, name, password, imap4):
        super(ImapAccount, self).__init__(name)
        self.password = password
        self.imap4 = imap4

    @property
    def mails(self):
        try:
            self.imap4.login(self.name, self.password)
        finally:
            self.imap4.logout()

    @mails.setter
    def mails(self, value):
        pass

    @property
    def folders(self):
        """Return folders account in a Tree structure"""
        tree = utils.Tree()
        try:
            self.imap4.login(self.name, self.password)
            typ, data = self.imap4.list()
        finally:
           self.imap4.logout()
        if typ == 'OK':
            for response in data:
                (flags, delimiter, mailbox_name) = parse_list_response(response)
                tree.branch(mailbox_name.split(delimiter))
        else:
            raise NotImplementedError("""Response code %r not handled."""
                    """Of type %s with members:"""
                    """%s""" % (typ, type(typ), "\n".join(dir(typ))))
        return tree


list_response_pattern = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')

def parse_list_response(line):
    flags, delimiter, mailbox_name = list_response_pattern.match(line.decode()).groups()
    mailbox_name = mailbox_name.strip('"')
    return (flags, delimiter, mailbox_name)
