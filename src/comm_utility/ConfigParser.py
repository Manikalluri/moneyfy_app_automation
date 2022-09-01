import sys
import os
from src.comm_utility.Constants import *
import configparser

__config = configparser.ConfigParser(inline_comment_prefixes=(';', '#'))

# Read the config file
__config.read(USER_CONFIG_PATH)

# Primary drive that contains all the
DEFAULT_EXECUTION_PATH = os.path.dirname(os.path.abspath(__file__)) + "/../../"
PASS = 1
FAIL = 0
FALSE = 0
TRUE = 1


class MoneyfyAppConfigGlobal:
    """ These global data would be initialized before the execution of trello web scripts"""


    __config = configparser.ConfigParser(inline_comment_prefixes=(';', '#'))

    # Read the config file
    __config.read(USER_CONFIG_PATH)

    TestFolderPath = DEFAULT_EXECUTION_PATH  # This is the default execution path as set in the global variable - This is CONSTANT

    # Configure Test VS details
    AppiumHost_IP = __config.get("COMMON", "AppiumHost_IP")

