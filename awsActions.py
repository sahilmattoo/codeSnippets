import boto3
import re
import sagemaker

destination = "/SAHIL/Doc2VecModels"

""" Find the list of FileNames """

my_bucket_name = "bucket-name"
src_dest= "nested/folder/within/bucket/"

s3 = boto3.resource('s3')
my_bucket = s3.Bucket(my_bucket_name)
my_bucket = s3.Bucket(my_bucket_name)
for object_summary in my_bucket.objects.filter(Prefix=src_dest):
    filename = object_summary.key
    print(filename)

filename1 = "nested/file/name/structure/doc2vec_dm_nontrainable.model"
filename2 = "nested/file/name/structure/doc2vec_dm_nontrainable.model.trainables.syn1neg.npy"

## Download Files

import boto3
import botocore

BUCKET_NAME = my_bucket_name # replace with your bucket name
KEY = filename1 # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, "./savedmodels/doc2vec_dm_nontrainable.model")
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

## Alternate Method::

BUCKET_NAME = my_bucket_name # replace with your bucket name
KEY = filename1 # replace with your object key
s3 = boto3.resource('s3')
s3.Bucket(BUCKET_NAME).download_file(KEY, "file.json")


## Upload to S3 from Jupyter Notebook
s3 = boto3.resource('s3')
s3.Bucket(BUCKET_NAME).upload_file("file.json", filename1)
