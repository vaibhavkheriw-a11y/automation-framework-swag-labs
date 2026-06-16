@echo off

@REM smoke TCs
pytest -vs -m "smoke" --alluredir=allure_report

pause