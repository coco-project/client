from bunch import bunchify
from slumber import API
from slumber.serialize import JsonSerializer, Serializer


class HttpClient(API):

    """
    Client to communicate with a coco core application's HTTP API.

    Using this client is the recommended method to speak with the coco app.

    Example usage:

    ```
    from coco.client.clients import HttpClient

    client = HttpClient("http://coco.api", auth=("user", "password"))

    containers = client.containers.get()  # get all containers
    for container in containers:
        client.containers(container.id).restart().post()  # restart each container
    ```
    """

    def __init__(self, base_url=None, auth=None):
        """
        Initialize a new client to communicate with the remote HTTP API.

        :link https://github.com/samgiles/slumber/blob/master/slumber/__init__.py#L196
        """
        super(HttpClient, self).__init__(
            base_url,
            auth,
            append_slash=False,
            serializer=Serializer(serializers=[BunchSerializer()])
        )


class BunchSerializer(JsonSerializer):

    """
    Custom serializer for `slumber` de-/serializing to `Bunch` objects.
    """

    def loads(self, data):
        """
        :inherit.
        """
        loaded = super(BunchSerializer, self).loads(data)
        if isinstance(loaded, list):
            loaded = [bunchify(record) for record in loaded]
        elif isinstance(loaded, dict):
            loaded = bunchify(loaded)
        return loaded
