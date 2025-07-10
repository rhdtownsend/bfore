# Module  : bfore
# Purpose : Python classes for Fortran mesh_t and geo_mesh_t types

import h5py as h5
import numpy as np

__version__ = '0.1'

# Class definitions

class Mesh:

    def __init__(self, file_name, group='/'):

        with h5.File(file_name, 'r') as f:

            type = f[group].attrs[f'TYPE'].decode('utf-8')
            if type != 'mesh_t':
                raise Exception(f'invalid type {type}')

            self.n_vert = f[group].attrs['n_vert']
            self.n_edge = f[group].attrs['n_edge']
            self.n_face = f[group].attrs['n_face']

            self.EV = f[group]['edge_verts'][...]
            self.ET = f[group]['edge_twins'][...]
            self.VE = f[group]['vert_edges'][...]
            self.VP = f[group]['vert_points'][...]
            self.VS = f[group]['vert_scalars'][...]
            self.VV = f[group]['vert_vectors'][...]

    def face_verts(self):

        # Return the face-vertex list

        return np.reshape(self.EV, [self.n_face, 3])-1

    def vert_points(self):

        # Return the vertex-point list

        return self.VP

    def vert_scalars(self, i):

        # Return the i'th vertex-scalar list

        return self.VS[:,i]

    def vert_vectors(self, i):

        # Return the i'th vertex-vector list

        return self.VV[:,i,:]

#
    
class Renderbuff:

    def __init__(self, file_name, group='/'):

        with h5.File(file_name, 'r') as f:

            type = f[group].attrs[f'TYPE'].decode('utf-8')
            if type != 'renderbuff_t':
                raise Exception(f'invalid type {type}')

            self.PD = f[group]['pixel_depths'][...]
            self.PT = f[group]['pixel_tags'][...]
            self.PS = f[group]['pixel_scalars'][...]
            self.PV = f[group]['pixel_vectors'][...]

    def pixel_depths(self):

        # Return the pixel-depths buffer

        return self.PD

    def pixel_tags(self):

        # Return the pixel-tags buffer

        return self.PT

    def pixel_scalars(self, a):

        # Return the a'th pixel-scalar buffer

        return self.PS[:,:,a]

    def pixel_vectors(self, a):

        # Return the a'th pixel-vector buffer

        return self.PV[:,:,a,:]
