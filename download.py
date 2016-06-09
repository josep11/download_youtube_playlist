from myfile import read_file
import urllib.request
import urllib.request as req
import unicodedata
import sys
import os.path
from urllib.error import URLError, HTTPError
import urllib.parse
# in case we read the videos from the text file


reservedChars = """\ / : * ? " < > |""".split(' ')


def connectProxy():
    host = "hostname"
    port = "port"
    dominio = "domain"
    username = "internet"
    password = "internet2016"
    fullhost = dominio + "\\" + username
    print(r'http://' + fullhost + ':' + password + '@' +
          host + ':' + port)
    # proxy = req.ProxyHandler({'http': "http://" + host + ":" + port })
    # NOT WORKING
    # r"http://" + username + ":" + password + "@" + host + ":" + port
    proxy = req.ProxyHandler(
        {'http':
         (r'http://' + fullhost + ':' + password + '@' +
          host + ':' + port)
         })
    # print(dir(proxy))
    # print((proxy.proxies))
    auth = req.HTTPBasicAuthHandler()
    opener = req.build_opener(proxy, auth, req.HTTPHandler)
    req.install_opener(opener)
    conn = req.urlopen('http://google.com')
    return_str = conn.read()
    print(return_str)


def cleanFileName(name):
    for el in reservedChars:
        name = name.replace(el, '')
    return name


def slugify(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s)
                    if unicodedata.category(c) != 'Mn'))
    # NFD stands for Normal Form Decomposed
    # value = unicodedata.normalize('NFKD', value).encode('ASCII', 'ignore')
    # return value.decode('UTF-8')


def downloadVideos(videos, rootPath=None):
    # try:
    #     pass
    # except URLError:
    #     raise
    def report(count, blockSize, totalSize):
        percent = int(count * blockSize * 100 / totalSize)
        # sys.stdout.write('\r')
        tantXBarra = 100 / 40

        sys.stdout.write("\r[%-40s] %d%%" %
                         ('=' * int(percent / tantXBarra), percent))
        sys.stdout.flush()

        # http://snipplr.com/view/72137/display-the-download-percentage-of-a-file/
        # urllib.urlretrieve(url, saveFile, reporthook=report)

    def downlFile(url, saveFile, report):
        req.urlretrieve(url, saveFile, reporthook=report)
        print()
        return 0

    if not rootPath:
        home_dir = os.path.expanduser('~')
        rootPath = home_dir + "\\Videos"

    print('\n' + "Downloading", len(videos),
          "videos in folder: " + rootPath + '\n')

    for key, value in sorted(videos.items()):
        # print("%s, %s\n" % (key, value))
        fileName = slugify(cleanFileName(key))
        # fileName = key
        print("Downloading file %s.mp4 ..." % fileName)

        fullFileName = rootPath + "\\" + fileName + ".mp4"
        try:
            downlFile(value, fullFileName, report)
        except urllib.error.HTTPError as err:
            print(err.code)
        except:
            print("Unexpected error:")

if __name__ == "__main__":
    videos = read_file()
    downloadVideos(videos)
