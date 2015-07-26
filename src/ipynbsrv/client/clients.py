import slumber


class HttpClient(slumber.API):

    """
    Client to communicate with an ipynbsrv core application's HTTP API.

    Using this client is the recommended method to speak with the ipynbsrv app.
    """

    def __init__(self, base_url=None, auth=None, format=None, append_slash=False, session=None, serializer=None):
        """
        Initialize a new client to communicate with the remote HTTP API.

        :link https://github.com/samgiles/slumber/blob/master/slumber/__init__.py#L196
        """
        super(HttpClient, self).__init__(base_url, auth, format, append_slash, session, serializer)
