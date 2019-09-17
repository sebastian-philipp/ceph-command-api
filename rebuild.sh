#!/usr/bin/env bash

set -e

# This file expects a Ceph build environment in ../ceph.
# If you don't have it, then rebuild.py just expects a running cluster.

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
: ${CEPH_BUILD_DIR:=$script_dir/../ceph/build}

. venv/bin/activate
. $CEPH_BUILD_DIR/vstart_environment.sh


python rebuild.py $CEPH_BUILD_DIR/ceph.conf

python setup.py test
python setup.py build_sphinx
