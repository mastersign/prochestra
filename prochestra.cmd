@ECHO OFF
SetLocal
PUSHD "%~dp0"
CALL python -m mastersign.prochestra %*
POPD
