from _winreg import *
import boto3
import botocore
import os

def GetCredentialsFromUser():
	print "IN GetCredentialsFromUser"
	try: 
		ASKI = os.environ['AWS_ACCESS_KEY_ID']
	except:
		ASKI = raw_input("\n\nAWS Access Key ID: ")		
	
	try:
		ASAK = os.environ['AWS_SECRET_ACCESS_KEY']
	except:
		ASAK = raw_input("\nAWS Secret Access Key: ")
	
	return(ASAK,ASKI)
	


def ReadReg(wreg):
	print "IN ReadRegistry"
	try:
		s3u_root_key = OpenKey(wreg, 'SOFTWARE\\AWS')
		print "AWS key found!"
		aws_secret_access_key = QueryValueEx(s3u_root_key, "ASAK")
		aws_secret_key_id = QueryValueEx(s3u_root_key, "ASKI")
		return(aws_secret_access_key, aws_secret_key_id)
		
	except EnvironmentError:
		print "AWS not installed. Creating..."
		s3u_root_key = CreateKey(wreg, 'SOFTWARE\\AWS')
		ASAK, ASKI = GetCredentialsFromUser()
		SetValueEx(s3u_root_key, 'ASAK',0, REG_SZ, ASAK)
		SetValueEx(s3u_root_key, 'ASKI',0, REG_SZ, ASKI)	
		CloseKey(s3u_root_key)
	

# let's get started
#
def LetsGetStarted():
	print "LET'S GET STARTED"	
	try:
		wreg = ConnectRegistry(None, HKEY_CURRENT_USER)
		asak, aski = ReadReg(wreg)
		aski = aski[0]
		asak = asak[0]
		print aski
		print asak
		s3 = boto3.resource('s3', aws_access_key_id=aski, aws_secret_access_key=asak)
		for bucket in s3.buckets.all():
			print(bucket.name)
			
	except:
		print "Something broke"


if __name__ == "__main__":
	LetsGetStarted()
