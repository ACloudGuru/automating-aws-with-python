# coding: utf-8
event = {'Records': [{'eventVersion': '2.0', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2018-07-09T14:47:06.505Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDAITRTGNM64QPYU6DW6'}, 'requestParameters': {'sourceIPAddress': '162.233.171.126'}, 'responseElements': {'x-amz-request-id': '5C55894ABB4C09C1', 'x-amz-id-2': 'dBf64puCLEmiN6tkkky037+7JPSJj9n3xvJWDhptJ2VftvVWRgSn1GWhLl2CJFP1FSLYthwF3dc='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '4256d959-8f6f-42c0-8a32-5036a840e2b0', 'bucket': {'name': 'robinvideolyzervideos12345', 'ownerIdentity': {'principalId': 'A3EGVT21L2CFMG'}, 'arn': 'arn:aws:s3:::robinvideolyzervideos12345'}, 'object': {'key': 'Pexels+Videos+4640.mp4', 'size': 10278716, 'eTag': '6bcf2e76121ff9d1c3bf616c49650be7-2', 'sequencer': '005B437568838B6599'}}}]}
event
event['Records'][0]
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
