import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    languages = ["ar","ca","cs","da","de","en","el","es","fi","fr","it","ko","nl","pl","pt","pt-br","ro","ru","sk","uk","zh-hans"]
    lang = request.config.getoption("language")
    browser = None
    if lang in languages:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})        
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be available")
    yield browser
    print("\nquit browser..")
    browser.quit()
