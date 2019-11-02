import boto3
ACCESS_KEY = 'AKIATLJVLC6JIOIKKU53'
SECRET_KEY = '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'
def create_boto_resource(resource: str, region: str, access_key: str,
secret_key: str) -> boto3.resource:
    resource = boto3.resource(
        resource,
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )
    return resource
    
s3_resource = create_boto_resource(
    resource='s3',
    region='us-east-1',
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY
)
bucket = s3_resource.Bucket('sa-str-hack-ohio')
# list objects in bucket
for obj in bucket.objects.all():
    print(obj)
    # download a dataset
with open('octo-sample.csv', 'wb') as data: bucket.download_fileobj('OCTO-STATEAUTO-1280-TRIPP-20180603-010001-000.csv', data)