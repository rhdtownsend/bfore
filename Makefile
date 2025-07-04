# File     : Makefile
# Purpose  : top-level makefile

# Build ForUM internally. If not set to "yes", then
# you must set FORUM_LIB_DIR and FORUM_INC_DIR to
# point to where the ForUM library and module files,
# respectively, are located
FORUM ?= yes

# Build MSG internally. If not set to "yes", then
# you must set MSG_LIB_DIR and MSG_INC_DIR to
# point to where the ForUM library and module files,
# respectively, are located
MSG ?= no

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

# General make settings

export

SH = /bin/bash
MAKEFLAGS += --no-print-directory

# Paths

BIN_DIR ?= $(CURDIR)/bin
LIB_DIR ?= $(CURDIR)/lib
INC_DIR ?= $(CURDIR)/include

SRC_DIR = $(CURDIR)/src
SRC_DIRS = $(addprefix $(SRC_DIR)/,mesh common framebuffer view transform vector point surface map include)

ifeq ($(FORUM),yes)
   FORUM_LIB_DIR = $(LIB_DIR)
   FORUM_INC_DIR = $(INC_DIR)
endif

ifeq ($(MSG),yes)
   MSG_LIB_DIR = $(LIB_DIR)
   MSG_INC_DIR = $(INC_DIR)
endif

# Rules

install : build | $(BIN_DIR) $(LIB_DIR) $(INC_DIR)
	@$(MAKE) -C build $@

build : install-forum
	@$(MAKE) -C build $@

clean : clean-forum
	@$(MAKE) -C build $@
	@rm -rf $(BIN_DIR) $(LIB_DIR) $(INC_DIR)

ifeq ($(FORUM),yes)

   install-forum : | $(BIN_DIR) $(LIB_DIR) $(INC_DIR)
	@$(MAKE) -C src/forum install

   clean-forum :
	@$(MAKE) -C src/forum clean

else

   install-forum : ;
   clean-forum : ;

endif

ifeq ($(MSG),yes)

   install-msg : | $(BIN_DIR) $(LIB_DIR) $(INC_DIR)
	@MSG_DIR=src/msg $(MAKE) -C src/msg install

   clean-msg :
	@$(MAKE) -C src/msg clean

   ifeq ($(FORUM),yes)
      install-msg : install-forum
   endif

   install-msg clean-msg : FORUM = no
   install-msg : TESTS = no
   install-msg : TOOLS = no
   install-msg : PYTHON = no

else

   install-msg : ;
   clean-msg : ;

endif

.PHONY: install build clean install-forum clean-forum install-msg clean-msg

$(BIN_DIR) $(LIB_DIR) $(INC_DIR) :
	@mkdir -p $@
