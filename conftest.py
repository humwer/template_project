import pytest
from webwalker import WebWalker
from locators import TestSite


def pytest_addoption(parser):
    parser.addoption('--without_browser', action='store', default='true',
                     help="Without browser: true or false")


@pytest.fixture(scope='function')
def walker(request):
    without_browser = request.config.getoption("without_browser")
    if without_browser == 'true':
        walker = WebWalker(url=TestSite.URL, option_launching_browser=True,
                           option_ignoring_error=True, debugging=True)
    elif without_browser == 'false':
        walker = WebWalker(url=TestSite.URL, option_launching_browser=False,
                           option_ignoring_error=True, debugging=True)
    else:
        raise pytest.UsageError("--without_browser should be true or false")
    yield walker
    print("\n[+] Quit browser")
    walker.browser.quit()

