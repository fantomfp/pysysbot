#!/usr/bin/python
#
# pysysbot - A simple python jabber bot for getting system information
# Copyright (c) 2009 Fabian Affolter <fabian@affolter-engineering.ch>
#
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from distutils.core import setup
from glob import glob

if __name__ == '__main__':
    setup(
        name = 'pysysbot',
        version = "0.0.3",
        description = 'Python based system jabber bot',
        long_description = """This python jabber (XMPP) bot is based on \
            the jabberbot framework (http://thpinfo.com/2007/python-jabberbot/).\
            The bot is capable to display details about the system it \
            is running on. """,
        author = 'Fabian Affolter',
        author_email = 'fabian@affolter-engineering.ch',
        maintainer = 'Fabian Affolter',
        maintainer_email = 'fabian@affolter-engineering.ch',
        url = 'http://www.affolter-engineering.ch/index.php?page=pysysbot',
        license = 'GPLv3+',
        platforms = 'Linux',

        packages = ['pysysbot'],
        package_dir = {'': 'src'},
        scripts = ['pysysbot'],
        data_files = [
            ('share/doc/pysysbot-0.0.3', ['AUTHORS', 'README', 'COPYING', 'ChangeLog']), 
            ('share/man/man1', glob("man/pysysbot.1"))
            ],
         
        keywords = ['Jabber','XMPP','System','python'],
        classifiers = [
                'Development Status :: 0.0.3 - Alpha',
                'Environment :: Console'
                'Intended Audience :: Advanced End Users',
                'Intended Audience :: System Administrators',
                'License :: OSI Approved :: GNU General Public License v3+',
                'Operating System :: POSIX',
                'Programming Language :: Python',
                'Topic :: Jabber',
                'Topic :: XMPP',
                'Topic :: Monitoring'
                ],
    )
