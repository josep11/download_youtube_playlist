from myfile import read_file
import urllib.request
import urllib.request as req
import re
import sys

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


def downloadVideos(videos, rootPath=None):
    # try:
    #     pass
    # except URLError:
    #     raise
    def report(count, blockSize, totalSize):
        percent = int(count * blockSize * 100 / totalSize)
        sys.stdout.write("\r%d%%" % percent + ' complete')
        sys.stdout.flush()

        # http://snipplr.com/view/72137/display-the-download-percentage-of-a-file/
        urllib.urlretrieve(getFile, saveFile, reporthook=report)
        sys.stdout.write("\rDownload complete, saved as %s" %
                         (fileName) + '\n\n')

        sys.stdout.flush()

    def downlFile(getFile, saveFile, report):
        pass

    # connectProxy()
    if not rootPath:
        from os.path import expanduser
        home_dir = expanduser('~')
        rootPath = home_dir + "\\Videos"

    print('\n' + "Downloading", len(videos),
          "videos in folder: " + rootPath + '\n')

    for key, value in videos.items():
        # print("%s, %s\n" % (key, value))
        fileName = cleanFileName(key)
        print("Downloading file %r.mp4 ..." % fileName)
        try:
            req.urlretrieve(value,
                            rootPath + "\\" + fileName + ".mp4",
                            reporthook=report)
        except urllib.error.HTTPError as err:
            print(err.code)
        except:
            print("Unexpected error:")

if __name__ == "__main__":
    videos = read_file()
    downloadVideos(videos)
