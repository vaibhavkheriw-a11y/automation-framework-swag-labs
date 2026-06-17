@echo off

@REM clean old results
rmdir /s /q allure_report

@REM smoke TCs
pytest -vs -m "smoke" --alluredir=allure_report

pause