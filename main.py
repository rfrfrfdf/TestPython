import os
import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager


class Downloader:
    def init(self):
        pass

    def mainMenu():
        menu = input('1 - Ввести ссылку и скачать трек\n'
                     '2 - Деинсталлировать библеотеки Selenium и Webdriver_manager:\n')
        if menu == '1':
            Downloader.loadFile()
        elif menu == '2':
            Downloader.cmdPrompt()

    def loadFile():

        yourTrack = input('--==Welcome to SoundCloud Downloader!==--\n'
                          '_To download your track you only need to enter SoundCloud link\n'
                          '___Example: https://soundcloud.com/allelas/a7x-nightmare-guitar-recording-no-solo\n\n\n'
                          '_____Your download link: ')

        choose = input('1 - Edge\n'
                       '2 - Chrome:\n')
        if choose == '1':
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        elif choose == '2':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif choose == 'cmd':
            Downloader.cmdPrompt()

        # Приветстие пользователя и ввод ссылки на песню для скачивания

        time.sleep(1)

        # Ссылка на sclouddownloader; переход по ссылке в браузере

        url = 'https://sclouddownloader.net'
        driver.get(url)

        # Передача ссылки на песню в поле ввода на сайте загрузчика
        # Нажатие на кнопку на этой странице, потом на следующей

        textLabel = driver.find_element_by_name('sound-url').send_keys(yourTrack)
        btn = driver.find_element_by_class_name('button').click()
        btn1 = driver.find_element_by_link_text('Download Track').click()
        # dummy = input('exit...')

        # Время ожидания загрузки

        for i in range(0, 5):
            print('Waiting...')
            time.sleep(2)

        answer = input('Continue? [y/n] - ')
        if answer == 'y' or answer == 'yes':
            Downloader.mainMenu()
        else:
            driver.close()
            exit()

    def cmdPrompt():
        # os.system('start cmd')
        os.system('pip uninstall selenium')
        os.system('pip unstall webdriver_manager')


Downloader.mainMenu()
