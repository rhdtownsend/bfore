# File     : Makefile
# Purpose  : makefile for build subdir

# Default rule in case make is invoked in current dir

all:
	make -C ..

# Targets

BIN_TARGETS = build_star

LIB_TARGETS = 

INC_FILES =

ifeq ($(UTESTS),yes)
   BIN_TARGETS += utest_vector utest_point utest_surface utest_mesh utest_renderbuff ptest_renderbuff
endif

# Source file lists & related variables
#
# xxx_SRCS = source files required to compile xxx
# xxx_USES = source files providing modules USE'd by xxx
# xxx_LIBS = library files required to link xxx

vector_SRCS = vector_m.fypp vector_operate_sm.fypp vector_transform_sm.fypp vector_array_sm.fypp
point_SRCS = point_m.fypp point_operate_sm.fypp point_transform_sm.fypp point_array_sm.fypp
mesh_SRCS = mesh_m.fypp mesh_construct_sm.fypp mesh_operate_sm.fypp mesh_connect_sm.fypp mesh_modify_sm.fypp \
            mesh_vert_sm.fypp mesh_face_sm.fypp mesh_io_sm.fypp mesh_primitives_m.fypp
renderbuff_SRCS = renderbuff_m.fypp renderbuff_construct_sm.fypp renderbuff_operate_sm.fypp \
                  renderbuff_render_sm.fypp renderbuff_pixel_sm.fypp renderbuff_io_sm.fypp
view_SRCS = view_m.fypp view_construct_sm.fypp view_io_sm.fypp
transform_SRCS = transform_m.fypp
surface_SRCS = polar_surface_m.fypp sphere_surface_m.fypp roche_surface_m.fypp #star_surface_m.fypp rotstar_surface_m.fypp
other_SRCS = stat_m.fypp file_m.fypp math_m.fypp
all_SRCS = $(point_SRCS) $(vector_SRCS) $(mesh_SRCS) $(renderbuff_SRCS) $(view_SRCS) $(transform_SRCS) $(surface_SRCS) $(other_SRCS)

utest_vector_SRCS = utest_vector.fypp $(vector_SRCS) $(transform_SRCS)
utest_vector_USES = $(utest_vector_SRCS)
utest_vector_LIBS =

utest_point_SRCS = utest_point.fypp $(point_SRCS) $(vector_SRCS) $(transform_SRCS)
utest_point_USES = $(utest_point_SRCS)
utest_point_LIBS =

utest_surface_SRCS = utest_surface.fypp $(surface_SRCS) $(point_SRCS) $(vector_SRCS) $(transform_SRCS)
utest_surface_USES = $(utest_surface_SRCS)
utest_surface_LIBS =

utest_mesh_SRCS = utest_mesh.fypp $(all_SRCS)
utest_mesh_USES = $(utest_mesh_SRCS)
utest_mesh_LIBS = 

utest_renderbuff_SRCS = utest_renderbuff.fypp $(all_SRCS)
utest_renderbuff_USES = $(utest_renderbuff_SRCS)
utest_renderbuff_LIBS =

ptest_renderbuff_SRCS = ptest_renderbuff.fypp $(all_SRCS)
ptest_renderbuff_USES = $(ptest_renderbuff_SRCS)
ptest_renderbuff_LIBS =

build_star_SRCS = build_star.fypp star_common_m.fypp $(all_SRCS)
build_star_USES = $(build_star_SRCS)
build_star_LIBS =

# Build flags

FFLAGS = -I$(FORUM_INC_DIR)

FPPFLAGS = -I$(FORUM_INC_DIR)

LDFLAGS = `lapack_link` `hdf5_link` `lapack95_link` `odepack_link` -L$(FORUM_LIB_DIR) -lforum `toml-f_link`

# Include standard rules

include Make.inc

# Target for linting

linter :
	fortitude check --file-extensions=f90

.PHONY: all linter
