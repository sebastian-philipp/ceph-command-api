#!/usr/bin/python
import json
import rados
import sys

def run_command(cluster_handle, cmd):
    return cluster_handle.mon_command(json.dumps(cmd), b'', timeout=5)

header="""
from typing import List
"""

func_template = '''
def {}({}):
    """
    {}
{}
    module={} perm={} flags={}
    """
    prefix = '{}'
    _args = {{'prefix': prefix, {}}} 
'''


class Flags:
    NOFORWARD = (1 << 0)
    OBSOLETE = (1 << 1)
    DEPRECATED = (1 << 2)
    MGR = (1<<3)
    POLL = (1 << 4)
    HIDDEN = (1 << 5)

    VALS = {
        NOFORWARD: 'no_forward',
        OBSOLETE: 'obsolete',
        DEPRECATED: 'deprecated',
        MGR: 'mgr',
        POLL: 'poll',
        HIDDEN: 'hidden',
    }

    def __init__(self, fs):
        self.fs = fs

    def __str__(self):
        keys = Flags.VALS.keys()
        es = {Flags.VALS[k] for k in keys if self.fs & k == k}
        return ', '.join(es)



class Param(object):
    t = {
        'CephInt': 'int',
        'CephString': 'str',
        'CephChoices': 'str',
        'CephPgid': 'str',
        'CephOsdName': 'str',
        'CephPoolname': 'str',
        'CephObjectname': 'str',
        'CephUUID': 'str',
        'CephEntityAddr': 'str',
        'CephIPAddr': 'str',
        'CephName': 'str',
        'CephBool': 'bool',
        'CephFloat': 'float',
    }


    def __init__(self, type, name, who=None, n=None, req=True, **kwargs):
        self.type = type
        self.name = name
        self.who = who
        self.n = n
        self.req = req
        self.kwargs = kwargs

    def safe_name(self):
        unsafe = ['from', 'class', 'id']
        return self.name + '_' if self.name in unsafe else self.name

    def help(self):
        return '    :param {}: {} who={} req={} {}'.format(self.name, self.type, self.who, self.req, str(self.kwargs))

    def mk_default(self):
        if self.req == 'false':
            return '=None'
        return ''

    def mk_type(self):
        inner = Param.t[self.type]
        return 'List[{}]'.format(inner) if self.n == 'N' else inner

    def mk_dict(self):
        return "'{}': {}".format(self.name, self.safe_name())

    def __str__(self):
        return '{}: {}{}'.format(self.safe_name(), self.mk_type(), self.mk_default())

class FuncSig(object):
    def __init__(self, sig, help, module, perm, flags):
        self.sig = [s for s in sig if isinstance(s, basestring)]
        self.params = [Param(**s) for s in sig if not isinstance(s, basestring)]
        self.help = help
        self.module = module
        self.perm = perm
        self.flags = Flags(flags)

    def name(self):
        return '_'.join([e.replace('-', '_') for e in self.sig])

    def prefix(self):
        return ' '.join(self.sig)

    def mk_params(self):
        return ', '.join([str(p) for p in self.params])

    def mk_param_help(self):
        return '\n'.join([f.help() for f in self.params])

    def mk_mk_dict(self):
        return ', '.join([p.mk_dict() for p in self.params])

    def __str__(self):
        return func_template.format(self.name(), self.mk_params(), self.help, self.mk_param_help(), self.module, self.perm, str(self.flags), self.prefix(), self.mk_mk_dict())

def mk_sigs(cluster):
    all = json.loads(run_command(cluster, {"prefix": "get_command_descriptions"})[1])
    #print(all)
    sigs = [FuncSig(**e[1]) for e in all.items()]
    sigs = sorted(sigs, key=lambda f: f.sig)
    print(header)
    print(''.join([str(s) for s in sigs]))

def main(conf):
    cluster = rados.Rados(conffile=conf)
    cluster.connect()
    mk_sigs(cluster)

if __name__ == '__main__':
    main(*sys.argv[1:])
