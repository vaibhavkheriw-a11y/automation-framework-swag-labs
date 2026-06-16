import pytest
from pytest_html import extras
from base.base_driver import BaseDriver

@pytest.fixture(scope="function")
def driver(request):
    driver = BaseDriver()
    yield driver
    driver.exit_webdriver()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot = driver.take_screenshot(f"{item.name}.png")
            if screenshot:
                from pytest_html import extras
                extra = getattr(report, "extras", [])
                extra.append(extras.image(screenshot))
                report.extras = extra