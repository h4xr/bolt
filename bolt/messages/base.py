'''
File: base.py
Description: Provides the base class for the messages infrastructure for bolt
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 29/08/2017
'''
import json

class MessageBase(object):
    '''Base class for the messages infrastructure

    Provides some common functionality and must to be overriden methods that
    should be present in all the deriving classes.
    '''

    MESSAGE_TYPE = {
        'COMMAND': 'command',
        'API_REQ': 'api_request',
        'HEARTBEAT': 'heartbeat'
    }

    def __init__(self, message_class, message_type='command'):
        """MessageBase constructor

        Initializes the MessageBase with the supported parameters to mark the
        start of the message. The method also initializes the message_body
        structure which needs to be transmitted during the server to client
        communication.

        @message_body: Dictionary type structure encompassing the following keys
        @key command String The command to be executed
        @key subcommand List The list of subcommands that should be passed
        @key options List A list of tuples holding the options and any value passed to them

        Args:
            message_class(str): The name of the deriving message class
        """

        self.message_class = message_class
        self.message_body = {
            'type': message_type,
            'command': '',
            'subcommand': [],
            'options': [],
            'extras': []
        }

    def __str__(self):
        """Returns the string type representation of the message class

        Returns:
            String
        """

        error_message = "{} does not implement string representation"
        raise NotImplemedtedError(error_message.format(self.message_class))

    def clear(self):
        """Clear the message body
        """

        self.message_body['command'] = ''
        self.message_body['subcommand'] = []
        self.message_body['options'] = []
        self.message_body['extras'] = []

    def set_command(self, command):
        """Set the command to be executed

        Args:
            command(str): The command to be executed
        """

        self.message_body['command'] = command

    def set_subcommand(self, sub_command):
        """Set the subcommand to be passed to the main command

        Args:
            sub_command(str): The subcommand to be passed to the main command
        """

        self.message_body['subcommand'].append(sub_command)

    def set_options(self, option, value=''):
        """Set the option to be passed to the command and subcommand

        Args:
            option(str): The name of the option to be passed
            value(str): The optional value to be passed to the option
        """

        option_pair = (option, value)
        self.message_body['options'].append(option_pair)

    def set_extras(self, option, value):
        """Set the extra options for the message

        Args:
            option(str): The option to be set
            value(str): The value to be stored inside the extra params
        """

        opval = (option, value)
        self.message_body['extras'].append(opval)

    def serialize(self):
        """Serializes the message body for transmission

        Returns:
            JSON
        """

        return json.dumps(self.message_body)
