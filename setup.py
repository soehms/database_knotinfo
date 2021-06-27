from setuptools import setup

package_name = 'database_knotinfo'

def local_scheme(version):
    return ""

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name=package_name,
  packages=[package_name],
  package_dir={package_name: package_name},
  package_data={package_name: ['cvs_data/knotinfo_data_complete.csv',
                               'cvs_data/linkinfo_data_complete.csv']},
  license='GPL',
  description='The KnotInfo and LinkInfo databases as lists of dictionaries',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Sebastian Oehms',
  author_email='seb.oehms@gmail.com',
  url='https://github.com/soehms/database_knotinfo',
  keywords=['KnotInfo', 'LinkInfo', 'SageMath', 'database', 'knot', 'link',
            'mathematics', 'topology', 'invariants'],
  install_requires=[],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',
    # Whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
  ],
  include_package_data=True,
  use_scm_version={"local_scheme": local_scheme},
  setup_requires=['setuptools_scm'],
)
