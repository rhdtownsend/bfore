# File     : Makefile
# Purpose  : makefile for build subdir

# Default rule in case make is invoked in current dir

all:
	make -C ..

# Targets

LIB_TARGETS = 

INC_FILES = 

ifeq ($(UTESTS),yes)
   BIN_TARGETS += utest_mesh utest_framebuffer utest_map
endif

# Source file lists & related variables
#
# xxx_SRCS = source files required to compile xxx
# xxx_USES = source files providing modules USE'd by xxx
# xxx_LIBS = library files required to link xxx

mesh_SRCS = mesh_m.fypp mesh_construct_sm.fypp mesh_operate_sm.fypp mesh_modify_sm.fypp mesh_traverse_sm.fypp \
            mesh_topology_sm.fypp mesh_geometry_sm.fypp mesh_io_sm.fypp \
            mesh_primitives_m.fypp \
	    stat_m.fypp file_m.fypp math_m.fypp \
            transform_m.fypp \
            point_m.fypp point_operate_sm.fypp point_transform_sm.fypp \
            vector_m.fypp vector_operate_sm.fypp vector_transform_sm.fypp \
            view_m.fypp view_construct_sm.fypp view_io_sm.fypp \
            framebuffer_m.fypp framebuffer_construct_sm.fypp framebuffer_render_sm.fypp framebuffer_pixel_sm.fypp framebuffer_io_sm.fypp \
            map_m.fypp map_construct_sm.fypp map_render_sm.fypp map_pixel_sm.fypp map_io_sm.fypp

utest_mesh_SRCS = utest_mesh.fypp $(mesh_SRCS)
utest_mesh_USES = $(utest_mesh_SRCS)
utest_mesh_LIBS = 

utest_framebuffer_SRCS = utest_framebuffer.fypp $(mesh_SRCS)
utest_framebuffer_USES = $(utest_framebuffer_SRCS)
utest_framebuffer_LIBS = 

utest_map_SRCS = utest_map.fypp $(mesh_SRCS)
utest_map_USES = $(utest_map_SRCS)
utest_map_LIBS = 

utest_surface_SRCS = utest_surface.fypp surface_m.fypp roche_surface_m.fypp
utest_surface_USES = $(utest_roche_surface_SRCS)
utest_surface_LIBS = 

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
