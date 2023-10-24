.PHONY: all lint clean run


all: lint clean run


run:
	uvicorn router.app:app --reload

lint:
	black .
	isort .

clean:
	@echo Removing __pycache__ directories...
	@for /r %%i in (__pycache__) do @if exist "%%i" rmdir /s /q "%%i"
	@echo Cleaning __pycache__ completed.
