"""
Model for IMAP in python
"""
import email

class Account:
    """docstring for Account"""
    def __init__(self, name):
        self.name = name
        self.mails = []

class Mail(email.message.Message):
    """docstring for Mail"""
    def __init__(self, subject, sender, body, attachement = None):
        super(Mail, self).__init__()
        self.subject = subject
        self.sender = sender
        self.body = body
        self.attachement = attachement


if __name__ == '__main__':
    pass
