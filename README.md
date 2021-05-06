# Database KnotInfo

This repository contains a snapshot of the complete content of the [KnotInfo](https://knotinfo.math.indiana.edu/) and [LinkInfo](https://linkinfo.sitehost.iu.edu/)  databases in `CSV` format (converted from the corresponding Excel spreadsheets).

It has been created as a part of the [SageMath](https://www.sagemath.org/) interface to theses databases (see Trac ticket [#30352](https://trac.sagemath.org/ticket/30352))  but can also be used independently.

In Python code it can be used in den following way:

```
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

In order to build a new release, the `CSV` files can be upgraded with the `create_knotinfo_csv.py` script.
