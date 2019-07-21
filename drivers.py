# coding:utf-8
import os


import selenium
from selenium import webdriver
from selenium.webdriver import Ie, Opera, Chrome, Firefox
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.opera.options import Options

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
EXTENSION_DIR = os.path.join(CURRENT_DIR, "extensions")


def create_remote_driver(drivername, executor, custom_capabilities=None, **kwargs):
    if not isinstance(drivername, str):
        msg = "drivername should be an instance of string. given {0}".format(type(drivername))
        raise TypeError(msg)
    if not isinstance(executor, str):
        msg = "executor should be an instance of string. given {0}".format(type(executor))
        raise TypeError(msg)
    if custom_capabilities and not isinstance(custom_capabilities, dict):
        msg = "custom_capabilities should be an instance of dict. given {0}".format(type(custom_capabilities))
        raise TypeError(msg)
    capabilities = {'ie': DesiredCapabilities.INTERNETEXPLORER,
                    'opera': DesiredCapabilities.OPERA,
                    'chrome': DesiredCapabilities.CHROME,
                    'firefox': DesiredCapabilities.FIREFOX}
    dname = drivername.lower()
    if dname in capabilities:
        capability = capabilities[dname]
        custom_capabilities = custom_capabilities or {}
        for key in custom_capabilities:
            capability[key] = custom_capabilities[key]
        driver = selenium.webdriver.Remote(executor, capability, **kwargs)
        try:
            return driver
        except Exception as e:
            raise e
    else:
        msg = "".join(("drivername should be one of [IE, Opera, Chrome, Firefox, PhantomJS]",
                       "(case-insentive). given {0}".format(drivername)))
        raise ValueError(msg)


def create_local_driver(drivername, *args, **kwargs):
    if not isinstance(drivername, str):
        msg = "drivername should be an instance of string. given {0}".format(type(drivername))
        raise TypeError(msg)
    drivers = {'ie': Ie,
               'opera': Opera,
               'chrome': Chrome,
               'firefox': Firefox}
    dname = drivername.lower()
    if dname in drivers:
        try:
            return drivers[dname](*args, **kwargs)
        except Exception as e:
            raise e
    else:
        msg = "".join(("drivername should be one of [IE, Opera, Chrome, Firefox, PhantomJS]",
                       "(case-insentive). given {0}".format(drivername)))
        raise ValueError(msg)


def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=ru')
    # options.add_argument('--headless')
    options.add_argument('--always-authorize-plugins=true')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--auto-open-devtools-for-tabs')
    # options.add_extension(os.path.join(EXTENSION_DIR, "CAdES_Browser_Plug-in.crx"))
    # options.add_extension(os.path.join(EXTENSION_DIR, "ESEPCrypto.crx"))
    options.add_experimental_option(
        'prefs', {
            'credentials_enable_service': False,
            'profile': {
                'password_manager_enabled': False
            },
            "intl.accept_languages": "ru",
            "plugins.plugins_enabled": [
                "Chrome PDF Viewer",
                "Native Client"
            ]
        }
    )
    return options.to_capabilities()


