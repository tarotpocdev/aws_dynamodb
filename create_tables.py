import boto3
from boto3.dynamodb.conditions import Key, Attr

# get session
session = boto3.Session(profile_name='tarot_iam_dynamodb')

# Get the service resource.
dynamodb = session.resource('dynamodb')

# Create the DynamoDB table.
# table = dynamodb.create_table(
#     TableName='CardInfo',
#     KeySchema=[
#         {
#             'AttributeName': 'card_no',
#             'KeyType': 'HASH'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'card_no',
#             'AttributeType': 'N'
#         }
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

table = dynamodb.Table('CardInfo')

# Wait until the table exists.
# table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)

# put item to table
# table.put_item(
#   Item={
#     'card_no': 1,
#     'nickname': '더 풀',
#     'overall_type': ''
#   }
# )

# get item from table
# response = table.get_item(
#   Key={
#     'card_no': 1,
#   }
# )
# item = response['Item']
# print(item)

# query item
response = table.query(
  KeyConditionExpression=Key('card_no').eq(1)
)
items = response['Items']
print(items)

# delete table
table.delete()
