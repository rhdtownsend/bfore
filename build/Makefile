# File     : Makefile
# Purpose  : makefile for build subdir

# Default rule in case make is invoked in current dir

all:
	make -C ..

# Targets

BIN_TARGETS = build_star render_mesh pulse_star color_star

LIB_TARGETS = 

PKG_FILES =
INC_FILES =

ifeq ($(UTESTS),yes)
   BIN_TARGETS += utest_vector utest_point utest_surface utest_mesh utest_renderbuff ptest_renderbuff
endif

# Source file lists & related variables
#
# xxx_SRCS = source files required to compile xxx
# xxx_USES = source files providing modules USE'd by xxx
# xxx_LIBS = library files required to link xxx

vector_SRCS = vector_m.fypp vector_operate_sm.fypp vector_transform_sm.fypp \
              vector_array_sm.fypp basis_vectors_m.fypp
point_SRCS = point_m.fypp point_operate_sm.fypp point_transform_sm.fypp \
             point_array_sm.fypp
mesh_SRCS = mesh_m.fypp mesh_construct_sm.fypp mesh_operate_sm.fypp \
            mesh_connect_sm.fypp mesh_modify_sm.fypp mesh_vert_sm.fypp \
            mesh_face_sm.fypp mesh_io_sm.fypp mesh_primitives_m.fypp \
           mesh_utils_m.fypp
renderbuff_SRCS = renderbuff_m.fypp renderbuff_construct_sm.fypp \
                  renderbuff_operate_sm.fypp renderbuff_render_sm.fypp \
                  renderbuff_pixel_sm.fypp renderbuff_io_sm.fypp
stream_SRCS = stream_m.fypp stream_construct_sm.fypp stream_operate_sm.fypp \
              stream_pixel_sm.fypp stream_io_sm.fypp
view_SRCS = view_m.fypp view_construct_sm.fypp view_operate_sm.fypp view_transform_sm.fypp \
            view_geometry_sm.fypp view_io_sm.fypp
transform_SRCS = transform_m.fypp
surface_SRCS = polar_surface_m.fypp sphere_surface_m.fypp roche_surface_m.fypp
star_SRCS = star_m.fypp star_construct_sm.fypp star_perturb_sm.fypp star_io_sm.fypp
mode_SRCS = mode_m.fypp
math_SRCS = special_m.fypp
other_SRCS = stat_m.fypp file_m.fypp math_m.fypp propmap_m.fypp
all_SRCS = $(point_SRCS) $(vector_SRCS) $(mesh_SRCS) $(renderbuff_SRCS) \
           $(stream_SRCS) $(view_SRCS) $(transform_SRCS) $(surface_SRCS) \
           $(mode_SRCS) $(math_SRCS) $(star_SRCS) $(other_SRCS)

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

render_mesh_SRCS = render_mesh.fypp $(all_SRCS)
render_mesh_USES = $(render_mesh_SRCS)
render_mesh_LIBS =

build_star_SRCS = build_star.fypp $(all_SRCS)
build_star_USES = $(build_star_SRCS)
build_star_LIBS =

pulse_star_SRCS = pulse_star.fypp $(all_SRCS)
pulse_star_USES = $(pulse_star_SRCS)
pulse_star_LIBS =

color_star_SRCS = color_star.fypp $(all_SRCS)
color_star_USES = $(color_star_SRCS)
color_star_LIBS =

# Build flags

PKGS = hdf5_fortran toml-f

PKGCONF_FLAGS =

ifeq ($(EXTERNAL_FORUM),yes)
   PKGS += $(EXTERNAL_FORUM_PKG)
else
   PKGS += forum
   PKGCONF_FLAGS += --with-path=$(PKG_DIR)
endif

ifeq ($(EXTERNAL_MSG),yes)
   PKGS += $(EXTERNAL_MSG_PKG)
else
   PKGS += msg
   PKGCONF_FLAGS += --with-path=$(PKG_DIR)
endif

FFLAGS := `pkgconf $(PKGCONF_FLAGS) --cflags $(PKGS)`
FPPFLAGS := `pkgconf $(PKGCONF_FLAGS) --cflags-only-I $(PKGS)` -m os
LDFLAGS := `pkgconf $(PKGCONF_FLAGS) --libs $(PKGS)`

# Include standard rules

include Make.inc

# Target for linting

linter :
	fortitude check --file-extensions=f90

# Targets for source checking

check_src:
	@for src in $(ALL_SRCS); do \
             find $(SRC_DIRS) -path '*/forum/*' -prune -or -name $$src -print | grep -q  . || echo $$src MISSING; \
         done

check_src : SRC_DIRS ?= ../src

.PHONY: all linter check_src
