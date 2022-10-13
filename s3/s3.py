import os, boto3, time, tempfile, pathlib

AWS_KEY = os.environ['AWSKEY'] 
AWS_SECRECT = os.environ['AWSSECRECT'] 
AWS_REGION = os.environ['AWSREGION']
AWS_BUCKET = os.environ['AWSBUCKET']
AWS_FOLDER = os.environ['AWSFOLDER']


session = boto3.Session(
    aws_access_key_id = AWS_KEY,
    aws_secret_access_key= AWS_SECRECT,
    region_name=AWS_REGION
    )
s3 = session.resource('s3')

bucket = s3.Bucket(AWS_BUCKET)

def upload_string(fname,strdata,acl, content_type = 'text/html',
                content_dispo='attachment'):
    """
    accepts string and uploads in s3 returns bot s3url and publi url for object
    """
    str_dt = time.strftime("%m%d%Y")
    key = f'{AWS_FOLDER}/{str_dt}/{fname}'
    bucket.put_object(Key=key,Body=strdata,ACL=acl,
                     ContentDisposition= content_dispo,
                     ContentType=content_type)

    s3_url = f's3://{AWS_BUCKET}/{key}'
    s3_public = f'https://{AWS_BUCKET}.s3.amazonaws.com/{key}'
    return s3_public,s3_url

def upload_file(fname,acl):
    str_dt = time.strftime("%m%d%Y")
    file_name = pathlib.Path(fname).stem
    key = f'{AWS_FOLDER}/{str_dt}/{file_name}'
    bucket.upload_file(Filename=fname,Key=key, ExtraArgs={'ACL':acl})
    s3_url = f's3://{AWS_BUCKET}/{key}'
    s3_public = f'https://{AWS_BUCKET}.s3.amazonaws.com/{key}'
    return s3_url, s3_public

def download_file(filename):
    """
        download the file to tempfile , and return path without deleting
    """
    i_filename = filename.replace('s3://','')
    f_split = i_filename.split('/')
    KEY = '/'.join(f for f in f_split[1:])
    tmp = tempfile.NamedTemporaryFile(delete=False,suffix='.csv')
    with open(tmp.name,'wb') as fp:
        bucket.download_fileobj(Key=KEY, Fileobj=fp)
        fp.seek(0)
    return tmp


if __name__ == '__main__':
   print(upload_string(fname='tetst2.txt',strdata='this is new file'))

