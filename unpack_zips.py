# must run this script from the folder with all lexer.*.zip files
import os
import zipfile

items = os.listdir('.')
items = [fn for fn in items if fn.endswith('.zip')]
for fn in items:
    name = fn.split('.')[1].replace('_', ' ')

    z = zipfile.ZipFile(fn)
    dir = os.path.join('.', name)
    z.extractall(dir)

print('Zip files unpacked:', len(items))
