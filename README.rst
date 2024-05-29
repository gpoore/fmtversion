=============================================================
``fmtversion``:  Simple version variables for Python packages
=============================================================

:Author: Geoffrey M. Poore
:License: `BSD 3-Clause <http://opensource.org/licenses/BSD-3-Clause>`_

Converts version information into a string ``__version__`` and a namedtuple
``__version_info__`` suitable for Python packages.  The approach is inspired
by PEP 440 and ``sys.version_info``:

* https://www.python.org/dev/peps/pep-0440
* https://docs.python.org/3/library/sys.html

Versions of the form "major.minor.micro" are supported, with an optional,
numbered dev/alpha/beta/candidate/final/post status.  The module does not
support more complicated version numbers like "1.0b2.post345.dev456", since
this does not fit into a namedtuple of the form used by ``sys.version_info``.
The code is written as a single module, so that it may be bundled into
packages, rather than needing to be installed as a separate dependency.

Typical usage in a package's ``version.py`` with a bundled ``fmtversion.py``::

    from .fmtversion import get_version_plus_info
    __version__, __version_info__ = get_version_plus_info(1, 1, 0, 'final', 0)

Following ``sys.version_info``, ``get_version_plus_info()`` takes arguments
for a five-component version number:  major, minor, micro, releaselevel, and
serial.  The releaselevel may be any of dev, alpha, beta, candidate, final, or
post, or common variations/abbreviations thereof.  All arguments but
releaselevel must be convertable to integers.

If only ``__version__`` or ``__version_info__`` is desired, then the functions
``get_version()`` or ``get_version_info()`` may be used instead.  If a micro
version is not needed (``<major>.<minor>.<micro>``), then set the optional
keyword argument ``usemicro=False``.  This will omit a micro version from the
string ``__version__``, while the namedtuple ``__version_info__`` will still
have a field ``micro`` that is set to zero to simplify comparisons.  If each
releaselevel will only have one release, then set ``useserial=False``.  This
will omit a serial number from the string ``__version__``, while the
namedtuple ``__version_info__`` will still have a field ``serial`` that is set
to zero.

A function ``get_version_from_version_py_str()`` is included for extracting
the version from a ``version.py`` file that has been read into a string.  This
is intended for use in ``setup.py`` files.
