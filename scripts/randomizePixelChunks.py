import os.path, random
from sys import argv, exit
from PIL import Image

def getChunkSize(s, imgs):
    if s == 1 or s == 2:
        return s
    orig = s
    while s > 2 and (imgs[0] % s != 0 or imgs[1] % s != 0):
        s -= 1
    
    if s != 2:
        return s

    s = orig

    while (s < imgs[0] / 2 and s < imgs[1] / 2) and (imgs[0] % s != 0 or imgs[1] % s != 0):
        s += 1

    if s >= imgs[0] / 2 or s >= imgs[1] / 2: 
        return 2

    return s

argc = len(argv)
if argc != 4:
    print 'Usage: ', argv[0], ' [picturename] [outputname] [chunkwidth]'
    print 'Will find the closest chunksize to evenly distribute chunks in resolution'
    exit()

if os.path.isfile(argv[1]) == False:
    print "Image does not exist"
    exit()

im = Image.open(argv[1])
pixelMap = im.load()

img = Image.new(im.mode, im.size)
pixelsNew = img.load()

cs = getChunkSize(int(argv[3]), im.size)

cw = im.size[0] / cs
ch = im.size[1] / cs
chunks = cw * ch
pix = random.sample(xrange(0, chunks), chunks)

for i in xrange(0, chunks):
    for j in xrange(0, cs):
        for k in xrange(0, cs):
            pixelsNew[(i%cw)*cs+j,(i/cw)*cs+k] = pixelMap[(pix[i]%cw)*cs+j,(pix[i]/cw)*cs+k]

im.close()
img.save(argv[2])
img.close()
