# Define the default target
.DEFAULT_GOAL := all

# Define variables
SCRIPT := file_gen.sh

NAME1 := "_infile_.1"
NAME2 := "_infile_.2"


# Define targets
all: create_file

# Rule to run the Bash script
create_file:
	@echo "Running $(SCRIPT) with arguments $(width) and $(list_l) of name $(name)..."
	@bash $(SCRIPT) $(width) $(list_l) $(name)

generate_infiles:
	@echo "Generating 2 infiles: $(SCRIPT) with arguments $(width) and $(list_l) ..."

	@bash $(SCRIPT) "$(width)" "$(list_l)" "$(NAME1)"
	@bash $(SCRIPT) "$(width)" "$(list_l)" "$(NAME2)"

# Clean rule
clean:
	@echo "Cleaning up..."

.PHONY: all create_file clean

