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

    def __init__(self, message_class):
        """MessageBase constructor

        Initializes the MessageBase with the supported parameters to mark the
        start of the message. The method also initializes the message_body
        structure which needs to be transmitted during the server to client
        communication.

        @message_body: Dictionary type structure encompassing the following keys
        @key command String The command to be executed
        @key subcommand List The list of subcommands that should be passed
        @key options List A list of tuples holding the options and any value passed to them

        Keyword arguments:
        message_class -- The name of the deriving message class
        """

        self.message_class = message_class
        self.message_body = {
            command: '',
            subcommand: [],
            options: []
        }

    def __str__(self):
        """Returns the string type representation of the message class

        @returns String
        """

        error_message = "{} does not implement string representation"
        raise NotImplemedtedError(error_message.format(self.message_class))

    def set_command(self, command):
        """Set the command to be executed

        Keyword arguments:
        command -- The command to be executed
        """

        self.message_body['command'] = command

    def set_subcommand(self, sub_command):
        """Set the subcommand to be passed to the main command

        Keyword arguments:
        sub_command -- The subcommand to be passed to the main command
        """

        self.message_body['subcommand'].append(sub_command)

    def set_options(self, option, value=''):
        """Set the option to be passed to the command and subcommand

        Keyword arguments:
        option -- The name of the option to be passed
        value -- The optional value to be passed to the option
        """

        option_pair = (option, value)
        self.message_body['options'].append(option_pair)

    def serialize(self):
        """Serializes the message body for transmission

        @returns JSON
        """

        return json.dumps(self.message_body)
