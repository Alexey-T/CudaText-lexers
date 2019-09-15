# must run this script from the folder with all lexer.*.zip files
import os
import zipfile

l = os.listdir('.')
for item in l:
    if not item.endswith('.zip'):
        continue
    name = item.split('.')[1].replace('_', ' ')

    z = zipfile.ZipFile(item)
    dir = os.path.join('.', name)
    #os.mkdir(dir)
    z.extractall(dir)
