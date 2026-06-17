@echo off

@REM clean old results
rmdir /s /q allure_report

@REM All TCs
pytest -vs --alluredir=allure_report

pause