# Database KnotInfo

This repository contains a snapshot of the complete content
of the [KnotInfo](https://knotinfo.math.indiana.edu/) and
[LinkInfo](https://linkinfo.sitehost.iu.edu/) databases.
Each database is provided as a Python list of Python dictionaries.
The data are from the corresponding Excel spreadsheets available
on the KnotInfo and LinkInfo homepages on the date of release.

This repository was created as a part of the
[SageMath](https://www.sagemath.org/) interface to these databases
(see Sage Trac ticket [#30352](https://trac.sagemath.org/ticket/30352))
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

### SageMath

Once ticket #30352 is released, the database can be installed in Sage by:

```bash
sage -i database_knotinfo
```

This will contain integration with the knot and link functionality of Sage.
Of course the flat Python functionality is already available by:

```bash
sage -pip install database_knotinfo
```

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
