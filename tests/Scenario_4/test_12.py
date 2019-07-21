# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType

def test_11 (browser, pdf_file):
    """
    Сценарий 11. Выгрузка Презентации к повестке
        Шаг 1. Загрузка главной страницы:
        открыть страницу http://10.5.127.12/web

        Шаг 2. Авторизация:
        Вести логин и пароль - MekhdievZ, QAtest05

        Шаг 3. Перейти во вкладку "МИО.Итоговая повестка"
        В поле "Дата ближайщей повестки" выбрать дату
        Нажать кнопку "Презентация к повестке"
        Нажать кнопку "Закрыть"

        Шаг 4. Переход в раздел "Отчеты"
        Найти и Кликнуть по наименованию отчета
        Нажать кнопку-ссылку "Скачать"
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
            # Осуществить вход в систему под учетной записью
            browser.login_test_mvk('MekhdievZ', 'QAtest05')
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 3. "МИО.Итоговая повестка"'):
        try:
            # Перейти во вкладку "МИО.Итоговая повестка"
            browser.hover_and_click("/html/body/nav/div/div[2]/ul/li[2]/a", "/html/body/nav/div/div[2]/ul/li[2]/ul/li[5]/a")
            # browser.get("http://10.5.127.12/web/mio_final_notice")
            time.sleep(6)
            # В поле "Дата ближайщей повестки" выбрать дату
            browser.xpath(".//*[@id='noticeDate']").click()
            time.sleep(2)
            browser.xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[4]/a").click()
            time.sleep(3)
            # Нажать кнопку "Презентация к повестке"
            browser.xpath(".//*[@id='noticePresentationReport']").click()
            # Нажать кнопку "Закрыть"
            xp = ".//*[@id='close']"
            browser.xpath(xp, eager=True)[14].click()
            # browser.modal_close()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 4. Отчеты'):
        try:
            # Перейти в раздел "Отчеты"
            browser.hover_and_click("html/body/nav/div/div[2]/ul/li[3]/a", "html/body/nav/div/div[2]/ul/li[3]/a")
            # browser.get("http://10.5.127.12/web/jobs")
            time.sleep(3)
            # В поисковом поле ввести название отчета и нажать кнопку "Поиск"
            browser.xpath(".//*[@id='searchInput']").send_keys(u'Презентация к повестке (04.07.2019)')
            browser.xpath(".//*[@id='searchButton']").click()
            time.sleep(3)
            # Выбрать найденный отчет и скачать его
            browser.xpath("html/body/div[2]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]").click()
            browser.xpath(".//*[@id='outFile-card']/a").click()
            browser.xpath(".//*[@id='formCardJob']/div[3]/button[5]").click()
            browser.xpath("//a[@title='Выйти']").click()

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

