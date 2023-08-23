install:
	poetry install
lint:
	flake8 page_loader
test:
	pytest -vvvv
check:
	make lint
	make test
test-coverage:
	poetry run pytest --cov --cov-report term-missing --cov-report xml
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	pip install dist/*.whl --force-reinstall
bpp:
	make build
	make publish
	make package-install
