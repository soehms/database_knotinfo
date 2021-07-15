# -*- coding: utf-8 -*-
r"""
Utility to access data from the webpages
`KnotInfo <https://knotinfo.math.indiana.edu/>`__
and `LinkInfo <https://linkinfo.sitehost.iu.edu/>`__
as Python lists of dictionaries.

Many thanks to Chuck Livingston and Allison Moore for their agreement.
For further acknowledgments see the corresponding homepages.
"""

##############################################################################
#       Copyright (C) 2021 Sebastian Oehms <seb.oehms@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  http://www.gnu.org/licenses/
##############################################################################

import os, csv, enum

class Names(enum.Enum):
    r"""
    Enum for constants which are commonly used in
    ``create_knotinfo_csv.py``
    """
    delimiter = '|'
    csv_path = 'csv_data'
    file_knot = 'knotinfo_data_complete'
    file_link = 'linkinfo_data_complete'


def link_list(proper_links=False):
    r"""
    Return the KnotInfo or LinkInfo table as a list of dictionaries.

    INPUT:

    - ``proper_links`` -- boolean (default ``False``) whether to read
      from the KnotInfo (default) or LinkInfo database.

    EXAMPLES::

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
    """
    if proper_links:
        filename = Names.file_link.value
    else:
        filename = Names.file_knot.value
        # filename = file_knot
    filename += '.csv'

    import database_knotinfo
    package_path = database_knotinfo.__path__[0]
    csv_path = os.path.join(package_path, Names.csv_path.value)

    link_csv = open(os.path.join(csv_path, filename))
    link_dict = csv.DictReader(link_csv, delimiter=Names.delimiter.value)
    link_list = list(link_dict)
    link_csv.close()
    return link_list

def version():
    r"""
    Return the current version of the databases.

    EXAMPLES::

        >>> from database_knotinfo import version
        >>> version()
        '21.07.15'
    """
    from database_knotinfo import __version__
    return __version__.value
