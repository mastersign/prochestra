@ECHO OFF

SET indexurl=https://test.pypi.org/legacy/

PUSHD "%~dp0.."
CALL python setup.py bdist_wheel upload -r %indexurl%
POPD
