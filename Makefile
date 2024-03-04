# Define the default target
.DEFAULT_GOAL := all

# Define variables
TEST_FOLDER := ./test
SCRIPT := $(TEST_FOLDER)/file_gen.sh

# Define variables with default values
# W is the width and L is number of values. 
W ?= 8
L ?= 10

NAME1 := "_infile_.1"
NAME2 := "_infile_.2"

# Define targets
all: generate_infiles

# Rule to run the Bash script
create_file:
	@echo "Running $(SCRIPT) with arguments $(width) and $(list_l) of name $(name)..."
	@bash $(SCRIPT) $(W) $(L) $(name)

generate_infiles:
	@echo "Generating 2 infiles: $(SCRIPT) with arguments $(W) and $(L) ..."
	@bash $(SCRIPT) "$(W)" "$(L)" "$(NAME1)"
	@bash $(SCRIPT) "$(W)" "$(L)" "$(NAME2)"

# Clean rule
clean:
	@echo "Cleaning up..."
	@rm -f *.txt *.1 *.2

.PHONY: all create_file clean

