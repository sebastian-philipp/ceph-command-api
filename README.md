ceph-command-api
================


`ceph-command-api`. An automatically generated API for accessing the Ceph CLI.

It provides proper auto completion in your IDE, an automatically
[generated documentation](https://ceph-command-api.readthedocs.io/en/latest/mon_command_api.html)
, and static type checking. 


Usage
-----

Install [`ceph-command-api`](https://pypi.org/project/ceph-command-api/) from PyPi:

```
pip install ceph-command-api
```

And then:

```python
import rados
from ceph_command_api import MonCommandApi
cluster = rados.Rados(conffile='/etc/ceph/ceph.conf')
cluster.connect()
print(MonCommandApi(cluster).version())
```   

Rebuild the API
---------------

See `./rebuild.sh`

Reference
---------

See [cholcombe973/ceph_command_parser](https://github.com/cholcombe973/ceph_command_parser) for a 
similar project.