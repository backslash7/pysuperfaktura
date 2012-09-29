__author__ = 'backslash7 <lukas.stana@it-admin.sk>'

class SFAPIException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
