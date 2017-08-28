'''
File: pub_server.py
Description: Provides the ZMQ based publishing server for bolt
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 28/08/2017
'''
import time
import zmq

class Server(object):
    '''Publisher server for Bolt

    Provides mechanism for setting up a message publishing server for bolt
    through which the system can publish messages provided the topic and message
    format.
    '''

    def __init__(self, host, port):
        """Server constructor

        Sets up the Server to listen on the provided host and port combination.
        Currently, only tcp based connection is allowed.

        Keyword arguments:
        host -- The host on which to setup the socket
        port -- The port on which to publish the messages
        """

        self.host = host
        self.port = port

        self.protocol = 'tcp'
        self.setup()

    def setup(self):
        """Setup the ZMQ connection

        Initiates the ZMQ connection using the provided parameters
        """

        connection_string = "{}://{}:{}".format(self.protocol, self.host, self.port)
        self.zmq_context = zmq.Context()
        self.zmq_socket = self.zmq_context.socket(zmq.PUB)
        self.zmq_socket.bind(connection_string)

    def disconnect(self):
        """Close the ZMQ connection running on the port"""

        if not self.zmq_socket:
            raise Exception("Unable to find an active ZMQ connection")
        self.zmq_socket.close()

    def message(self, topic, body):
        """Send a ZeroMQ message

        Publishes a message provided the topic and body. The serialization of
        the message is the responsibility of the calling method.

        Keyword arguments:
        topic -- The topic to be used for publishing
        body -- The message body to be transmitted
        """

        message = self._prep_message(topic, body)
        self.zmq_socket.send(message)

    def _prep_message(self, topic, body):
        """Prepares a ZeroMQ message for sending

        Keyword arguments:
        topic -- The topic on which message should be published
        body -- The body of the message

        Returns: String
        """

        return "{}: {}".format(topic, body)
