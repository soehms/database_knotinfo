# Database KnotInfo

This repository contains a snapshot of the complete content
of the [KnotInfo](https://knotinfo.math.indiana.edu/) and
[LinkInfo](https://linkinfo.sitehost.iu.edu/) databases.
Each database is provided as a Python list of Python dictionaries.
The data are from the corresponding Excel spreadsheets available
on the KnotInfo and LinkInfo homepages on the date of release.

This repository was created as a part of the
[SageMath](https://www.sagemath.org/) interface to these databases
(see the [corresponding section](https://doc.sagemath.org/html/en/reference/knots/sage/knots/knotinfo.html)
of the SageMath reference manual or [this tutorial](tutorials/sage_knotinfo_interface_tutorial.ipynb))
but can also be used independently.

In Python, it can be used as follows:

```python
>>> from database_knotinfo import link_list
>>> k = link_list()
>>> len(k)
2979
>>> names_k = k[0]
>>> type(names_k)
<type 'dict'>
>>> names_k['braid_index']
'Braid Index'
>>> k2 = k[2]
>>> k2['name']
'3_1'
>>> k2['braid_index']
'2'
>>> k2['homfly_polynomial']
'(2*v^2-v^4)+(v^2)*z^2'

>>> l = link_list(proper_links=True)
>>> len(l)
4189
>>> names_l = l[0]
>>> type(names_l)
<type 'dict'>
>>> names_l['braid_notation']
'Braid Notation'
>>> l2 = l[2]
>>> l2['name']
'L2a1{1}'
>>> l2['homflypt_polynomial']
'v/z-v^3/z + v*z'
```

To build a new release, the `CSV` files can be upgraded with the
`create_knotinfo_csv.py` script. A [cronjob](https://github.com/soehms/database_knotinfo/blob/main/.github/workflows/check_version_changed.yml)
executes it on the first day of every month and creates a new
release if differences are detected.

## Installation

### Python

```bash
pip install database_knotinfo
```

or

```bash
pip install database_knotinfo==2021.9.1
```

if you want to install a former version.


### SageMath

Since Release 9.4, the database can be installed in Sage by:

```bash
sage -i database_knotinfo
```

This will contain integration with the knot and link functionality of Sage.
Sage 9.4 ships the PyPI release [0.7](https://pypi.org/project/database-knotinfo/0.7/)
of the database. To use a more recent one you have to execute

```bash
sage -package update database_knotinfo <version>
```

before the installation command above, for example:

```bash
sage -package update database_knotinfo 2021.9.1
```

This procedure can be used to upgrade to the next version, as well. But note
that there is a bug in 9.4 concerning such upgrades which will be fixed in
SageMath 9.5 (see Trac ticket [#32099](https://trac.sagemath.org/ticket/32099)).
A workaround for 9.4 can be perfomed in a Sage session as follows:

```
sage: from sage.databases.knotinfo_db import KnotInfoDataBase
sage: KnotInfoDataBase().reset_filecache()
```

If you upgrade to a version of the database which is ahead of the version the
SageMath release is build on, you should keep in mind, that the examples shown
in the Sage reference manual may be outdated.

In case the installation via `sage -i` is failing on your system you can try:

```bash
sage -pip install database_knotinfo
```

or

```bash
sage -pip install database_knotinfo==0.7
```

for the version compatible the the current Sage release.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/soehms/database_knotinfo)



## Versioning

Version numbers are automatically generated every month if differences to the
original databases are detected. They follow the scheme

\<year\>.\<month\>.\<day\>

## Help

If you note a divergence between this repository and the original data in case
the current release is older than a month please create an issue about that.

## Credits

Many thanks to Chuck Livingston and Allison Moore for making the data
available. For further acknowledgments see the corresponding homepages.
