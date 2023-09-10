from chalice import Chalice
import os, boto3, json

app = Chalice(app_name='message')

@app.route('/public', cors=True)
def public():
    data = dict(app.current_request.query_params)
    sns = boto3.client('sns')
    topic_arn = os.environ.get('TOPIC_ARN')
    sns.publish(TopicArn=topic_arn, Message=json.dumps(data))
    return data

@app.route('/')
def index():
    return {'hello': 'world'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
