import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http


# When a user logs in, add them to the 'users' group,
# with their username and the value of 'is_logged_in',
# websockets have to be passed a JSON serializable message
@channel_session_user_from_http
def ws_connect(message):
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': True
        })
    })
    Group("chat").add(message.reply_channel)

# When the user logs out remove them from the 'users' group,
# and change the is_logged_in value to false
@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('users').discard(message.reply_channel)
    Group("chat").discard(message.reply_channel)

# Trying to send messages through websockets for chat,
# 'text' represents the data of the message being sent
def ws_message(message):
    # Group('chat').add(message.reply_channel)
    # Group('chat').send({
    #     'text': json.dumps({
    #         'message': message
    #     })
    # })
    
    # 'text': json.dumps({

    # })
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })
