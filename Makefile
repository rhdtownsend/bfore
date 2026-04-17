# File     : Makefile
# Purpose  : top-level makefile

# Link against an external ForUM library
#
# If set to "yes", then the build system will use pkgconf to search
# for the library, with a package name speficied by
# EXTERNAL_FORUM_PKG. Otherwise, the ForUM library will be built and
# linked internally
EXTERNAL_FORUM ?= no
EXTERNAL_FORUM_PKG ?= forum

# Link against an external ForUM library
#
# If set to "yes", then the build system will use pkgconf to search
# for library, with a package name speficied by EXTERNAL_MSG_PKG.
# Otherwise, the MSG library will be built and linked internally
EXTERNAL_MSG ?= no
EXTERNAL_MSG_PKG ?= msg

# Enable debugging (with a performance penalty)
DEBUG ?= yes

# Build & link against shared libraries
SHARED ?= yes

# Enable OpenMP parallelization
OMP ?= yes

# Enable FPE checks
FPE ?= yes

# Build unit tests
UTESTS ?= yes

############ DO NOT EDIT BELOW THIS LINE ############
### (unless you think you know what you're doing) ###
#####################################################

# Export options

export EXTERNAL_FORUM
export EXTERNAL_FORUM_PKG
export EXTERNAL_MSG
export EXTERNAL_MSG
export DEBUG
export SHARED
export OMP
export FPE
export UTESTS

# General make settings

SH = /bin/bash
MAKEFLAGS += --print-directory

# Paths

export BIN_DIR ?= $(CURDIR)/bin
export LIB_DIR ?= $(CURDIR)/lib
export PKG_DIR ?= $(LIB_DIR)/pkgconfig
export INC_DIR ?= $(CURDIR)/include

export SRC_DIR := $(CURDIR)/src
export SRC_DIRS := $(addprefix $(SRC_DIR)/,vector point mesh renderbuff stream \
   view transform surface star mode math include common frontend)

# Rules

install : build | $(BIN_DIR) $(LIB_DIR) $(PKG_DIR) $(INC_DIR)
	@$(MAKE) -C build $@

build : install-forum install-msg
	@$(MAKE) -C build $@

clean : clean-forum clean-msg
	@$(MAKE) -C build $@
	@rm -rf $(BIN_DIR) $(LIB_DIR) $(PKG_DIR) $(INC_DIR)

ifneq ($(EXTERNAL_FORUM),yes)

   install-forum : | $(BIN_DIR) $(LIB_DIR) $(PKG_DIR) $(INC_DIR)
	@echo running $(MAKE) -C $(SRC_DIR)/forum
	@$(MAKE) -C $(SRC_DIR)/forum

   clean-forum :
	@echo running $(MAKE) -C $(SRC_DIR)/forum clean
	@$(MAKE) -C $(SRC_DIR)/forum clean

   install-forum : TESTS = no

   export TESTS

else

   install-forum : ;
   clean-forum : ;

endif

ifneq ($(EXTERNAL_MSG),yes)

   install-msg : | $(BIN_DIR) $(LIB_DIR) $(PKG_DIR) $(INC_DIR)
	@MSG_DIR=$(SRC_DIR)/msg $(MAKE) -C $(SRC_DIR)/msg

   clean-msg :
	@$(MAKE) -C $(SRC_DIR)/msg clean

   ifneq ($(EXTERNAL_FORUM),yes)
      install-msg : install-forum
   endif

   install-msg clean-msg : EXTERNAL_FORUM = yes
   install-msg : PKG_CONFIG_PATH += $(PKG_DIR)
   install-msg : TESTS = no
   install-msg : TOOLS = no
   install-msg : PYTHON = no

   export PKG_CONFIG_PATH
   export TESTS
   export TOOLS
   export PYTHON


else

   install-msg : ;
   clean-msg : ;

endif

.PHONY: install build clean install-forum clean-forum install-msg clean-msg

$(BIN_DIR) $(LIB_DIR) $(PKG_DIR) $(INC_DIR) :
	@mkdir -p $@
