#####
BFORE
#####

.. image:: https://img.shields.io/github/license/rhdtownsend/bfore
   :alt: GitHub
   :target: https://github.com/rhdtownsend/bfore/blob/master/COPYING
.. image:: https://img.shields.io/github/v/release/rhdtownsend/bfore
   :alt: GitHub release (latest by date)
   :target: https://github.com/rhdtownsend/bfore/releases/latest
.. image:: https://img.shields.io/github/issues/rhdtownsend/bfore
   :alt: GitHub issues
   :target: https://github.com/rhdtownsend/bfore/issues
.. image:: https://img.shields.io/readthedocs/bfore
   :alt: Read the Docs
   :target: https://bfore.readthedocs.io/en/latest

Overview
========

BFORE (pronounced as ‘before’) is an open-source software package for
modelling the variability of stars and other opaque astrophysical
objects. It represents the object surface using a triangle-based mesh,
which is perturbed to account for the effects of oscillations, tides,
spots, etc. The observer-visible surface of the object is determined
by rendering the mesh into a pixel-based buffer. The resulting
ensemble of non-empty pixels, each specifying surface properties such
as temperature, orientation and composition, provides the basis for
synthesizing disk-integrated spectra, photometric colors and related
information for the object.

Documentation
=============

Full documentation for BFORE can be found at
https://bfore.readthedocs.io/en/latest.
