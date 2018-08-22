import requests
from chalice import Chalice

SLACK_BOOT_TOKEN = 'xoxb-421141044658-421345925141-Ff18OAMhnaaSVnv3vxZXz84x'
SLACK_API_ROOT_URL = 'https://slack.com/api/'
SLACK_SEND_MESSAGE_ENDPOINT = 'chat.postMessage'

app = Chalice(app_name='git_web_hooks')


@app.route('/', methods=['POST'])
def say_hello():

    url = SLACK_API_ROOT_URL + SLACK_SEND_MESSAGE_ENDPOINT

    data = {
        "channel": "CCD8EC5DK",
        "text": "Teestttt"
    }

    headers = {
        "Authorization": "Bearer " + SLACK_BOOT_TOKEN
    }

    requests.post(url, data=data, headers=headers)

    return {}


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
