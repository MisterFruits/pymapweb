"""Test for the pymap package"""
import unittest
import random
import imaplib, ssl
import re
from pprint import pprint as pp
from pymap import Account, Mail, Header, ImapAccount, Tree, branch
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
        imap4 = imaplib.IMAP4_SSL(host='imap.free.fr', port=993)
        account = ImapAccount("vic.toad.tor", "toad6121021990", imap4)
        imap4.logout()
        # pp(dict(account.folders))

class PymapTest(unittest.TestCase):
    """Test for package methods"""
    def test_Tree(self):
        self.assertEqual(Tree(), {})
        tree = Tree()
        tree[40]
        self.assertEqual({40:{}}, tree)
        tree[40]
        self.assertEqual({40:{}}, tree)
        tree[30]
        self.assertEqual({40:{}, 30:{}}, tree)
        tree[40][3]
        self.assertEqual({40:{3:{}}, 30:{}}, tree)

    def test_branch(self):
        expectedtree = Tree()
        actualtree = Tree()

        expectedtree['path']
        branch(['path'], actualtree)
        self.assertEqual(expectedtree, actualtree)

        expectedtree['poth']
        branch(['poth'], actualtree)
        self.assertEqual(expectedtree, actualtree)

        expectedtree['path']['to']['dir']
        branch(['path','to','dir'], actualtree)
        self.assertEqual(expectedtree, actualtree)

        expectedtree = Tree()
        actualtree = Tree()
        expectedtree[1]['A']['i']
        expectedtree[1]['A']['ii']
        expectedtree[1]['B']
        expectedtree[2]['A']['i']
        branch([1, 'A', 'i'], actualtree)
        branch([1, 'A', 'ii'], actualtree)
        branch([1, 'B'], actualtree)
        branch([2, 'A', 'i'], actualtree)
        self.assertEqual(expectedtree, actualtree)

if __name__ == '__main__':
    """Main procedure, launching unit tests"""
    unittest.main()

