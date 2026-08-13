from collections.abc import Generator
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--browser",
        action="store",
        choices=("chrome", "firefox"),
        default="chrome",
        help="Browser to run: chrome or firefox (default: chrome).",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run without a visible browser window (local runs are headed by default).",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo[None]):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"report_{report.when}", report)


@pytest.fixture(scope="function")
def driver(request: pytest.FixtureRequest) -> Generator[WebDriver, None, None]:
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        web_driver = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        web_driver = webdriver.Firefox(options=options)
        web_driver.set_window_size(1920, 1080)

    try:
        yield web_driver
    finally:
        report = getattr(request.node, "report_call", None)
        if report is not None and report.failed:
            screenshot_dir = Path(__file__).resolve().parents[1] / "screenshots"
            screenshot_dir.mkdir(exist_ok=True)
            screenshot_path = screenshot_dir / f"{browser}-{request.node.name}.png"
            try:
                web_driver.save_screenshot(str(screenshot_path))
            except Exception as error:  # Screenshot failure must not prevent browser cleanup.
                print(f"Unable to capture failure screenshot: {error}")
        web_driver.quit()
