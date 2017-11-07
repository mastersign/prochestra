@ECHO OFF

SET indexurl=https://test.pypi.org/legacy/

PUSHD "%~dp0.."
CALL python setup.py sdist bdist_wheel
CALL twine upload "%~dp0../dist/*" --repository-url %indexurl%
POPD
