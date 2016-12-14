
getAwsKeys:

class for retrieving your aws keys from the registry

myKeys = getAwsKeys()
  
  myKeys.asak
  myKeys.aski

Requirements:

Python 2.7
_winreg

setAwsKeys:

class for inserting your aws keys into the windows registry

myKeys = setAwsKeys(AWS_SECRET_KEY_ID, AWS_SECRET_ACCESS KEY)

Requirements:

Python 2.7
_winreg



winregread.py

Script will create registry keys in HKEY_CURRENT_USER if not found.

Then, it opens connection to S3 and lists any buckets you have. If you don't have S3 then this will fail.

Requirements:

Python 2.7

boto3 and _winreg libraries. 
