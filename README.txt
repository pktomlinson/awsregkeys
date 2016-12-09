Requirements:

Python 2.7

boto3 and _winreg libraries. 

Script will create registry keys in HKEY_CURRENT_USER if not found.

Then, it opens connection to S3 and lists any buckets you have. If you don't have S3 then this will fail.
