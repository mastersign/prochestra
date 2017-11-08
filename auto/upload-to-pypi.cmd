@ECHO OFF

PUSHD "%~dp0.."
DEL /S /Q "%~dp0..\dist"
CALL python setup.py sdist bdist_wheel
CALL twine upload "%~dp0../dist/*"
POPD
