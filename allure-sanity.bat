@echo off

@REM clean old results
rmdir /s /q allure_report

@REM sanity TCs
pytest -vs -m "sanity" --alluredir=allure_report

pause