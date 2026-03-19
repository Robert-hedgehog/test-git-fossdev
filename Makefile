.DEFAULT_GOAL := help

create-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	@echo "Creating practice"
	mkdir -p $(PRACTICE)

remove-practice:
ifndef PRACTICE
	$(error must pass val via PRACTICE)
endif
	rm -rf $(PRACTICE)

help:
	@echo "This makefile for repo-level activity"

#mkdir demo-prcatice
#mkdir demo-prcatice/src
#mkdir demo-prcatice/tests
#mkdir demo-prcatice/docs
#mkdir demo-prcatice/README.md
