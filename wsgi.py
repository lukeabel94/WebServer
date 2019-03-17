import socket
import io
import sys

# following https://ruslanspivak.com/lsbaws-part2/

class WSGIServer(object):

    address_family = socket.AF_INET