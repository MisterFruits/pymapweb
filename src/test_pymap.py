"""Test for the pymap package"""
import unittest
import random
import imaplib, ssl
import re
from pprint import pprint as pp
from pymap import Account, Mail, Header, ImapAccount
import string

def get_random_mail():
    body = gen_text(random.randint(500, 600))
    return Mail(get_random_header(), body)

def get_random_header():
    subject = 'SUBJECT_%s' % gen_text(5)
    sender = 'SENDER_%s' % gen_text(5)
    recievers = ['RECIEVER%d_%s' % (el, gen_text(5)) for el in range(random.randint(1, 3))]
    return Header(subject, sender, recievers)

def get_random_account():
    mails = [get_random_mail() for el in range(random.randint(3, 6))]
    return Account('%sacc' % gen_text(3), mails)

def gen_text(length=8, chars=string.ascii_letters + string.digits):
    return ''.join([random.choice(chars) for i in range(length)])


# pylint: disable=R0904
class AccountTest(unittest.TestCase):
    """Test regarding the Account class"""
    def setUp(self):
        self.acc = Account('Test Account',
                           [get_random_mail() for el in range(5)])

    def test_init(self):
        """Tests constructor"""
        acc = Account('Test Account')
        self.assertEqual('Test Account', acc.name)
        self.assertTrue([] == acc.mails)
        mails = [get_random_mail() for el in range(5)]
        acc = Account('Test Account', mails)
        self.assertEqual('Test Account', acc.name)
        self.assertEqual(mails, acc.mails)

    def test__str__(self):
        """Test to string method"""
        self.assertTrue(re.search(self.acc.name, str(self.acc)))
        self.assertTrue(re.search(str(len(self.acc.mails)), str(self.acc)))

class MailTest(unittest.TestCase):
    """Test regarding the Mail class"""
    def setUp(self):
        self.mail = Mail(get_random_header(),"The Body!")

    # def test_init(self):
    #     """Tests constructor"""
    #     mail = Mail('Test Mail')
    #     self.assertEqual('Test Mail', mail.name)
    #     self.assertTrue([] == mail.mails)
    #     mails = [get_random_mail() for el in range(5)]
    #     mail = Mail('Test Mail', mails)
    #     self.assertEqual('Test Mail', mail.name)
    #     self.assertEqual(mails, mail.mails)

    # def test__str__(self):
    #     """Test to string method"""
    #     self.assertTrue(re.search(self.mail.name, str(self.mail)))
    #     self.assertTrue(re.search(str(len(self.mail.mails)), str(self.mail)))

class ImapAccountTest(unittest.TestCase):
    """docstring for ImapAccountTest"""
    def test_main(self):
        context = ssl.create_default_context()
        imap4 = imaplib.IMAP4_SSL(host='imap.free.fr', port=993,
                                  ssl_context=context)
        account = ImapAccount("vic.toad.tor", "toad6121021990", imap4)
        pp(dict(account.folders))


if __name__ == '__main__':
    """Main procedure, launching unit tests"""
    unittest.main()

