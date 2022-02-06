import boto3
import pandas

# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id = 'AKIA3VABAJ3ZMFY76XFZ',
    aws_secret_access_key = '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',
    region_name = 'ap-south-1'
)
    
# Creating the high level object oriented interface
resource = boto3.resource(
    's3',
    aws_access_key_id = 'AKIA3VABAJ3ZMFY76XFZ',
    aws_secret_access_key = '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',
    region_name = 'ap-south-1'
)

# Creating a bucket in AWS S3
location = {'LocationConstraint': 'ap-south-1'}
client.create_bucket(
    Bucket='shreysteeleye',
    CreateBucketConfiguration=location
)

# Fetch the list of existing buckets
clientResponse = client.list_buckets()
    
# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')

# Create the S3 object
obj = client.get_object(
    Bucket = 'shreysteeleyedemo',
    Key = './steeleye1.csv')

# Read data from the S3 object
data = pandas.read_csv(obj['Body'])
    
# Print the data frame
print('Printing the data frame...')
print(data)