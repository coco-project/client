# ipynbsrv-client

> Client package to communicate with the ipynbsrv core API.

## Usage

```python
from ipynbsrv.client.clients import HttpClient

# initialize the client
client = HttpClient("http://ipynbsrv.api", auth=("user", "password"))

# work on existing resources
containers = client.containers.get()
for container in containers:
    client.containers(container.id).restart().post()

# create new records
share = client.shares.post({
    'name': 'my-share',
    'description': 'sharing is caring'
})

...
```