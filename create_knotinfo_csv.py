#!/usr/bin/python
# -*- coding: utf-8 -*-

r"""
Python script to create the source for the ``database_knotinfo`` package
in ``csv`` format in the given path. This utility should be used to switch
to a new version of the data files if the original files on the KnotInfo
or LinkInfo webpage have changed.

.. NOTE::

    This function requires the Python packages ``pandas``, ``xlrd`` and
    ``xlsx2csv``. If necessary, install them by running::

        pip install pandas
        pip install xlrd
        pip install xlsx2csv

    before using this function.

INPUT:

- ``path`` -- what path the data should be downloaded to
  (if not provided, the current working directory is used)

EXAMPLES::

    database_knotinfo $ ls
    create_knotinfo_csv.py  README.md

    database_knotinfo $ ./create_knotinfo_csv.py
    database_knotinfo $ ls
    create_knotinfo_csv.py  README.md csv_data
    database_knotinfo $ ls csv_data
    knotinfo_data_complete.csv  linkinfo_data_complete.csv

    database_knotinfo $ ./create_knotinfo_csv.py
    mv: das Verschieben
    von '.../database_knotinfo/special_knotinfo_spkg_temp_dir/csv_data'
    nach '.../database_knotinfo/csv_data' ist nicht möglich:
    Das Verzeichnis ist nicht leer
    database_knotinfo $ ls
    create_knotinfo_csv.py  README.md  csv_data
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

import sys, os
from xlsx2csv import Xlsx2csv
from pandas import read_excel
from database_knotinfo import Names

cmdline_args = sys.argv[1:]

path = None

if len(cmdline_args) > 0:
    path = cmdline_args[0]
    if not os.path.exists(path):
        raise ValueError("the path '%s' does not exist" % path)

if not path:
    pwd = os.environ['PWD']
    path = os.path.join(pwd, 'database_knotinfo')
    if not os.path.exists(path):
        path = pwd

path_temp = os.path.join(path, 'special_knotinfo_temp_dir')
path_temp_csv_data = os.path.join(path_temp, Names.csv_path.value)
path_csv_data      = os.path.join(path,      Names.csv_path.value)
os.makedirs(path_temp)
os.makedirs(path_temp_csv_data)

def convert(path_temp_csv_data, url, filename, reader):
    r"""
    Download a data file in xls or xslx format and convert it to csv.
    """
    if reader == Xlsx2csv:
        excel = filename + '.xlsx'
    else:
        excel = filename + '.xls'
    csv = filename + '.csv'
    inp = os.path.join(url, excel)
    out = os.path.join(path_temp_csv_data, csv)
    if reader == Xlsx2csv:
        temp_file = os.path.join(path_temp, 'temp.xlsx')
        os.system('wget -O %s %s' %(temp_file, inp))
        data = reader(temp_file,
                      delimiter=Names.delimiter.value,
                      skip_empty_lines=True)
        data.convert(out)
    else:
        data = reader(inp)
        data.to_csv(out, sep=Names.delimiter.value, index=False)

# first KnotInfo (using pandas and xlrd)
convert(path_temp_csv_data,
        'https://knotinfo.math.indiana.edu/',
        Names.file_knot.value,
        read_excel)

# now LinkInfo (using xlsx2csv)
convert(path_temp_csv_data,
        'https://linkinfo.sitehost.iu.edu/',
        Names.file_link.value,
        Xlsx2csv)

os.system('rm -rf %s;mv %s %s; rm -rf %s' % (path_csv_data, path_temp_csv_data, path, path_temp))
