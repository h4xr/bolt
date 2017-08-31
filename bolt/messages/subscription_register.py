'''
Name: subscription_register.py
Description: Subscription manager registration message
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 29/08/2017
'''
from base import MessageBase

class SubscriptionRegister(MessageBase):
    """Message implementation for calling subscription manager register

    Implements the variable type of subscription manager registration messages
    based on the provided arguments.
    """

    def __init__(self, **kwargs):
        """SubscriptionRegister constructor

        Initializes the message for subscription registration

        Keyword arguments:
            username(str): The username to use for registration
            password(str): The password to use for registration
            environment(str): The name of the environment to attach to
            activation_key(str): The activation key to be used
        """

        super(SubscriptionRegister, self).__init__(self.__class__.__name__, self.MESSAGE_TYPE['COMMAND'])
        self.set_command('subscription-manager')
        self.set_subcommand('register')
        self.set_extras('opval_sep', ' ')

        if 'username' in kwargs.keys():
            self.set_username(kwargs.get('username'))
        if 'password' in kwargs.keys():
            self.set_password(kwargs.get('password'))
        if 'environment' in kwargs.keys():
            self.set_environment(kwargs.get('environment'))
        if 'activation_key' in kwargs.keys():
            self.set_actkey(kwargs.get('activation_key'))

    def __str__(self):
        """Provide a string based representation of the class"""

        return "<subscription-manager register>"

    def set_username(self, username):
        """Set the username for the command

        Args:
            username(str): The username to be set
        """

        self.set_options('username', username)

    def set_password(self, password):
        """Set the password for the command

        Args:
            password(str): The password to be set
        """

        self.set_options('password', password)

    def set_environment(self, environment):
        """Set the environment for the command

        Args:
            environment(str): The environment to be set
        """

        self.set_options('environment', environment)

    def set_actkey(self, act_key):
        """Set the activation key to be used

        Args:
            act_key(str): The activation key to be used
        """

        self.set_options('activationkey', act_key)
