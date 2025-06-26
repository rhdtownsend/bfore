# File     : Makefile
# Purpose  : makefile for build subdir

# Targets

LIB_TARGETS = 

INC_FILES = 

ifeq ($(UTESTS),yes)
   BIN_TARGETS += utest_mesh utest_geo_mesh
endif

# Source file lists & related variables
#
# xxx_SRCS = source files required to compile xxx
# xxx_USES = source files providing modules USE'd by xxx
# xxx_LIBS = library files required to link xxx

mesh_SRCS = mesh_m.fypp mesh_construct_sm.fypp mesh_modify_sm.fypp \
            mesh_topology_sm.fypp mesh_primitives_m.fypp mesh_io_sm.fypp \
           stat_m.fypp file_m.fypp
geo_mesh_SRCS = $(mesh_SRCS) geo_mesh_primitives_sm.fypp geo_mesh_m.fypp \
                geo_mesh_construct_sm.fypp geo_mesh_modify_sm.fypp geo_mesh_io_sm.fypp

utest_mesh_SRCS = utest_mesh.fypp $(mesh_SRCS)
utest_mesh_USES = $(utest_mesh_SRCS)
utest_mesh_LIBS = 

utest_geo_mesh_SRCS = utest_geo_mesh.fypp $(geo_mesh_SRCS)
utest_geo_mesh_USES = $(utest_geo_mesh_SRCS)
utest_geo_mesh_LIBS = 

# Build flags

FFLAGS = -I$(FORUM_INC_DIR)

FPPFLAGS = -I$(FORUM_INC_DIR)

LDFLAGS = `lapack_link` `hdf5_link` `lapack95_link` `odepack_link` -L$(FORUM_LIB_DIR) -lforum

# Include standard rules

include Make.inc

# Target for linting

linter :
	fortitude check \
            --ignore M011 \
            --ignore S001 \
            --ignore E001 \
            --ignore T041 \
            --file-extensions=f90

.PHONY: linter
