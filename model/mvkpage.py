# coding=utf-8

""" Page Object для сайта mvk
"""
import random
import re
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from model.page import Page


class SetCorrectUserType(Exception):
    """ Кидает исключение, если выбран отсутствующий тип пользователя
    """
    pass


def ogrn_generator(length):
    """ Генератор ОГРН, ОГРНИП

    """
    if length == 14:
        divide = 13
    else:
        divide = 11

    my_randoms = [str(random.randrange(1, 9, 1)) for _ in range(length)]
    num = "".join(my_randoms)
    div = int(num) % divide
    if div > 9:
        div = str(div)[-1]
    ogrn = int(num + str(div))
    return str(ogrn)


class MvkPageObject(Page):


    def open_test_mvk(self):
        # Открывает главную страницу прод МВК
        self.get("http://10.5.127.12/web")

    def login_test_mvk(self, login, password):
        # Логинится на прод МВК
        self.find_element_by_id("login").click()
        self.find_element_by_id("login").clear()
        self.find_element_by_id("login").send_keys(login)
        self.find_element_by_id("password").click()
        self.find_element_by_id("password").clear()
        self.find_element_by_id("password").send_keys(password)
        self.find_element_by_id("loginBtn").click()

    def modal_close(self):
        # Нажимает "Закрыть" в модальном окне группового изменения статуса
        try:
            wait = WebDriverWait(self, 20)
            actions = ActionChains(self)
            xpath = ".//*[@id='idCardGroupChangeStatusResult']"
            statusMessage = wait.until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
            if self.is_exists(xpath):
                actions.move_to_element(statusMessage).perform()
                # here you can get text from message window, check/assert ..
                time.sleep(5)
                statusMessage.find_element_by_css_selector("#close").click()
        except:
            pass

    def select_value(self, xpath, num):
        # Выбирает значение из списка
        self.xpath(xpath).click()
        follow_sibling = self.xpath("{}/ancestor::div".format(xpath))
        follow_sibling.xpath("//span[2]/ul/li[{}]".format(num)).click(presleep=1)

    def go_next(self):
        # Далее
        self.xpath('//button[contains(.,"Далее")]').click()

    def add_dock(self, xpath):
        # Добавить документ
        element = self.find_element_by_xpath(xpath)
        element.send_keys("C:\myfile.jpg")

    def modal_ok(self):
        try:
        # Нажимает "Ок" в модальном окне "Найдены похожие объекты"
            self.xpath('//*[@id="idCardMatchedLand"]/div').click()
            self.xpath('//button[contains(.,"Ок")]').click()
        except NoSuchElementException: ""

    def get_claim_number(self):
        self.xpath("//a[@href='#tabInformation_land']").click()
        el = self.xpath("//div[@id='serialNumberLC']")
        return el.get_attribute("textContent")

    def save_card(self):
        # Сохранить карточку
        # Далее
        self.go_next()
        # Модальное окно "Похожие объекты"
        self.modal_ok()
        # Сохранить текущее состояние карты для презентации
        self.save_map()
        claim = self.get_claim_number()
        el2 = self.find_element_by_xpath(".//*[@id='js-save-card_land']")
        el2.click()
        return claim

    def save_map(self):
        # Сохраняет текущее состояние карты для презентации
        el = self.find_element_by_xpath('//a[@id="saveLinksForPresentation"]')
        el.click(presleep=5)

    def send_to_mvk(self):
        # Отправить на МВК открытую карточку
        xpaths = ".//*[@id='sendToMvkButton']",\
                 ".//*[@id='sendGroupToMvkButton']",

        for xpath in xpaths:
            if self.is_exists(xpath):
                self.xpath(xpath).click(presleep=2)
                break
        self.modal_confirm()
        self.modal_close()

    def set_executant(self):
        # Назначить ответственного
        xpaths = "//button[@id='setExecutantButton']",\
                 ".//*[@id='setGroupExecutantButton']"

        for xpath in xpaths:
            if self.is_exists(xpath):
                self.xpath(xpath).click(presleep=2)
                break
        self.xpath('//h4[contains(.,"Назначить ответственного")]').click()
        self.select_value('.//*[@id="executant"]/span', 2)
        self.modal_confirm()
        modal = '//*[@aria-hidden="false"]'
        if self.is_exists(modal):
            self.modal_close()

    def open_new_card(self, new_card):
        # Найти новую созданную карточку и открыть ее
        self.search_card(new_card)
        elem = self.find_element_by_xpath('//div[@class="floatThead-wrapper"]//td[.="' + new_card + '"]')
        elem.click(presleep=2)
        self.scroll_to_element('.//*[@id="statusButtonsBlock"]')

    def select_new_card(self, new_card):
        # Найти новую созданную карточку и выбрать ее в таблице
        self.search_card(new_card)
        elem = self.find_element_by_xpath("//input[@class='select-row-checkbox' and @type='checkbox']")
        elem.click(presleep=2)
        self.scroll_to_element('.//*[@id="statusButtonsBlock"]')

    def select_adress(self):
        # Заполнить адрес в новой карточке
        self._move_to_element("//span[@title='Московская, обл']")
        self.select_value('//span[contains(@title,"Район")]', 2)  # Район
        self.select_value('//span[contains(@title,"Город")]', 2)  # Город
        self.select_value('//span[contains(@title,"Улица")]', 2)  # Улица
        self.select_value('//span[contains(@title,"Дом")]', 2)  # Дом

    def user_fl(self):
        # Заполнить карточку физического лица в новой карточке
        # ФИО
        self.xpath('//input[@name="applicantsLC"]').send_keys(u'Тестов тест тестович')
        # Физическое лицо
        self.xpath('//input[@id="individual"]').click()
        # Кадастровый номер
        self.xpath("//input[@name='cadastralNumberLC']").send_keys("50:00:000000:00")
        # Предмет рассмотрения
        self.select_value("//*[@id='subjectOfConsiderationLC']", 3)
        # Площадь квадратных метров
        self.xpath('//input[@name="areaLC"]').send_keys(u"60")
        # Номер обращения в МФЦ
        self.xpath('//input[@name="mfcNumberLC"]').send_keys(u"B501-0000000000-10914509")
        # Дата обращения в МФЦ
        self.set_date_to_xpaths('//input[@name="mfcDateLC"]', u'08022019')
        # Категория вопроса
        self.select_value(".//*[@id='questionCategoryLC']", 3)
        # Вид решения
        self.select_value('//*[@id="decisionTypeLC"]', 2)
        # Категория земельного участка
        self.select_value('//*[@id="categoryLC"]', 3)
        # Вид разрешенного использования
        self.select_value('//*[@id="containerForEditPattern"]', 2)
        # Исх. МСЭД
        self.xpath('html/body/div[4]/div/div/form/div[2]/div/div[1]/div/div/div[5]/div/div/div[28]/div[2]'
                      '/input').send_keys(u'Тест')
        # Пояснение ОМС
        self.xpath('//textarea[@name="explanationsLC"]').send_keys(u'Тест пояснения ОМС')
        # Пояснение МИО
        self.xpath('//textarea[@name="explanationsMioLC"]').send_keys(u'Тест пояснения МИО')
        # Загрузить документ
        self.add_dock('//input[@name="attachments"]')

    def select_text(self, xpath, text):
        # Выбирает из выпадающего списка (xpath) поле с указанным текстом text
        self.xpath(xpath).click()
        input_xp = 'html/body/span/span/span[1]/input'
        self.xpath(input_xp).send_keys(text)
        result = self.find_element_by_xpath('html/body/span/span/span[2]')
        items = result.find_element_by_tag_name('li')
        items.click()


    def change_fild_value(self, field_name, text):
        if text is not None:
            self.xpath(field_name).send_keys(text)

        if field_name.__getattribute__("textContent").

    def new_card(self, card):
        #ФИО
        self.change_fild_value('//input[@name="applicantsLC"]', card.FIO)
        # Физическое лицо
        self.xpath('//input[@id="individual"]').click()
        # Кадастровый номер
        self.change_fild_value("//input[@name='cadastralNumberLC']", card.cadastr_number)
        # Предмет рассмотрения
        self.select_value("//*[@id='subjectOfConsiderationLC']", 3)
        # Площадь квадратных метров
        self.change_fild_value('//input[@name="areaLC"]', card.square)
        # Номер обращения в МФЦ
        self.change_fild_value('//input[@name="mfcNumberLC"]', card.mfcnumber)
        # Дата обращения в МФЦ
        self.change_fild_value('//input[@name="mfcDateLC"]', card.mfcdate)
        # Вид решения
        self.select_value('//*[@id="decisionTypeLC"]', 3)
        # Категория вопроса
        self.select_text(".//*[@id='questionCategoryLC']", card.questioncategory)
        # Категория земельного участка
        self.select_value('//*[@id="categoryLC"]', 3)
        # Вид разрешенного использования
        self.select_value('//*[@id="containerForEditPattern"]', 2)
        # Пояснение ОМС
        self.change_fild_value('//textarea[@name="explanationsLC"]', card.explanationsoms)
        # Пояснение МИО
        self.change_fild_value('//textarea[@name="explanationsMioLC"]', card.explanationsmio)
        # Загрузка документа
        # self.xpath('//input[@name="attachments"]').send_keys(card.file_type)
        # # Далее
        # self.go_next()
        # # Модальное окно "Похожие объекты"
        # self.modal_ok()
        # # Сохранить текущее состояние карты для презентации
        # self.save_map()
        # # Получить номер карточки
        # self.get_claim_number()

    def new_card_button(self):
        self.find_element_by_xpath("html/body/div[2]/div[2]/div[4]/div/div/div[1]/button[1]").click(presleep=10)
        self.xpath('html/body/div[4]/div/div/form').click()

    def confirm(self):
        # Нажимает "Ок" в модальном окне
        el = self.find_element_by_xpath('//button[contains(.,"Подтвердить")]')
        el.click()

    def end_session(self):
        el = self.xpath('//a[contains(@class,"logoutLink") or contains(@title,"Выйти")]')
        el.click()

    def remove_from_voting(self):
        # Нажимает кнопку "Снять с голосования" в детализации карточки
        self.xpath('//button[@id="sendToMvkInterruptingVoting"]').click(postsleep=2)
        self.xpath('html/body/div[5]/div/div/div[3]/button[1]').click()

    def send_to_rework(self):
        # Нажимает кнопку "Отправить на доработку" и заполняет поля в модальном окне
        xpaths = ".//*[@id='sendToOmsRework']",\
                 ".//*[@id='sendGroupToOmsRework']"

        for xpath in xpaths:
            if self.is_exists(xpath):
                self.xpath(xpath).click(presleep=2)
                break
        self.xpath('//h4[contains(.,"Отправить на доработку")]').click()
        self.xpath('//textarea[contains(@name,"remark")]').send_keys('Тест')
        self.xpath('//input[@name="msedNumber"]').send_keys(u'111')
        self.modal_confirm()
        self.modal_close()

    def edit_card(self, new_card_data):
        # Нажимает кнопку "Редактировать" в детализации карточки
        self.xpath('html/body/div[4]/div/div/form/div[3]/button[2]').click(presleep=2)
        self.new_card(new_card_data)

    def save_after_edit(self):
        # Нажимает кнопку "Сохранить" во время редактирования карточки
        self.xpath('.//*[@id="js-save-card_land"]').click()

    def send_to_consideration(self):
        # Нажимает кнопку "Отправить на согласование" в детализации карточки
        xpaths = "html/body/div[4]/div/div/form/div[2]/div/div[1]/div/div/div[9]/button[6]",\
                 "html/body/div[2]/div[2]/div[3]/div/div[1]/div/button[3]",

        # project_result = ''

        for xpath in xpaths:
            if self.is_exists(xpath):
                self.xpath(xpath).click(presleep=2)
                break
        project_result_modal = './/*[@id="idCardTextAreaChangeStatus"]'
        time.sleep(5)
        if self.is_exists(project_result_modal):
            # self.xpath(project_result_modal).click()
            self.xpath("//textarea[@name='modalTextArea']").send_keys('Тест')
            self.modal_confirm()
            self.modal_close()
        else:
            self.modal_confirm()

    def modal_confirm(self):
        #Нажимает кнопку "Подтвердить" в всплывающем окне подтверждения действия
        el = self.xpath('//*[@aria-hidden="false"]')
        el2 = el.find_elements_by_tag_name('button')
        el2[0].click()
        time.sleep(5)

    def send_to_formed_notice(self):
        # Нажимает кнопку "Включить в повестку" и заполняет поля в модальном окне
        xpaths = "//button[@class='btn btn-sm btn-default status-after-consideration' and " \
                 "@id='sendToFormedNotice' and contains(text(),'Включить в повестку')]",\
                 "//button[@class='btn btn-sm btn-default status-after-consideration' and " \
                 "@id='sendGroupToFormedNotice'and contains(text(),'Включить в повестку')]",

        for xpath in xpaths:
            if self.is_exists(xpath):
                self.xpath(xpath).click(presleep=2)
                break
        wait = WebDriverWait(self, 5)
        notice_day = wait.until(EC.visibility_of_element_located((By.XPATH, 'html/body/div[11]/div/div/div[2]/div/form/div/div[2]/input')))
        self.set_date('html/body/div[11]/div/div/div[2]/div/form/div/div[2]/input')
        # self.set_date_to_xpaths('html/body/div[11]/div/div/div[2]/div/form/div/div[2]/input', u'07.03.2019')
        self.modal_confirm()
        modal = '//*[@aria-hidden="false"]'
        if self.is_exists(modal):
            self.modal_close()

    def set_date(self, xpath):
        """ Записывает дату и закрывает календарь
        """
        self.xpath(xpath).click()
        # self.xpath(xpath).send_keys(text)
        # В случае если календарь отсутствует тест будет продолжен
        try:
            el = self.xpath("//td[@data-handler='selectDay' and contains(.,'28')]", eager=True)
            el[0].click()
        except:
            self.css(".ui-state-default").click()
            pass


    def send_to_commission(self):
        # Нажимает кнопку "Вынести на комиссию"
        xpaths = "html/body/div[4]/div/div/form/div[2]/div/div[1]/div/div/div[7]/button[7]", \
                 "html/body/div[2]/div[2]/div[3]/div/div[1]/div/button[2]"

        for xpath in xpaths:
            if self.is_exists(xpath):
                self.xpath(xpath).click()
                self.modal_confirm()
                break
        modal = '//*[@aria-hidden="false"]'
        if self.is_exists(modal):
            self.modal_close()

    def formed_protocol(self):
        xpaths = "//button[@class='btn btn-sm btn-default' and " \
                 "@id='sendToFormedProtocol' and contains(text(),'Сформировать протокол')]", \
                 "html/body/div[2]/div[2]/div[3]/div/div[1]/div/button[5]", \


        for xpath in xpaths:
            if self.is_exists(xpath):
                self.xpath(xpath).click(presleep=2)
                self.select_value('.//*[@id="mvkDecision"]/span/span[1]/span', 5)
                self.modal_confirm()
                break
        modal = '//*[@aria-hidden="false"]'
        if self.is_exists(modal):
            self.modal_close()

    def search_card(self, new_card):
        table = WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.XPATH, "html/body/div[2]/div[2]/div[5]/div[2]/table/tbody|html/body/div[2]/div[2]/div[5]")))
        self.xpath('//button[@id="changeFilterVisibility"]').click()
        self.xpath('//input[@name="serialNumber-param"]').clear()
        self.xpath('//input[@name="serialNumber-param"]').send_keys(new_card)
        self.xpath('//button[@id="searchLandsButton"]').click(presleep=3)
        protocol = './/*[@id="protocol_accordion"]'
        if self.is_exists(protocol):
            self.xpath(protocol).click(presleep=5)
        self.xpath('//button[@id="changeFilterVisibility"]').click()
        time.sleep(3)

    def doc_upload(self, xpath, file_type):
        """ Загружает документ в форму"""
        self.xpath(xpath).send_keys(file_type)

    def hover_and_click(self, hover, click):
        self._move_to_element(hover)
        self.xpath(click).click()

    def select_option(self):
        el = self.find_element_by_xpath("xpath")
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'text':
                option.click()

    def check_for_counter(self, xpath):
        # xpath = 'html/body/nav/div/div[2]/ul/li[1]'
        target = self.xpath(xpath)
        self._move_to_element(xpath)
        el2 = target.find_elements_by_tag_name('li')
        new_array = []
        for element in el2:
            # table = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.XPATH, "html/body/div[2]/div[2]/div[5]/div[2]")))
            x = element.get_attribute('textContent')
            # element.click()
            # y = re.sub("\D", "", x)
            new_array.append(x)
        print(new_array)
        # for element in new_array:

    def search_for_selection(self, section, num):
        select = self.xpath(section)
        el2 = select.find_elements_by_tag_name('li')
        time.sleep(10)
        self._move_to_element(section)
        selection_counter = el2[num].get_attribute("textContent")
        el2[num].click()
        time.sleep(10)
        scounter = re.sub("\D", "", selection_counter)
        page_counter = self.xpath("html/body/div[2]/div[2]/div[6]/div/div[1]/span/span")
        page_counter = self.xpath("html/body/div[2]/div[2]/div[6]/div/div[1]/span/span").parent.unwrap.text
        pcounter = re.sub("\D", "", page_counter)
        # x = page_counter.parent.unwrap.text.get_attribute("text")
        if scounter == pcounter:
            print(selection_counter, page_counter)
        else: print("ERROR : " + selection_counter, page_counter)

    def go_to_section(self, patition, section):

        time.sleep(10)
        oms = "ОМС"
        mio = "МИО"
        list = [oms, mio]



        for patition in list:
            if patition == patition:
                xpath = "html/body/nav/div/div[2]/ul/li[1]/a"
                self._move_to_element(xpath)

        xpath = "//a[@href='/web/oms_mvk']"

        list2 = {"Отправлено на МВК": xpath}
        for section in list2.values():
            if section == section:
                self.xpath(xpath).click()
