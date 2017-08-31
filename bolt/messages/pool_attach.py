'''
File: pool_attach.py
Description: Subscription manager attach to the specified pool
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 31/08/2017
'''
from base import MessageBase

class PoolAttach(MessageBase):
    """Subscription manager attach to the specified pool

    Implements the pool attach mechanism for subscription manager by constructing
    the appropriate message structure.

    Raises:
        RuntimeError
    """

    def __init__(self, **kwargs):
        """Pool attach constructor

        Keyword Arguments:
            pool_id(str): The id of the pool to which we need to attach
        """

        super(PoolAttach, self).__init__(self.__class__.__name__, self.MESSAGE_TYPE['COMMAND'])
        self.set_command('subscription-manager')
        self.set_subcommand('attach')

        if 'pool_id' not in kwargs.keys():
            raise RuntimeError("One or more required parameters not found")
        self.pool_id = kwargs.get('pool_id')
        self.set_options('pool', self.pool_id)

        self.set_extras('opval_sep', '=')

    def __str__(self):
        """Return the string representation of class
        """

        return "<{} {}>".format(self.__class__.__name__, self.pool_id)
