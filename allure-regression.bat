@echo off

@REM regression TCs
pytest -vs -m "regression" --alluredir=allure_report

pause