#####
BFORE
#####

BFORE (pronounced as 'before') is an open-source software package for
modelling the variability of stars and other opaque astrophysical
objects. It represents the object surface using a triangle-based mesh,
which is perturbed to account for the effects of oscillations, tides,
spots, etc. The observer-visible surface of the object is determined
by rendering the mesh into a pixel-based buffer. The resulting
ensemble of non-empty pixels, each specifying surface properties such
as temperature, orientation and composition, provides the basis for
synthesizing disk-integrated spectra, photometric colors and related
information for the object.

BFORE is free software: you can redistribute it and/or modify it under
the terms of the `GNU General Public License
<http://www.gnu.org/licenses/gpl-3.0.html>`__ published by the `Free
Software Foundation <https://www.fsf.org/>`__, version 3.

.. toctree::
   :caption: User Guide
   :name: user-guide
   :maxdepth: 2

   user-guide/preliminaries.rst
   user-guide/quick-start.rst
