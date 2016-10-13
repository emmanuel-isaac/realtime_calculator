from __future__ import division

import re
import json
import logging

from channels import Group
from channels.sessions import channel_session

from .models import CalculatorData

log = logging.getLogger(__name__)


@channel_session
def ws_connect(message):
    Group('calculate', channel_layer=message.channel_layer).add(message.reply_channel)


@channel_session
def ws_receive(message):
    try:
        data = json.loads(message['text'])
    except ValueError:
        log.debug("ws message isn't json text=%s", text)
        return

    if set(data.keys()) != set(('owner', 'entry')):
        log.debug("ws message unexpected format data=%s", data)
        return

    if data:
        log.debug('owner=%s entry=%s', **data)
        data['result'] = '%.3f' % round(eval(compile(data['entry'], '<string>', 'eval', division.compiler_flag)), 3)
        data['owner'] = data['owner'] or 'AnonymousUser'
        m = CalculatorData.objects.create(**data)

        Group('calculate', channel_layer=message.channel_layer).send({'text': json.dumps(m.as_dict())})

def ws_disconnect(message):
    Group('calculate', channel_layer=message.channel_layer).discard(message.reply_channel)
