import os
import json
import boto3
import logging
import urllib

iam = boto3.resource('iam')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# TODO: リファクタリング
def handler(event, context):
    logger.info(event)

    if validate(event):
        iam.AccessKey(os.environ['AWS_IAM_USER_NAME'], os.environ['AWS_IAM_ACCESS_KEY_ID']).deactivate()

        body = {
            'username': 'IAM',
            'text': ':lock: ' * 3 + 'CircleCIの本番環境の鍵を無効化しました ' + ':lock: ' * 3
        }
    else:
        body = {
            'username': 'IAM',
            'text': ':warning: ' * 3 + '許可されてませんねぇ.. ' + ':warning: ' * 3
        }

    result = {
        'statusCode': 200,
        'body': json.dumps(body)
    }

    return result


def validate(event):
    params = urllib.parse.parse_qs(event['body'])

    accepted_users = os.environ['ACCEPTED_SLACK_USERS'].split(',')
    accepted_tokens = os.environ['SLACK_ACCESS_TOKENS'].split(',')

    if not params['user_id'][0] in accepted_users or not params['token'][0] in accepted_tokens:
        return False

    return True
