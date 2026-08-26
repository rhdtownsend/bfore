# Module  : bfore
# Purpose : Python classes for Fortran mesh_t and geo_mesh_t types

import h5py as h5
import numpy as np
import numpy.ma as ma

__version__ = '0.1+dev'

# Class definitions

class Mesh:

    def __init__(self, file_name, group='/'):

        with h5.File(file_name, 'r') as f:

            type = f[group].attrs[f'TYPE'].decode('utf-8')
            if not (type == 'mesh_t'):
                raise Exception(f'invalid type {type}')

            self.n_vert = f[group].attrs['n_vert']
            self.n_edge = f[group].attrs['n_edge']
            self.n_face = f[group].attrs['n_face']
            self.n_scalar = f[group].attrs['n_scalar']
            self.n_vector = f[group].attrs['n_vector']

            self.EV = f[group]['edge_verts'][...]
            self.ET = f[group]['edge_twins'][...]
            self.VE = f[group]['vert_edges'][...]
            self.VP = f[group]['vert_points'][...]
            self.VS = f[group]['vert_scalars'][...]
            self.VV = f[group]['vert_vectors'][...]

    def face_verts(self):

        # Return the face-vertex array

        return np.reshape(self.EV, [self.n_face, 3])-1

    def vert_points(self):

        # Return the vertex point array

        return self.VP

    def vert_scalars(self, i):

        # Return the i'th vertex scalar array

        return self.VS[:,i]

    def vert_vectors(self, i):

        # Return the i'th vertex vector array

        return self.VV[:,i,:]

#

class Star(Mesh):

    def __init__(self, file_name, group='/'):

        with h5.File(file_name, 'r') as f:

            type = f[group].attrs[f'TYPE'].decode('utf-8')
            if not (type == 'star_t'):
                raise Exception(f'invalid type {type}')

        super().__init__(file_name, f'{group}/mesh_t')

#

class Rbuff:

    def __init__(self, file_name, group='/'):

        with h5.File(file_name, 'r') as f:

            type = f[group].attrs[f'TYPE'].decode('utf-8')
            if type != 'rbuff_t':
                raise Exception(f'invalid type {type}')

            self.n_x = f[group].attrs['n_x']
            self.n_y = f[group].attrs['n_y']
            self.n_scalar = f[group].attrs['n_scalar']
            self.n_vector = f[group].attrs['n_vector']

            PD = f[group]['pixel_depths'][...]
            PT = f[group]['pixel_tags'][...]
            PS = f[group]['pixel_scalars'][...]
            PV = f[group]['pixel_vectors'][...]

        mask = PT == -1

        self.PD = ma.masked_array(PD, mask)
        self.PT = ma.masked_array(PT, mask)

        self.PS = []

        for a in range(self.n_scalar):
            self.PS += [ma.masked_array(PS[:,:,a], mask)]

        mask_vector = np.repeat(np.expand_dims(mask, 2), 3, axis=2)

        self.PV = []

        for a in range(self.n_vector):
            self.PV += [ma.masked_array(PV[:,:,a,:], mask_vector)]

    def pixel_depths(self):

        # Return the pixel depths array

        return self.PD

    def pixel_tags(self):

        # Return the pixel tags array

        return self.PT

    def pixel_scalars(self, a):

        # Return the a'th pixel scalar buffer

        return self.PS[a]

    def pixel_vectors(self, a):

        # Return the a'th pixel vector buffer

        return self.PV[a]

#

class Stream:

    def __init__(self, file_name, group='/'):

        with h5.File(file_name, 'r') as f:

            type = f[group].attrs[f'TYPE'].decode('utf-8')
            if type != 'stream_t':
                raise Exception(f'invalid type {type}')

            self.n = f[group].attrs['n']
            self.n_scalar = f[group].attrs['n_scalar']
            self.n_vector = f[group].attrs['n_vector']

            self.FA = f[group]['frag_areas'][...]
            FS = f[group]['frag_scalars'][...]
            FV = f[group]['frag_vectors'][...]

        self.FS = []

        for a in range(self.n_scalar):
            self.FS += [FS[:,a]]

        self.FV = []

        for a in range(self.n_vector):
            self.FV += [FV[:,:,a]]

    def frag_areas(self):

        # Return the fragment area array

        return self.FA

    def frag_scalars(self, a):

        # Return the a'th fragment scalar array

        return self.FS[a]

    def frag_vectors(self, a):

        # Return the a'th fragment vector array

        return self.FV[a]
