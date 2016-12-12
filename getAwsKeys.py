from _winreg import *

class getAwsKeys(object):
        """getAwsKeys: a class for retrieving your AWS_SECRET_ACCESS KEY
            and AWS_SECRET_KEY_ID from the windows registry

            Attributes:
            asak - aws_secret_access_key
            aski - aws_secret_key_id
            

            Registry hive used is HKEY_CURRENT_USER\SOFTWARE\AWS so multiple
            users may use independent key sets on the same machine.

            See setAwsKeys for class to write your AWS_SECRET_ACCESS KEY
            and AWS_SECRET_KEY_ID to the windows registry"""
        
        def __init__(self):
                _wreg = ConnectRegistry(None, HKEY_CURRENT_USER)
                _aws_root_key = OpenKey(_wreg, 'SOFTWARE\\AWS')
                self.aws_secret_access_key = QueryValueEx(_aws_root_key, "ASAK")
                self.aws_secret_key_id = QueryValueEx(_aws_root_key, "ASKI")
                self.asak = self.aws_secret_access_key[0]
                self.aski = self.aws_secret_key_id[0]


