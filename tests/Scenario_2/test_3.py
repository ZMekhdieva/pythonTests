# coding=utf-8

import allure
from allure_commons.types import AttachmentType



def test_3(browser, pdf_file):
    """
    Сценарий 2. Сценарий скачивания документа из карточки, выгрузка сводного заключения,
     итоговой повестки, рабочей повестки
        """


    with allure.step('Шаг 1. Загрузка главной страницы'):
        try:
            # Открыть тестовый стенд МВК
            browser.open_test_mvk()

            # Залогиниться на тестовый стенд МВК
            browser.login_test_mvk('MekhdievZ', 'QAtest05')

            # Начать заполнение новой карточки
            browser.new_card()

            # Заполнить адрес в новой карточке
            browser.select_adress()

            # Заполнить карточку физического лица в новой карточке
            # ФИО
            browser.xpath('//input[@name="applicantsLC"]').send_keys(u'Тестов тест тестович')
            # Физическое лицо
            browser.xpath('//input[@id="individual"]').click()
            # Кадастровый номер
            browser.xpath("//input[@name='cadastralNumberLC']").send_keys("50:00:000000:00")
            # Предмет рассмотрения
            browser.select_value("//*[@id='subjectOfConsiderationLC']", 3)
            # Площадь квадратных метров
            browser.xpath('//input[@name="areaLC"]').send_keys(u"60")
            # Номер обращения в МФЦ
            browser.xpath('//input[@name="mfcNumberLC"]').send_keys(u"B501-0000000000-10914509")
            # Дата обращения в МФЦ
            browser.set_date_to_xpaths('//input[@name="mfcDateLC"]', u'08022019')
            # Вид решения
            browser.select_value('//*[@id="decisionTypeLC"]', 3)
            # Категория вопроса
            browser.select_text(".//*[@id='questionCategoryLC']", u"Проект ЦИОГВ о проведении торгов (аренда)")
            # Категория земельного участка
            browser.select_value('//*[@id="categoryLC"]', 3)
            # Вид разрешенного использования
            browser.select_value('//*[@id="containerForEditPattern"]', 2)
            # Исх. МСЭД
            #TODO тест упал тут
            #TODO пример плохого локатора
            browser.xpath('html/body/div[4]/div/div/form/div[2]/div/div[1]/div/div/div[5]/div/div/div[28]/div[2]'
                       '/input').send_keys(u'Тест')
            # Пояснение ОМС
            browser.xpath('//textarea[@name="explanationsLC"]').send_keys(u'Тест пояснения ОМС')
            # Пояснение МИО
            browser.xpath('//textarea[@name="explanationsMioLC"]').send_keys(u'Тест пояснения МИО')
            # Загрузить документ
            browser.doc_upload('//input[@name="attachments"]', pdf_file)
            # Далее
            browser.go_next()

            # Модальное окно "Похожие объекты"
            browser.modal_ok()

            # Сохранить текущее состояние карты для презентации
            browser.save_map()

            # Получить номер карточки
            browser.get_claim_number()

            # Создает карточку и сохраняет ее номер
            new_card = browser.save_card()

            # Найти новую созданную карточку и открыть ее
            browser.open_new_card(new_card)

            browser.xpath('//a[contains(.,"Скачать")]').click()

            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise
