@ECHO OFF

PUSHD "%~dp0.."
CALL python setup.py bdist_wheel upload
POPD
