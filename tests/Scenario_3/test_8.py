# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType

def test_8(browser, pdf_file):
    """
 Сценарий 6 "Фильтрация по просрочке в разделах "МИО.Основной отдел", "МИО.Отдел отказа", "Голосование""
    """

    with allure.step('Шаг 1. Открыть тестовый стенд МВК'):
        try:
            browser.open_test_mvk()
            browser.login_test_mvk('MekhdievZ', 'QAtest05')
            # time.sleep(5)
            # МИО отдел отказа
            browser.get('http://10.5.127.12/web/mio_decline_dept')
            # time.sleep(10)
            browser.xpath("//div[@data-status-age-gt='2']").click()
            # time.sleep(15)
            # browser.xpath("//td[contains(.,'50:04.20014')]").click()
            #TODO тест упал тут
            browser.open_new_card('50:04.20014')
            # time.sleep(10)
            browser.xpath("//a[@href='#tabStatusHistory_land']").click()
            # time.sleep(5)

            browser.xpath("//button[@id='js-close-card_land']").click()
            browser.xpath("//div[@data-status-age-gt='0']").click()

            # МИО Основной отдел
            browser.get('http://10.5.127.12/web/mio_main_dept')
            # time.sleep(10)
            browser.xpath("//div[@data-status-age-gt='7']").click()
            # time.sleep(15)
            # browser.xpath("//td[contains(.,'50:01.8754')]").click()
            browser.open_new_card('50:01.9790')
            # time.sleep(10)
            browser.xpath("//a[@href='#tabStatusHistory_land']").click()
            # time.sleep(5)
            browser.xpath("//button[@id='js-close-card_land']").click()
            browser.xpath("//div[@data-status-age-gt='4']").click()

            # Голосование
            browser.get('http://10.5.127.12/web/voting')
            # time.sleep(10)
            browser.xpath("//div[@data-status-age-gt='3']").click()
            # time.sleep(15)
            # browser.xpath("//td[contains(.,'50:33.11881')]").click()
            browser.open_new_card('50:99.9891')
            # time.sleep(7)
            browser.xpath("//a[contains(.,'История')]").click()
            browser.xpath("//button[@id='js-close-card_land']").click()
            browser.xpath("//div[@data-status-age-gt='2']").click()
            # time.sleep(10)

            browser.xpath("//a[@title='Выйти']").click()

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise













