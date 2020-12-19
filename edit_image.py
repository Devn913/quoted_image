from PIL import Image, ImageDraw, ImageFont, ImageFilter
from image_grab import ImageGrab
from fetch_quote import Quote
import textwrap
import random

class ImageEdit:

    def genPhoto(self):
        save_image = ImageGrab()
        save_image.unsplash()
    
    def blurImage(self):
        image_to_blur = Image.open("now.png")
        blurred_image = image_to_blur.filter(ImageFilter.GaussianBlur(radius=5))   
        blurred_image.save("now.png")
    
    def drawSquare(self):
        image = Image.open("now.png")
        draw = ImageDraw.Draw(image)
        color = "white"
        draw.rectangle([(50,50),(950,950)], fill=None, outline=color, width=15)
        image.save("now.png")
    
    def drawQuote(self):
        image = Image.open("now.png")
        draw = ImageDraw.Draw(image)      
        quote = Quote().getQuote()
        para = textwrap.wrap(quote, width=25)
        MAX_W, MAX_H = 1000, 1000
        current_h, pad = 300, 15
        last_font = 3                               # if you want to add a font change its name to a number following old fonts and change the variable here
        r = random.randint(1,last_font)
        fonts = ImageFont.truetype("fonts/"+ str(r) + ".ttf", 50)
        for line in para:
            w,h = draw.textsize(line,font = fonts)
            draw.text(((MAX_W - w) / 2 , current_h),line,font = fonts)   
            current_h += h + pad     
        image.save("now.png")
    
    def run(self):
        self.genPhoto()
        self.blurImage()
        self.drawSquare()
        self.drawQuote()
        return True

