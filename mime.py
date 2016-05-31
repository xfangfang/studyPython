import mimetypes
print mimetypes.guess_type('/Users/FANGs/Downloads/8367527881140385272.jpg')[0]
myfile = file("/Users/FANGs/Downloads/8367527881140385272.jpg","rb")

print myfile.read()
