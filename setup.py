from setuptools import setup
from sphinx.setup_command import BuildDoc
cmdclass = {'build_sphinx': BuildDoc}

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '1.0'
release = '1.0.0'

setup(
    name='ceph-command-api',
    version=release,
    packages=['ceph_command_api'],
    url='https://github.com/sebastian-philipp/ceph-command-api',
    license='',
    author='Sebastian Wagner',
    author_email='sebastian.wagner@suse.com',
    description='Automatically generated command API. ',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        "Operating System :: OS Independent",
    ],
    cmdclass=cmdclass,
    command_options={
        'build_sphinx': {
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docs/source')}},
)

