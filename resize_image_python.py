from PIL import Image

def resize_image(size1, size2):

    image = Image.open('ferthosi.jpg')

    print(f"Current size : {image.size}" )

    resized_image = image.resize(( size1, size2))
        
    resized_image.save('FerthosiNew.jpeg')

size1= int(input("Enter length: "))
size2= int(input("Enter width: "))

resize_image(size1, size2)
