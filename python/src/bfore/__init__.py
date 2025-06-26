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

            self.EV = f[group]['EV'][...]
            self.ET = f[group]['ET'][...]
            self.VE = f[group]['VE'][...]

    def face_verts(self):

        # Return the face-vertex list

        return np.reshape(self.EV, [self.n_face, 3])-1


class GeoMesh(Mesh):

    def __init__(self, file_name, group='/'):

        Mesh.__init__(self, file_name, 'mesh')

        with h5.File(file_name, 'r') as f:

            type = f[group].attrs['TYPE'].decode('utf-8')

            if type != 'geo_mesh_t':
                raise Exception(f'invalid type: {type}')

            self.VC = f[group]['VC'][...]

    def vert_coords(self):

        # Return the vertex-coordinate list

        return self.VC
