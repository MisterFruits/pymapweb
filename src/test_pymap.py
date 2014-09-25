"""Test for the pymap package"""
import unittest
import random
import re
from pymap import Account, Mail, Header
import string

def get_random_mail():
    subject = 'SUBJECT_%s' % gen_text(5)
    sender = 'SENDER_%s' % gen_text(5)
    recievers = ['RECIEVER%d_%s' % (el, gen_text(5)) for el in range(random.randint(1, 3))]
    body = gen_text(random.randint(500, 600))
    return Mail(Header(subject, sender, recievers), body)

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
        self.assertTrue(re.search(self.acc.name, self.acc.__str__()))

if __name__ == '__main__':
    """Main procedure, launching unit tests"""
    print(get_random_mail().__str__())
    unittest.main()

