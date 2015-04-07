# -*- coding: utf-8 -*-
"""
Model for Mails accounts in python
"""
import email.header
import imapclient.response_types
from collections import defaultdict

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
    def __init__(self, header=None, body=None, attachements=None):
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
    def __init__(self, name, imap, folder=u'INBOX'):
        super(ImapAccount, self).__init__(name)
        self.imap = imap
        self.folder = folder
        self._mails = {}

    @property
    def mails(self):
        self.imap.select_folder(self.folder)
        mails = []
        for uid in self.imap.search():
            if uid not in self._mails:
                self._mails[uid] = ImapMail(uid, self.imap)
            mails.append(self._mails[uid])
        return mails

    @mails.setter
    def mails(self, value):
        pass

    @property
    def folders(self):
        """Return folders account in a Tree structure"""
        folders = self.imap.list_folders(self.folder)

class ImapMail(Mail):
    """A mail lazzy fecthing the IMAP protocol"""
    def __init__(self, uid, imap):
        super(ImapMail, self).__init__()
        self.uid = uid
        self.imap = imap
        self._header = None

    @property
    def header(self):
        if not self._header:
            self._header = ImapHeader(self.uid, self.imap)
        return self._header

    @header.setter
    def header(self, value):
        pass

class ImapHeader(Header):
    """Lazzy structure fetching IMAP protocol"""
    def __init__(self, uid, imap):
        self.envelope = imap.fetch(uid, ['ENVELOPE'])[uid][b'ENVELOPE']
        subject = decode_header(self.envelope.subject).strip()
        sender = decode_address(self.envelope.sender[0])
        super(ImapHeader, self).__init__(subject, sender, None)

def decode_header(bytes_input, imap_encoding='us-ascii'):
    encoded_string = bytes_input.decode(imap_encoding)
    test = bytes_output, encoding = email.header.decode_header(encoded_string)[0]
    if encoding:
        return bytes_output.decode(encoding)
    return bytes_output

def decode_address(address):
    d = defaultdict(None)
    if address.mailbox:
        d['mailbox'] = decode_header(address.mailbox)
    else:
        d['mailbox'] = None
    if address.host:
        d['host'] = decode_header(address.host)
    else:
        d['host'] = None
    if address.name:
        d['name'] = decode_header(address.name)
    else:
        d['name'] = None
    if address.route:
        d['route'] = decode_header(address.route)
    else:
        d['route'] = None
    return imapclient.response_types.Address(**d)
