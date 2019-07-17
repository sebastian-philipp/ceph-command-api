ceph-command-api
================


`ceph-command-api`. An automatically generated reference.

Usage
-----

```python
import rados
from ceph_command_api import MonCommandApi
cluster = rados.Rados(conffile='/etc/ceph/ceph.conf')
cluster.connect()
print(MonCommandApi(cluster).version())
```   

Reference
---------

See [cholcombe973/ceph_command_parser](https://github.com/cholcombe973/ceph_command_parser) for a 
similar project.