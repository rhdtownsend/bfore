# File     : Makefile
# Purpose  : makefile for build subdir

# Default rule in case make is invoked in current dir

all:
	make -C ..

# Targets

LIB_TARGETS = 

INC_FILES = 

ifeq ($(UTESTS),yes)
   BIN_TARGETS += utest_mesh utest_renderbuff
endif

# Source file lists & related variables
#
# xxx_SRCS = source files required to compile xxx
# xxx_USES = source files providing modules USE'd by xxx
# xxx_LIBS = library files required to link xxx

point_SRCS = point_m.fypp point_operate_sm.fypp point_transform_sm.fypp point_array_sm.fypp
vector_SRCS = vector_m.fypp vector_operate_sm.fypp vector_transform_sm.fypp vector_array_sm.fypp
mesh_SRCS = mesh_m.fypp mesh_construct_sm.fypp mesh_operate_sm.fypp mesh_modify_sm.fypp mesh_traverse_sm.fypp \
            mesh_vert_sm.fypp mesh_face_sm.fypp mesh_topology_sm.fypp mesh_io_sm.fypp mesh_primitives_m.fypp
renderbuff_SRCS = renderbuff_m.fypp renderbuff_construct_sm.fypp renderbuff_operate_sm.fypp \
                  renderbuff_render_sm.fypp renderbuff_pixel_sm.fypp renderbuff_io_sm.fypp
view_SRCS = view_m.fypp view_construct_sm.fypp view_io_sm.fypp
other_SRCS = transform_m.fypp stat_m.fypp file_m.fypp math_m.fypp
all_SRCS = $(point_SRCS) $(vector_SRCS) $(mesh_SRCS) $(renderbuff_SRCS) $(view_SRCS) $(other_SRCS)

utest_mesh_SRCS = utest_mesh.fypp $(all_SRCS)
utest_mesh_USES = $(utest_mesh_SRCS)
utest_mesh_LIBS = 

utest_renderbuff_SRCS = utest_renderbuff.fypp $(all_SRCS)
utest_renderbuff_USES = $(utest_renderbuff_SRCS)
utest_renderbuff_LIBS =

# Build flags

FFLAGS = -I$(FORUM_INC_DIR)

FPPFLAGS = -I$(FORUM_INC_DIR)

LDFLAGS = `lapack_link` `hdf5_link` `lapack95_link` `odepack_link` -L$(FORUM_LIB_DIR) -lforum

# Include standard rules

include Make.inc

# Target for linting

linter :
	fortitude check --file-extensions=f90

.PHONY: all linter
