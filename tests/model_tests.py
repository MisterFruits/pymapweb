"""Test for the pymap package"""
import unittest
from pymap.model import Account, Mail, Header
import pymap.utils
import re, random
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
    #     mails = [RandomMail() for el in range(5)]
    #     mail = Mail('Test Mail', mails)
    #     self.assertEqual('Test Mail', mail.name)
    #     self.assertEqual(mails, mail.mails)

    # def test__str__(self):
    #     """Test to string method"""
    #     self.assertTrue(re.search(self.mail.name, str(self.mail)))
    #     self.assertTrue(re.search(str(len(self.mail.mails)), str(self.mail)))

# class ImapAccountTest(unittest.TestCase):
#     """docstring for ImapAccountTest"""
#     def test_main(self):
#         imap4 = imaplib.IMAP4_SSL(host='imap.free.fr', port=993)
#         account = ImapAccount("vic.toad.tor", "", imap4)
#         imap4.logout()
#         # pp(dict(account.folders))
#
# if __name__ == '__main__':
#     """Main procedure, launching unit tests"""
#     unittest.main()

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
