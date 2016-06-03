from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import mybrowser
import configGUI
from download import *
from myfile import write_file
from myfile import read_file
from myfile import create_dir
# import pprint
from colorama import init, Back  # ,Fore

import time

init()

urlPlayList = """https://www.youtube.com/watch?v=74Wei0-vAZs&list=PL-bTaZrTDhtb
hxgS59t4HzwCnq2iIYMgV""".replace('\n', '')

urlBase = 'http://www.downvids.net/download-youtube-playlist-videos'


browser = mybrowser.initBrowser()
# browser = webdriver.PhantomJS()
# browser.implicitly_wait(1)  # esperar si elements no available immediatament


def printElement(element, trimLength=None):  # WebElement
    if element is None:
        print(Back.RED + "NULL element" + Back.BLACK)
        return

    html = element.get_attribute('innerHTML')
    print(Back.CYAN)
    if trimLength:
        print(html[:trimLength])
    else:
        print(html)
    # print(element.text + " " + element.tag_name)
    print(Back.BLACK)
    # print(username.parent)
    # print(username.tag_name)
    # print(username.text)
    # print(username.value_of_css_property)


def find_by_xpath(locator):
    try:
        element = browser.wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
    except TimeoutException:
        print(Back.RED + "TimeoutException buscant " + locator + Back.BLACK)
        return None
    return element


def find_el_by_text(text):
    # print('Buscant ...')
    # print("//*[contains(.,'%s')" % text)
    return find_by_xpath("//*[contains(.,'%s')]" % text)


def searchPlaylist(urlPlayList):
    browser.get(urlBase)
    searchForm = browser.find_element_by_id('home_search_q')
    submit = browser.find_element_by_id('home_search_submit')
    # time.sleep(3)
    searchForm.send_keys(urlPlayList)

    submit.click()


def getPlaylistTitle(urlPlayList):
    browser.get(urlPlayList)
    try:
        title = browser.find_element_by_xpath(
            '//*[@id="watch-appbar-playlist"]/div/div[1]/div[1]/div[2]/h3/a'
        ).text
    except Exception:
        title = 'gg'
    else:
        pass
    finally:
        pass
    return title


def extractUrlToDownload(trial=0):
    global urls
    if trial > 3:
        raise

    elements = browser.find_elements_by_partial_link_text('as video')
    if not len(elements):
        trial = trial + 1
        extractUrlToDownload(trial)
    else:
        urls = list(map(lambda el: el.get_attribute('href'), elements))


def extractVideoNames(trial=0):
    global videoNames

    if trial > 3:
        raise

    elements = browser.find_elements_by_class_name('msgtxt')
    if not len(elements):
        trial = trial + 1
        extractUrlToDownload(trial)
    else:
        videoNames = list(map(lambda el: el.text, elements))


# print(configGUI.pathToSaveVideos, configGUI.urlPlayList)

playlistTitle = getPlaylistTitle(configGUI.urlPlayList)

pathToSaveVideos = create_dir(
    configGUI.pathToSaveVideos + "\\" + playlistTitle
)

print(pathToSaveVideos)

searchPlaylist(configGUI.urlPlayList)

extractUrlToDownload()
extractVideoNames()

if len(videoNames) != len(urls):
    raise Exception('No sa parsejat bé els títols o les urls dels vídeos')

# write_file(zip(videoNames, urls))
downloadVideos(dict(zip(videoNames, urls)), pathToSaveVideos)
# browser.get_screenshot_as_file('prova.png')
# time.sleep(5)
# browser.quit()
