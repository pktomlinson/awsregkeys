from _winreg import *

class setAwsKeys(object):
        """setAwsKeys: a class for storing your AWS_SECRET_ACCESS KEY
        and AWS_SECRET_KEY_ID in the windows registry

        Attributes:
        asak - aws_secret_access_key
        aski - aws_secret_key_id
    

        Registry hive used is HKEY_CURRENT_USER\SOFTWARE\AWS so multiple
        users may use independent key sets on the same machine.

        See getAwsKeys for class to read your AWS_SECRET_ACCESS KEY
        and AWS_SECRET_KEY_ID from the windows registry"""

        def __init__(self, aski, asak):
                _wreg = ConnectRegistry(None, HKEY_CURRENT_USER)
                _aws_root_key = CreateKey(_wreg, 'SOFTWARE\\AWS')
                SetValueEx(_aws_root_key, 'ASAK',0, REG_SZ, asak)
                SetValueEx(_aws_root_key, 'ASKI',0, REG_SZ, aski)



