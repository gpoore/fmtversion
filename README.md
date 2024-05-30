# `fmtversion`:  Simple version variables for Python packages

Converts version information into a string `__version__` and a named tuple
`__version_info__` suitable for Python packages.  The approach is inspired
by PEP 440 and `sys.version_info`:

  * https://www.python.org/dev/peps/pep-0440

  * https://docs.python.org/3/library/sys.html

Versions of the form "major.minor.micro" are supported, with an optional,
numbered dev/alpha/beta/candidate/final/post status.  The module does not
support more complicated version numbers like "1.0b2.post345.dev456", since
this does not fit into a named tuple of the form used by `sys.version_info`.
The code is written as a single module, so that it may be bundled into
packages, rather than needing to be installed as a separate dependency.

Typical usage in a package's `version.py` with a bundled `fmtversion.py`:

```
from .fmtversion import get_version_plus_info
__version__, __version_info__ = get_version_plus_info(1, 2, 0, 'final', 0)
```

Following `sys.version_info`, `get_version_plus_info()` takes arguments
for a five-component version number:  major, minor, micro, release level, and
serial.  The release level may be any of dev, alpha, beta, candidate, final, or
post, or common variations/abbreviations thereof.  All arguments but
release level must be convertable to integers.

If only `__version__` or `__version_info__` is desired, then the functions
`get_version()` or `get_version_info()` may be used instead.  If a micro
version is not needed (`<major>.<minor>.<micro>`), then set the optional
keyword argument `usemicro=False`.  This will omit a micro version from the
string `__version__`, while the named tuple `__version_info__` will still
have a field `micro` that is set to zero to simplify comparisons.  If each
release level will only have one release, then set `useserial=False`.  This
will omit a serial number from the string `__version__`, while the
named tuple `__version_info__` will still have a field `serial` that is set
to zero.


## License

BSD 3-Clause License

Copyright (c) 2015-2024, Geoffrey M. Poore
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
