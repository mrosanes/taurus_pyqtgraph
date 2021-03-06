#!/usr/bin/env python

##############################################################################
##
# This file is part of Taurus
##
# http://taurus-scada.org
##
# Copyright 2011 CELLS / ALBA Synchrotron, Bellaterra, Spain
##
# Taurus is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
##
# Taurus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
##
# You should have received a copy of the GNU Lesser General Public License
# along with Taurus.  If not, see <http://www.gnu.org/licenses/>.
##
##############################################################################

from setuptools import setup, find_packages

# Do not modify the __version manually. To be modified by bumpversion
__version = '0.1.1-alpha'

description = 'Taurus extension providing pyqtgraph-based widgets'

long_description = '''taurus_pyqtgraph is an extension for the Taurus package. 
It adds the taurus.qt.qtgui.tpg submodule which provides pyqtgraph-based 
widgets.'''

author = 'Taurus Community',

maintainer = author,

maintainer_email = 'tauruslib-devel@lists.sourceforge.net',

url = 'http://github.com/taurus-org/taurus_pyqtgraph',

download_url = url,

platforms = ['Linux', 'Windows']

keywords = ['Taurus', 'pyqtgraph', 'plugin', 'widgets']

install_requires = [
    'taurus>=4.5.2',
    'taurus[taurus-qt]',
    'pyqtgraph',
]

entry_points = {
    'taurus.qt.qtgui': ['tpg = taurus_pyqtgraph',],
}

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: X11 Applications :: Qt',
    'Environment :: Win32 (MS Windows)',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: User Interfaces',
    'Topic :: Software Development :: Widget Sets',
]


setup(name='taurus_pyqtgraph',
      version=__version,
      description=description,
      long_description=long_description,
      author=author,
      maintainer=maintainer,
      maintainer_email=maintainer_email,
      url=url,
      download_url=download_url,
      platforms=platforms,
      license='LGPL',
      keywords=keywords,
      packages=find_packages(),
      classifiers=classifiers,
      include_package_data=True,
      entry_points=entry_points,
      install_requires=install_requires,
      )
