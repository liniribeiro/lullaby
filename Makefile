

PYTHON = python3

PYTHONPATH := $(shell pwd)


run_gunicorn:
	@echo "---- Running Application ----"
	@PYTHONPATH="${PYTHONPATH}" gunicorn -c ./lullaby/gunicorn.py lullaby.main:app


run_all:
	@echo "---- Running Application ----"
	@make run_gunicorn


############################## Testes ##############################

test:
	${PYTHON} -m pytest --cov=src tests/

