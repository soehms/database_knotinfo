from setuptools import setup
setup(
  name = 'database_knotinfo',
  packages = ['database_knotinfo'],
  license='GPL',
  description = 'Content of the KnotInfo and LinkInfo databases as lists of dictionaries',
  author = 'Sebastian Oehms',
  author_email = 'seb.oehms@gmail.com',
  url = 'https://github.com/soehms/database_knotinfo',
  keywords = ['KnotInfo', 'LinkInfo', 'SageMath', 'database'],
  install_requires=[
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
  use_scm_version=True,
  setup_requires=['setuptools_scm'],
)
