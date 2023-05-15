import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s

@allure.tag('web')
@allure.feature('Задачи в репо')
@allure.story('Тест без шагов')
def test_selene(web_browser):
    web_browser.open('/')

    s(".header-search-input").type("qa_guru_5_12_allure_reports").press_enter()
    s(by.link_text('dmitri91/qa_guru_5_12_allure_reports')).click()
    s('#issues-tab').click()

    s(by.partial_text('test_issue')).should(be.visible)


@allure.tag('web')
@allure.feature('Задачи в репо')
@allure.story('Тест с шагами через with allure.step')
def test_dynamic_step(web_browser):
    with allure.step('Открываем главную страницу'):
        web_browser.open('/')

    with allure.step('Ищем репозиторий'):
        s(".header-search-input").type("qa_guru_5_12_allure_reports").press_enter()
    with allure.step('Переходим по ссылки репозитория'):
        s(by.link_text('dmitri91/qa_guru_5_12_allure_reports')).click()
    with allure.step('Открываем Issues'):
        s('#issues-tab').click()
    with allure.step('Проверяем наличие задачи с именем "test_issue"'):
        s(by.partial_text('test_issue')).should(be.visible)


@allure.tag('web')
@allure.feature('Задачи в репо')
@allure.story('Тест с шагами деоратора allure')
def test_decorator_steps(web_browser):
    open_main_page()
    search_for_repository("dmitri91/qa_guru_5_12_allure_reports")
    go_to_repository("dmitri91/qa_guru_5_12_allure_reports")
    open_issues()
    should_see_issue_with_number("test_issue")


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-input").type(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем Issues')
def open_issues():
    s('#issues-tab').click()


@allure.step('Проверяем наличие задачи с именем {name}')
def should_see_issue_with_number(name):
    s(by.partial_text(name)).should(be.visible)
