from myfile import read_file
from urllib.request import urlretrieve

videos = read_file()

stri = """'THE $100 STARTUP | HOW MUCH* MONEY CAN YOU: MAKE ON YOUTUBE? |
 HOW TO START A BUSINESS WITH NO MONEY'.mp4""".replace('\n', '')

reservedChars = """\ / : * ? " < > |""".split(' ')


def cleanFileName(name):
    for el in reservedChars:
        name = name.replace(el, '')
    return name


# print(type(videos))
for key, value in videos.items():
    # print("%s, %s\n" % (key, value))
    fileName = cleanFileName(key)
    print("Downloading file %r.mp4 ...\n" % fileName)
    urlretrieve(value, fileName + ".mp4")
