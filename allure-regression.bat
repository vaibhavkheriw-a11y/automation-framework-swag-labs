@echo off

@REM clean old results
rmdir /s /q allure_report

@REM regression TCs
pytest -vs -m "regression" --alluredir=allure_report

pause