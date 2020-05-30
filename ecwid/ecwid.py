# ecwid csv file to grav pages


# pip install urllib3

import csv, sys, os, io, codecs, urllib, requests

def getIMG(url, path, name):
    thisPath = path + '/' + name + '.jpg'
    print(thisPath)
    urllib.urlretrieve(url, thisPath)
    r = requests.get(url)

with open('import.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    # os.mkdir('toGrav')




    for line in csv_reader:


        # file handler
        path = 'import/' + line[23][22:].split("p/")[0].lower() #replace("p/", "p").replace("/", "-")
        if not os.path.exists(path):
            os.makedirs (path)
        # Create file
        print(path)

        # download product image
        if(line[6].endswith('.jpg')):
            getIMG(line[6], path, line[0].lower().replace(" ", "-").replace("/", "-").replace(",", "-"))

        header = '---' + '\n' + 'title: ' + line[0] + '\n' + "sku: " + line[1] + '\n' + 'published: true' + '\n' + 'product: true' + '\n' + '---'  + '\n'
        if(line[6].endswith('.jpg')):
            content = header + '# ' + line[0] + '\n\n' + '![' + line[0] + '](' + line[0].lower().replace(" ", "-").replace("/", "-") + '.jpg)' + '\n\n' + line[2] + '\n'
        else:
            content = header + '# ' + line[0] + '\n\n' + line[2] + '\n'
        path = path + '/blog_overview.en.md'

        with codecs.open(path, mode="w", encoding="utf-8") as f:
            f.write(unicode(content, "utf-8"))

        #def getJPG(url, filepath, filename):
        #    jpgpath = filepath + filename + '.jpg'
        #    urllib3.request.urlretrieve(url,jpgpath)
        #file = codecs.open('path','w','utf-8')
        #file.write(u'\ufeff')
        #file.close()


        #MD = os.open(path, os.O_RDWR|os.O_CREAT)
        #header = '---' + '\n' + 'title: ' + line[0] + '\n' + "sku: " + line[1] + '\n' + 'published: true' + '\n' + 'product: true' + '\n' + '---'  + '\n'
        #content = header + '# ' + line[0] + '\n\n' + line[2] + '\n'
        #content = unicode(content, "utf-8")
        # thisLine = unicode.encode(content)
        #numBytes = os.write(MD, content)
        #os.close(MD)


        # Debug

        # print('---')
        # print('title: ' + line[0])
        # print("sku: " + line[1])
        # print('published: true')
        # print('product: true')
        # print('---')
        # content
        # print("# " + line[0])
        # print(line[2])
