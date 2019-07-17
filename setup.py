from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ceph-command-api',
    version='1.0.0',
    packages=['ceph_command_api'],
    url='https://github.com/sebastian-philipp/ceph-command-api',
    license='',
    author='Sebastian Wagner',
    author_email='sebastian.wagner@suse.com',
    description='Automatically generated command API. ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developer',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        "Operating System :: OS Independent",
    ]
)
