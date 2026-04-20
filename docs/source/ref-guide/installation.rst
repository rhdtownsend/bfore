.. _installation:

************
Installation
************

This chapter discusses BFORE installation in detail. If you just want
to get up and running, have a look at the :ref:`quick-start` chapter.

Pre-Requisites
==============

To compile and run BFORE, you'll need the following software
components:

* A modern (2003+) Fortran compiler
* The :netlib:`BLAS <blas>` linear algebra library
* The :netlib:`LAPACK <lapack>` linear algebra library
* The :netlib:`LAPACK95 <lapack95>` Fortran 95 interface to LAPACK
* The `HDF5 <https://www.hdfgroup.org/solutions/hdf5/>`__ data management library
* The `crlibm <https://hal-ens-lyon.archives-ouvertes.fr/ensl-01529804>`__ correctly rounded math library
* The :git:`crmath <rhdtownsend/crmath>` Fortran 2003 interface to crlibm
* The :git:`fypp <aradi/fypp>` Fortran preprocessor
* The :git:`toml-f <toml-f/toml-f>` Fortran TOML parser

On Linux and MacOS platforms, all of these components are bundled
together in the MESA Software Development Kit (SDK), which can be
downloaded from the `MESA SDK <mesa-sdk_>`__ homepage. Using this SDK
is strongly recommended.

Building BFORE
==============

.. _install-download:

Download
--------

Download the `BFORE source code <tarball_url_>`__, and unpack it
from the command line using the :command:`tar` utility:

.. code-block:: console
   :substitutions:

   $ tar xf |tarball|

Set the :envvar:`BFORE_DIR` environment variable with the path to the
newly created source directory; this can be achieved, e.g., using the
:command:`realpath` command\ [#realpath]_:

.. code-block:: console
   :substitutions:

   $ export BFORE_DIR=$(realpath |dist_dir|)

.. _install-compile:

Compile
-------

Compile and install BFORE using the :command:`make` utility:

.. code-block:: console

   $ make -j -C $BFORE_DIR

(the :command:`-j` flags tells :command:`make` to use multiple cores, speeding up the build).

Test
----

To check that BFORE has compiled correctly and gives reasonable
results, you can run the unit tests via the command

.. code-block:: console

   $ make -C $BFORE_DIR utest

The initial output from the tests should look something like this:

.. literalinclude:: installation/make-utest.out
   :language: console
   :lines: 1-10

Custom Builds
=============

Custom builds of BFORE can be created by setting certain environment
variables to the value ``yes``. The following variables are currently
supported:

.. envvar:: EXTERNAL_FORUM

   Link against an external :git:`ForUM <rhdtownsend/forum>` library
   (default ``no``).  If set to ``yes``, then you must ensure that the
   :file:`forum.pc` package file can be found by the
   :command:`pkgconf` utility (for instance, by setting the
   :envvar:`PKG_CONFIG_PATH` environment variable)

.. envvar:: EXTERNAL_MSG

   Link against an external :git:`MSG <rhdtownsend/msg>` library
   (default ``no``).  If set to ``yes``, then you must ensure that the
   :file:`msg.pc` package file can be found by the
   :command:`pkgconf` utility (for instance, by setting the
   :envvar:`PKG_CONFIG_PATH` environment variable)

.. envvar:: DEBUG

   Enable debugging mode (default ``no``)

.. envvar:: SHARED

   Build shared libraries in addition to static ones (default ``yes``)

.. envvar:: OMP

   Enable OpenMP parallelization (default ``yes``)

.. envvar:: FPE

   Enable floating point exception checks (default ``yes``)

.. envvar:: UTESTS

   Build unit tests (default ``yes``)

If an environment variable is not set, then its default value is
assumed. The default values can be altered by editing the file
:file:`{$BFORE_DIR}/Makefile`.

Git Access
==========

Sometimes, you'll want to try out new features in BFORE that haven't
yet made it into a formal release. In such cases, you can check out
BFORE directly from the :git:`rhdtownsend/bfore <rhdtownsend/bfore>` git
repository on :git:`GitHub <>`:

.. code-block:: console

   $ git clone --recurse-submodules https://github.com/rhdtownsend/bfore.git

However, a word of caution: BFORE is under constant development, and
features in the main (``main``) branch can change without warning.

.. rubric:: footnote

.. [#realpath] The :command:`realpath` command is included in the GNU
               `CoreUtils <https://www.gnu.org/software/coreutils/>`__
               package. Mac OS users can install CoreUtils using
               `MacPorts <https://www.macports.org/>`__ or `Homebrew
               <https://brew.sh/>`__.
