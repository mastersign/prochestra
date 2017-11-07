@ECHO OFF

PUSHD "%~dp0.."
CALL python setup.py sdist bdist_wheel
CALL twine upload "%~dp0../dist/*"
POPD
