# -*- coding: utf-8 -*-
"""
Model for Mails accounts in python
"""
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
        super(ImapHeader, self).__init__(subject, sender, recievers)
        self.uid = uid
        self.imap = imap
        self._envelope = None
        self._subject = None

    @property
    def subject(self):
        if not self._subject:
            self._subject ='otot'
        return self._subject

    @subject.setter
    def subject(self, value):
        pass

    @property
    def sender(self):
        return "No sender"

    @sender.setter
    def sender(self, value):
        pass

