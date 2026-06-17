import pytest
import allure
from pytest_html import extras
from base.base_driver import BaseDriver
from utilities.logger import logger

@pytest.fixture(autouse=True)
def set_test_description(request):
    description = request.node.name.replace("_", " ").capitalize()
    allure.dynamic.description(description)
    logger.info(f"Starting test: {request.node.name}")

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
    if report.when == "call":
        logger.info(f"Test {item.name} {report.outcome}")
        if report.failed:
            driver = item.funcargs.get("driver")
            if driver:
                screenshot = driver.take_screenshot(f"{item.name}.png")
                if screenshot:
                    from pytest_html import extras
                    extra = getattr(report, "extras", [])
                    extra.append(extras.image(screenshot))
                    report.extras = extra
                    try:
                        allure.attach.file(
                            screenshot,
                            name="Failure Screenshot",
                            attachment_type=allure.attachment_type.PNG,
                        )
                    except Exception:
                        logger.exception("Failed to attach screenshot to Allure report")