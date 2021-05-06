from distutils.core import setup
setup(
  name = 'database_knotinfo',
  packages = ['database_knotinfo'],
  version = '0.3',
  license='GPL',
  description = 'Content of the KnotInfo and LinkInfo databases as lists of dictionaries',
  author = 'Sebastian Oehms',
  author_email = 'seb.oehms@gmail.com',
  url = 'https://github.com/soehms/database_knotinfo',
  download_url = 'https://github.com/soehms/database_knotinfo/archive/pypi-0_3.tar.gz',
  keywords = ['KnotInfo', 'LinkInfo', 'SageMath', 'database'],
  install_requires=[
          'csv',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
  ],
  include_package_data=True
)
