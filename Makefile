ROOT_DIR:=./
VENV_BIN_DIR:="venv/bin"

VIRTUALENV:=$(shell which virtualenv)

REQUIREMENTS_DIR:="requirements"
REQUIREMENTS_LOCAL:="$(REQUIREMENTS_DIR)/local.txt"

PIP:="$(VENV_BIN_DIR)/pip"
AUTOPEP8:="$(VENV_BIN_DIR)/autopep8"

CMD_FROM_VENV:=". $(VENV_BIN_DIR)/activate; which"
PYTHON=$(shell "$(CMD_FROM_VENV)" "python")


.PHONY: hello activatevenv deactivatevenv venv freeze fix clean runlocal


hello:
	@echo "Hello, World!"

# DEVELOPMENT

define create-venv
virtualenv venv -p python3
endef

activatevenv:
	@source ./$(VENV_BIN_DIR)/activate

deactivatevenv:
	@source deactivate

venv:
	@$(create-venv)
	@$(PIP) install -r $(REQUIREMENTS_LOCAL)

freeze: venv
	@$(PIP) freeze > $(REQUIREMENTS_LOCAL)

fix: venv
	@$(AUTOPEP8) --in-place --aggressive --recursive $(ROOT_DIR)

clean:
	@rm -rf .cache
	@find . -name hangman.db -delete
	@find . -type d -name __pycache__ -delete
	@rm -rf venv

# LOCAL

runlocal: venv
	@"$(PYTHON)" Proyecto.py