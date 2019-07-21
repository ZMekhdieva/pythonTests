# coding=utf-8
import time

import allure
from allure_commons.types import AttachmentType

from model.card import Card


def test_1(browser, pdf_file):
    """
Сценарий 1. Сценарий движения карточки Основного отдела, снятие с учета/Итоговая повестка/Протокол сформирован
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

    with allure.step('Шаг 3. Заполнить карточку физического лица в новой карточке'):
        try:
            browser.new_card_button()
            # Выбрать адрес
            browser.select_adress()
            browser.new_card(Card(FIO="test", cadastr_number="50:01:0060215:00", square="123",
                                  mfcnumber="M503-01234567-89", mfcdate="08.05.2019",
                                  questioncategory=3,
                                  explanationsmio="Тест пояснения МИО",
                                  explanationsoms="Тест пояснения ОМС"))
            browser.doc_upload('//input[@name="attachments"]', pdf_file)
            # Создает карточку и сохраняет ее номер

            created_card = browser.save_card()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 4. Найти новую созданную карточку и открыть ее, отправить на открытую карточку МВК'):
        try:
            browser.open_new_card(created_card)
            browser.edit_card(Card(FIO="parampampam"))
            browser.send_to_mvk()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 5. Перейти в раздел "Голосование", найти новую карточку и снять с голосования'):
        try:
            browser.get('http://10.5.127.12/web/voting')
            browser.open_new_card(created_card)
            browser.remove_from_voting()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 6. Перейти во вкладку "МИО.Основной отдел", найти карточку и назначить ответственного'):
        try:
            browser.get('http://10.5.127.12/web/mio_main_dept')
            browser.select_new_card(created_card)
            browser.set_executant()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 7. Отправить на доработку'):
        try:
            browser.select_new_card(created_card)
            browser.send_to_rework()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 8. Редактировать карточку'):
        try:
            browser.open_new_card(created_card)
            browser.edit_card()
            browser.xpath('//textarea[@name="draftDecisionLC"]').send_keys(u'Тест')
            browser.save_after_edit()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 9. Отправить на МВК'):
        try:
            browser.get('http://10.5.127.12/web/oms_rework')
            browser.select_new_card(created_card)
            browser.select_new_card(created_card)
            browser.send_to_mvk()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 10. Перейти во вкладку МИО Основной отдел и отправить на согласование'):
        try:
            browser.get('http://10.5.127.12/web/mio_main_dept')
            browser.select_new_card(created_card)
            browser.send_to_consideration()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 11. Включить в повестку'):
        try:
            browser.select_new_card(created_card)
            browser.send_to_formed_notice()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 12. Перейти во вкладку МИО.Формируемая повестка'):
        try:
            browser.get('http://10.5.127.12/web/mio_formed_notice')
            browser.set_date('//input[@id="noticeDate"]')
            #TODO тест упал тут
            browser.select_new_card(created_card)
            browser.send_to_commission()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 13. Выйтит из УЗ и войти в УЗ для формирования итоговой повестки'):
        try:
            browser.end_session()
            #TODO Введен неверный логин или пароль
            browser.login_test_mvk('LebedAA', 'LebedAA')
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 14. Перейти в раздел "МИО итоговая повестка и Сформировать протоколом'):
        try:
            browser.get('http://10.5.127.12/web/mio_final_notice')
            browser.set_date('//input[@id="noticeDate"]')
            browser.select_new_card(created_card)
            browser.formed_protocol()
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 15. Перейти во вкладку "МИО. Сводное заключение" и открыть карточку'):
        try:
            browser.get('http://10.5.127.12/web/mio_protocol')
            time.sleep(7)
            browser.select_new_card(created_card)
            time.sleep(7)

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise
