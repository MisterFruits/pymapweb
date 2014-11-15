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
        tree = Tree()
        try:
            self.imap4.login(self.name, self.password)
            typ, data = self.imap4.list()
            if typ == 'OK':
                for response in data:
                    pass
                    # branch(response[1], response[2], tree)
            else:
                raise NotImplementedError("""Response code %r not handled.
Of type %s with members:
%s""" % (typ, type(typ), "\n".join(dir(typ))))
        finally:
            self.imap4.logout()
        return tree

def branch(elements, tree):
    if elements:
        branch(elements[1:], tree[elements[0]])

class Tree(dict):
    """Tree structure definition"""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

    def branch(self, elements):
        if elements:
            branch(elements[1:], self[elements[0]])


