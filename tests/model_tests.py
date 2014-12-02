"""Test for the pymap package"""
import unittest
from unittest import mock
from pymap.model import Account, Mail, Header, ImapAccount
import pymap.utils
import re, random, logging
from pprint import pprint as pp

# pylint: disable=R0904
class AccountTest(unittest.TestCase):
    """Test regarding the Account class"""
    def setUp(self):
        self.acc = Account('Test Account',
                           [RandomMail() for el in range(5)])

    def test_init(self):
        """
        Tests constructor
        """
        acc = Account('Test Account')
        self.assertEqual('Test Account', acc.name)
        self.assertTrue([] == acc.mails)
        mails = [RandomMail() for el in range(5)]
        acc = Account('Test Account', mails)
        self.assertEqual('Test Account', acc.name)
        self.assertEqual(mails, acc.mails)

    def test_str(self):
        """Test to string method"""
        self.assertRegex(str(self.acc), self.acc.name)
        self.assertRegex(str(self.acc), str(len(self.acc.mails)))

class MailTest(unittest.TestCase):
    """Test regarding the Mail class"""
    def setUp(self):
        self.mail = Mail(RandomHeader(), "The Body!")

    def test_str(self):
        """Test to string method"""
        self.assertRegex(str(self.mail), str(self.mail.header))

class ImapAccountTest(unittest.TestCase):
    """docstring for ImapAccountTest"""
    def setUp(self):
        host = 'imap.free.fr'
        self.username = 'username'
        self.password = 'password'
        self.imap4 = mock.Mock()
        self.account = ImapAccount(self.username, self.password, self.imap4)

    def test_init(self):
        self.assertTrue(self.account.password)
        self.assertEqual(self.username, self.account.name)

    def test_mails(self):
        pass
    def test_folders(self):
        self.imap4.list.return_value = imap_list
        foldertree = self.account.folders

class RandomAccount(Account):
    """Account with random generated datas for tests purposes"""
    def __init__(self):
        super(RandomAccount, self).__init__('%sacc' % pymap.utils.gentext(3))
        mails = [RandomMail() for el in range(random.randint(3, 6))]

class RandomMail(Mail):
    """Mail with random generated dates for tests purposes"""
    def __init__(self):
        super(RandomMail, self).__init__(RandomHeader(),
                                        pymap.utils.gentext(random.randint(500, 600)))

class RandomHeader(Header):
    """docstring for RandomHeader"""
    def __init__(self):
        super(RandomHeader, self).__init__('SUBJECT_%s' % pymap.utils.gentext(5),
            'SENDER_%s' % pymap.utils.gentext(5),
            ['RECIEVER%d_%s' % (el, pymap.utils.gentext(5))
                for el in range(random.randint(1, 3))])


imap_list = ('OK', [b'(\\HasChildren) "/" "[Airmail]"', b'(\\HasNoChildren) "/" "[Airmail]/Done"', b'(\\HasNoChildren) "/" "[Airmail]/Memo"', b'(\\HasNoChildren) "/" "[Airmail]/To Do"', b'(\\HasNoChildren) "/" "Archive"', b'(\\HasNoChildren) "/" "Chats"', b'(\\HasNoChildren) "/" "Contacts"', b'(\\HasNoChildren) "/" "Drafts"', b'(\\HasNoChildren) "/" "Emailed Contacts"', b'(\\HasChildren) "/" "INBOX"', b'(\\HasNoChildren) "/" "INBOX/sent-mail"', b'(\\NoInferiors) "/" "Junk"', b'(\\HasNoChildren) "/" "Sent"', b'(\\HasNoChildren) "/" "Starred"', b'(\\HasNoChildren) "/" "Trash"'])
