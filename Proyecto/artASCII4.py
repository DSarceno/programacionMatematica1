from PIL import Image, ImageDraw, ImageFont
import math as m


# ascii_charact = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft'
# ASCII_CHARS = list(ascii_charact)
ASCII_CHARS = ['@','#','$','S','%','?','*','+',';',':','.',' ']



def rescale(image, newWidth=100):
    """Resizes an image preserving the aspect ratio.
    """
    (originalWidth, originalHeight) = image.size
    ratio = originalHeight/float(originalWidth)
    newHeight = int(ratio * newWidth)
    newImage = image.resize((newWidth, newHeight))
    return newImage, newHeight

def escalaGrises(image):
    return image.convert('L')

def pixelsAscii(image, rangeWidth=m.ceil(255/len(ASCII_CHARS))):
    """mapea cierto conjunto de pixeles a un caracter ascii.

    0-255 lo divide en un numero de rangos de m.ceil(255/len(ASCII_CHARS)) pixeles
    """

    pixelsImage = list(image.getdata())
    pixelsChars = [ASCII_CHARS[m.floor(pixel/rangeWidth)] for pixel in
            pixelsImage]

    return "".join(pixelsChars)

def imagetoAscii(image, newWidth=100):
    image, newHeight = rescale(image)
    image = escalaGrises(image)


    pixelsChars = pixelsAscii(image)

    fnt = ImageFont.load_default()
    outputImage = Image.new('RGB', (10*newWidth, 12*newHeight), color = (0, 0, 0))
    drawImage = ImageDraw.Draw(outputImage)

    for i in range(newHeight):
        for j in range(newWidth):
            drawImage.text((10*j, 12*i), pixelsChars[j + i*newWidth], font = fnt, fill = (255, 255, 255))

    outputImage.save('prueba.png')


    lenPixelsChars = len(pixelsChars)

    imageAscii = [pixelsChars[index: index + newWidth] for index in
            range(0, lenPixelsChars, newWidth)]

    return "\n".join(imageAscii)




def main(file, newWidth = 100):
    image = Image.open(file)


    imageAscii = imagetoAscii(image)
    print(imageAscii)





if __name__=='__main__':
    import sys

    file = sys.argv[1]
    main(file)
