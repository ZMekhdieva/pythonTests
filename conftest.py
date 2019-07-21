# coding=utf-8
import platform
import tempfile

import pytest

from drivers import *
from model.mvkpage import MvkPageObject

BROWSER = "CHROME"

@pytest.yield_fixture
def browser():
    options = chrome_options()
    options['enableVNC'] = True
    options['name'] = os.getenv("JOB_NAME")
    # Специальная стратегия хрома. Не будем дожидаться полной загрузки страницы
    # options['pageLoadStrategy'] = "normal"
    version = os.getenv("VERSION")
    if version:
        options['version'] = version

    # chrome = create_remote_driver(BROWSER, URL, custom_capabilities=options)
    chrome = create_local_driver(BROWSER, desired_capabilities=options)

    driver = MvkPageObject(chrome)
    if platform.system() == "Windows":
        driver.maximize_window()
    else:
        driver.set_window_size(1920, 1080)
    driver.timeout = 60
    driver.set_page_load_timeout(130)
    session_id = chrome.session_id
    yield driver
    driver.quit()



FILE_SIZE = '11' * 1000

@pytest.yield_fixture(scope="function")
def zip_file():
    fd, path = tempfile.mkstemp(suffix='.zip')
    with os.fdopen(fd, 'w') as f:
        f.write(FILE_SIZE)
        f.flush()
    yield path
    os.remove(path)


@pytest.yield_fixture(scope="function")
def jpg_file():
    fd, path = tempfile.mkstemp(suffix='.jpg')
    with os.fdopen(fd, 'w') as f:
        f.write(FILE_SIZE)
        f.flush()
    yield path
    os.remove(path)


@pytest.yield_fixture(scope="function")
def sig_file():
    fd, path = tempfile.mkstemp(suffix='.sig')
    with os.fdopen(fd, 'w') as f:
        f.write(FILE_SIZE)
        f.flush()
    yield path
    os.remove(path)


@pytest.yield_fixture(scope="function")
def pdf_file():
    fd, path = tempfile.mkstemp(suffix='.pdf')
    with os.fdopen(fd, 'w') as f:
        f.write(FILE_SIZE)
        f.flush()
    yield path
    os.remove(path)


@pytest.yield_fixture(scope="function")
def xls_file():
    fd, path = tempfile.mkstemp(suffix='.xls')
    with os.fdopen(fd, 'w') as f:
        f.write(FILE_SIZE)
        f.flush()
    yield path
    os.remove(path)


@pytest.yield_fixture(scope="function")
def xml_file():
    fd, path = tempfile.mkstemp(suffix='.xml')
    with os.fdopen(fd, 'w') as f:
        f.write(FILE_SIZE)
        f.flush()
    yield path
    os.remove(path)


@pytest.yield_fixture(scope="function")
def xlsx_file():
    fd, path = tempfile.mkstemp(suffix='.xlsx')
    with os.fdopen(fd, 'w') as f:
        f.write(FILE_SIZE)
        f.flush()
    yield path
    os.remove(path)


@pytest.yield_fixture(scope="function")
def zip_file():
    fd, path = tempfile.mkstemp(suffix='.zip')
    with os.fdopen(fd, 'w') as f:
        f.write(FILE_SIZE)
        f.flush()
    yield path
    os.remove(path)
