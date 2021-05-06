#!/usr/bin/python
# -*- coding: utf-8 -*-

r"""
Python script to create the source for the sage-package ``database_knotinfo``
in ``csv`` format in the given path. This utility should be used in case of a
 switch to a new version of the data files (that is if the original files on the
KnotInfo LinkInfo web-page have changed).

..NOTE::

    This function demands the Python package ``pandas``, ``xlrd`` and
    ``xlsx2csv`` to be installed. If not you have to run::

        pip install pandas
        pip install xlrd
        pip install xlsx2csv

    before using this function.

INPUT:

- ``path`` -- string of the path where the tarball should be stored
  (by default ``pwd``)

EXAMPLES::

    database_knotinfo $ ls
    create_knotinfo_csv.py  README.md

    database_knotinfo $ ./create_knotinfo_csv.py
    database_knotinfo $ ls
    create_knotinfo_csv.py  README.md csv_data
    database_knotinfo $ ls csv_data
    knotinfo_data_complete.csv  linkinfo_data_complete.csv

    database_knotinfo $ ./create_knotinfo_csv.py
    mv: das Verschieben von '.../database_knotinfo/special_knotinfo_spkg_temp_dir/csv_data' nach '.../database_knotinfo/csv_data' ist nicht möglich: Das Verzeichnis ist nicht leer
    database_knotinfo $ ls
    create_knotinfo_csv.py  README.md  csv_data
"""

import sys, os
from xlsx2csv import Xlsx2csv
from pandas import read_excel
from database_knotinfo import Names

##############################################################################
#       Copyright (C) 2021 Sebastian Oehms <seb.oehms@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  http://www.gnu.org/licenses/
##############################################################################


cmdline_args = sys.argv[1:]

path    = None

if len(cmdline_args) > 0:
    path = cmdline_args[0]

if not path:
    path = os.environ['PWD']

path_temp = os.path.join(path, 'special_knotinfo_temp_dir')
path_csv_data = os.path.join(path_temp, Names.csv_path.value)
os.makedirs(path_temp)
os.makedirs(path_csv_data)

def convert(path_csv_data, url, filen, reader):
    if reader == Xlsx2csv:
        excel = filen + '.xlsx'
    else:
        excel = filen + '.xls'
    csv   = filen + '.csv'
    inp   = os.path.join(url,      excel)
    out   = os.path.join(path_csv_data, csv)
    if reader == Xlsx2csv:
        from six.moves.urllib.request import urlopen
        f = urlopen(inp)
        url_data = f.read()
        temp_file = os.path.join(path_temp, 'temp.xlsx')
        f = open(temp_file, 'wt')
        f.write(url_data)
        f.close()
        data = reader(temp_file, delimiter=Names.delimiter.value, skip_empty_lines=True)
        data.convert(out)
    else:
        data = reader(inp)
        data.to_csv(out, sep=Names.delimiter.value, index=False)

# first KnotInfo (using pandas and xlrd)
convert(path_csv_data, 'https://knotinfo.math.indiana.edu/', Names.file_knot.value, read_excel)

# now LinkInfo (using xlsx2csv)
convert(path_csv_data, 'https://linkinfo.sitehost.iu.edu/', Names.file_link.value, Xlsx2csv)

os.system('mv %s %s; rm -rf %s' %(path_csv_data, path, path_temp))
