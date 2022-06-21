#!/bin/bash
set -e

_PATH="./app"
if [ -s "$1" ] && [ -d "$1" ]; then
    _PATH="./$1"
fi

echo "=========================================="
echo "==  Starting code quality verification  =="
echo "=========================================="

echo -e "\n [*] Safety check [safety check]"
safety check

echo -e "\n [*] Flake8 linting [flake8 $_PATH]"
flake8 $_PATH

echo -e "\n [*] Pylint linting [pylint $_PATH]"
pylint $_PATH

echo -e "\n [*] Isort module import order [isort $_PATH --check-only]"
isort $_PATH --check-only

echo -e "\n [*] Black code formatter [black --check $_PATH]"
black --check $_PATH

echo -e "\n [*] Radon code quality Cyclomatic Complexity B- [radon cc $_PATH -nb]"
radon cc $_PATH -nb

echo -e "\n [*] Radon code quality Maintainability Index B- [radon mi $_PATH -nb]"
radon mi $_PATH -nb

echo -e "\n [*] Bandit security issues [bandit -r $_PATH]"
bandit -r $_PATH

echo -e "\n [*] Doctest with pytest [pytest --doctest-modules $_PATH --disable-warnings]"
pytest --doctest-modules $_PATH --disable-warnings

echo "==================================="
echo "==  Good, exiting without error  =="
echo "==================================="

exit 0
