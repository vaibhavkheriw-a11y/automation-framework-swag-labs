@echo off

@REM sanity TCs
pytest -vs -m "sanity" --alluredir=allure_report

pause