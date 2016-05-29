from myfile import read_file
from urllib.request import urlretrieve

videos = read_file()

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
