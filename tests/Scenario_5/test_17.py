# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType


def test_12(browser, pdf_file):
    """
Сценарий 5. Сценарий првоерки счетчиков в разделе ОМС и МИО
        """


    with allure.step('Шаг 1. Открыть тестовый стенд МВК'):
        try:
            browser.open_test_mvk()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 2. Залогиниться на тестовый стенд МВК'):
        try:
            browser.login_test_mvk('MekhdievZ', 'QAtest05')
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 3. Переход по вкалдкам ОМС'):
        try:
            oms = 'html/body/nav/div/div[2]/ul/li[1]'
            # ОМС. В работе
            browser.search_for_selection(oms, 0)
            # ОМС. Отправлено на МВК
            browser.search_for_selection(oms, 1)
            # ОМС. Возврат на доработку
            browser.search_for_selection(oms, 2)
            # ОМС. Вынесено на комиссию
            browser.search_for_selection(oms, 3)
            # ОМС. Сводное заключение
            browser.search_for_selection(oms, 4)
            # ОМС. Градсовет
            browser.search_for_selection(oms, 5)
            # ОМС. Протокол. Отдел отказа
            browser.search_for_selection(oms, 6)
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 3. Переход по вкалдкам МИО'):
        try:
            mio = 'html/body/nav/div/div[2]/ul/li[2]'
            # МИО. Исполнитель
            browser.search_for_selection(mio, 0)
            # МИО. Отдел отказа
            browser.search_for_selection(mio, 1)
            # МИО. Основной отдел
            browser.search_for_selection(mio, 2)
            # МИО. Формируемая повестка
            browser.search_for_selection(mio, 3)
            # МИО. Итоговая повестка
            browser.search_for_selection(mio, 4)
            # МИО. Сводное заключение
            # В данном разделе не счетчик никогда не совпадает в связи с особенностями отображения страницы.
            browser.search_for_selection(mio, 5)
            # МИО. Градсовет
            browser.search_for_selection(mio, 6)
            # МИО. Отложенные проекты
            browser.search_for_selection(mio, 7)
            # МИО. Протокол. Отдел отказа
            # В данном разделе не счетчик никогда не совпадает в связи с особенностями отображения страницы.
            browser.search_for_selection(mio, 8)
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise