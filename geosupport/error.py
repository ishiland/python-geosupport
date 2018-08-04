class GeosupportError(Exception):
    def __init__(self, message, result={}):
        super(GeosupportError, self).__init__(message)
        self.result = result
