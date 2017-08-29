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
        """

        super(SubscriptionRegister, self).__init__(self.__class__.__name__)
        self.set_command('subscription-manager')
        self.set_subcommand('register')
        self.set_extras('option_renderer:=')
