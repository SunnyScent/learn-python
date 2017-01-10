import urllib.request


def save_image(url, filename):
    usock = urllib.request.urlopen(url)
    data = usock.read()
    usock.close()
    fp = open(filename, 'wb')
    fp.write(data)
    fp.close


save_image("https://lh3.googleusercontent.com/-UDAq_ddU8IA/WHN5jujL76I/AAAAAAAAox0/7LTW-vo0XxQMlCPsSuS4hetXDihhLT6rQCJoC/s530-p-rw/9%2B-%2B1",'1')
