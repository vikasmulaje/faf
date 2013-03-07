from datetime import date

ARCH = [
    'noarch',
    'src',
    'x86_64',
    'i686',
    'i586',
    'i486',
    'i386',
    'ppc',
    'ppc64',
    ]

OPSYS = {
    'Fedora':   [('17',    date(2012, 5, 22)),
                 ('18',    date(2013, 1, 15)),
                 ('devel', None)],

    'RHEL':     [('6',   date(2010, 11, 10)),
                 ('6.1', date(2011, 5, 9)),
                 ('6.2', date(2011, 12, 6)),
                 ('6.3', date(2012, 6, 20)),
                 ('7',   None)],

    'openSUSE': [('11.4', date(2011, 3, 10)),
                 ('12.1', date(2011, 11, 16))]
    }

COMPS = {
    'abrt':
        { 'packages': ['abrt',
                       'abrt-gui',
                       'abrt-tui',
                       'abrt-addon-vmcore',
                       'abrt-addon-xorg',
                       'abrt-addon-ccpp',
                       'abrt-addon-python',
                       'abrt-addon-kerneloops',
                       'abrt-dbus',
                       'abrt-libs',
                       'abrt-python']},
    'libreport':
        { 'packages': ['libreport',
                       'libreport-cli',
                       'libreport-devel',
                       'libreport-web',
                       'libreport-plugin-ureport']},
    'btparser':
        { 'packages': ['btparser',
                       'btparser-devel',
                       'btparser-python']},
    'will-crash':
        { 'packages': ['will-crash']},
    }

_LIBS = ['gtk', 'gdk', 'dbus', 'xul', 'GL', 'jvm', 'freetype']
LIBS = map(lambda x: 'lib%s' % x, _LIBS)

FUNS = dir(__builtins__)
