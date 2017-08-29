'''
File: heartbeat.py
Description: heartbeat type messages just to let the client know that we are there
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 29/08/2017
'''
from base import MessageBase
import datetime
import json

class Heartbeat(MessageBase):
    '''Heartbeat Message

    Sends a repeating heartbeat after every 5 seconds to let the clients know
    that the server is alive. This is a special type of message that does not
    contain any type of executable command and just provides time of heartbeat.
    '''

    def __init__(self):
        """Heartbeat constructor"""

        super(MessageBase, self).__init__(self.__class__.__name__)
        self.time = str(datetime.time())
        self.set_command('heartbeat')
        self.set_extras(self.time)

    def __str__(self):
        """Provide the string representation of the class"""

        return "<{} {}>".format(self.__class__.__name__, self.time)
