# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:426176885551:handleLabelDetectionTopic:01478983-30d7-47c7-ac3b-8c4d8fe17af4', 'Sns': {'Type': 'Notification', 'MessageId': '49ce09ca-3d12-5d25-af88-5a74cf680e70', 'TopicArn': 'arn:aws:sns:us-east-1:426176885551:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"dbd80e840fdec0f1525764d05f6b81166b8a318a7f8df6e55d2aa24d2eeaf443","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1531244602671,"Video":{"S3ObjectName":"Pexels Videos 4640.mp4","S3Bucket":"robinvideolyzervideos12345"}}', 'Timestamp': '2018-07-10T17:43:22.773Z', 'SignatureVersion': '1', 'Signature': 'Xg7bTkMLIXc9C1lPDLP0vaGDtSAiqJ7TL5+XABeq5RMVATkS4o2isvW5I5S8GG5aKhs2wj5aHC1wDekM8tbHSJpAFGlprN6tehgJRvCQkr9XVplgLxm8ACbw04HZskXTXd+s8Ay1Vu7a54tRfPEQ6GtuE1GJXLA6P+JtnXDV5gyrJDR87dwcHDvkajwlOhyoF8J+LJ8JmQvbNJlfu4ijxDLh0SBbaiFED7SRp1FKMjmzHD8wPshTSzfUBwUdhFFJueHiwM+eZjxR9zA+b+kywPPPjuRndBs7DgygbMVHs/6R6sUdbUzrBet7N5BwBlkXxLJb1aNF1bMXXK6qAidW9w==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-eaea6120e66ea12e88dcd8bcbddca752.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:426176885551:handleLabelDetectionTopic:01478983-30d7-47c7-ac3b-8c4d8fe17af4', 'MessageAttributes': {}}}]}
event.keys()
event['Records'][0]
event['Records'][0].keys()
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Message']
event['Records'][0]['Sns']['Message']['JobId']
type(event['Records'][0]['Sns']['Message'])
import json
json.loads(event['Records'][0]['Sns']['Message'])
