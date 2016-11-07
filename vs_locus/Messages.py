from __future__ import print_function
'''
A class for issuing messages
'''

import sys
import datetime

class Messages:
    def __init__(self):
        pass
    def __timestamp__(self):
        return "[{}]: ".format(datetime.datetime.now())
    def info(self, str):
        tmp = self.__timestamp__() + '\033[94mInfo\033[0m: ' + str
        print(tmp, file = sys.stderr)
    def success(self, str):
        tmp = self.__timestamp__() + '\033[92mSuccess\033[0m: ' + str
        print(tmp, file = sys.stderr)
    def warning(self, str):
        tmp = self.__timestamp__() + '\033[93mWarning\033[0m: ' + str
        print(tmp, file = sys.stderr)
    def fail(self, str):
        tmp = self.__timestamp__() + '\033[91mFail\033[0m: ' + str
        print(tmp, file = sys.stderr)
