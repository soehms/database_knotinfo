# -*- coding: utf-8 -*-


import os, csv, enum

class Names(enum.Enum):
    r"""
    Enum for constants which are commonly used in
    create_knotinfo_csv.py
    """
    delimiter      = '|'
    csv_path       = 'csv_data'
    file_knot      = 'knotinfo_data_complete'
    file_link      = 'linkinfo_data_complete'


def link_list(proper_links=False):
    r"""
    Return the KnotInfo and LinkInfo tables as Python dictionary.

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

    path_dirs = __file__.split('/')
    package_path = path_dirs[len(path_dirs)-2]
    csv_path     = os.path.join(package_path, Names.csv_path.value)

    link_csv = open(os.path.join(csv_path, filename))
    link_dict = csv.DictReader(link_csv, delimiter=Names.delimiter.value)
    link_list = list(link_dict)
    link_csv.close()
    return link_list
