

def write_file(dictionary, filename="output.txt"):
    # for key, value in (dictionary):
    #     print("key: %s , value: %s" % (key, value))
    target = open(filename, 'w')
    target.truncate()
    for key, value in dictionary:
        target.write("%s#%s\n" % (key, value))
    target.close()


def read_file(filename="output.txt"):
    videos = {}
    target = open(filename)
    content = target.read().splitlines()
    # print(len(content))
    # quit()
    for line in content:
        lineSplit = line.split('#')
        videos[lineSplit[0]] = lineSplit[1].replace('|', '')
    return videos
