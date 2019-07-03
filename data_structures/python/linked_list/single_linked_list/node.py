class Node(object):
    def __init__(self, data):
        if data is None:
            raise Exception('data cannot be of NoneType')
        self.data = data
        self.next = None
