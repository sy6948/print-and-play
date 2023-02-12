# script to generate a png with cards

# import PIL library
from PIL import Image
import os

"""
Printer Class
"""
class CardsPrinter:

    """
    A4-size blank image as background
    in pixel:  72 dpi, 595 x 842 pixel
                300 dpi, 2490 x 3510 pixel
    in mm: 210 mm * 297 mm
    """
    a4_width_pixel = 2490
    a4_height_pixel = 3510
    a4_width_mm = 210
    a4_height_mm = 297

    """
    the dimension of the card to export is 88 mm x 63 mm
    """
    card_height_mm = 88
    card_width_mm = 63

    card_width_pixel = None
    card_height_pixel = None

    """
    the page margin 
    """
    page_margin_x_pixel = 100
    page_margin_y_pixel = 100

    """
    the card padding
    """
    card_padding_x_pixel = 5
    card_padding_y_pixel = 5

    """
    config
    """
    output_folder = "."
    output_prefix = "Output "

    """
    __init__() read the images from the input folder and store in card_list array
    """
    def __init__(self, input_folder):
        self.input_folder = input_folder
        if not os.path.exists(input_folder):
            exit(-1)
        self.card_list = os.listdir(input_folder)
        self.updateCardDimensionInPixel()

    """
    SetPageMargin() set the page x margin (left, right) and y margin (top, bottom) in pixel
    """
    def setPageMargin(self, margin_x, margin_y):
        self.page_margin_x_pixel = margin_x
        self.page_margin_y_pixel = margin_y
        self.updatePosList()

    """
    setCardDimension() set the card dimension for output
    """
    def setCardDimension(self, height, width):
        self.card_height_mm = height
        self.card_width_mm = width
        self.updateCardDimensionInPixel()

    """
    setCardPadding() set the card padding
    """
    def setCardPadding(self, padding_x_mm, padding_y_mm):
        self.card_padding_x_pixel = int(self.a4_width_pixel / self.a4_width_mm * padding_x_mm)
        self.card_padding_y_pixel = int(self.a4_width_pixel / self.a4_width_mm * padding_y_mm)
        self.updatePosList()

    """
    setPageMargin() set the card padding
    """
    def setPageMargin(self, margin_x_mm, margin_y_mm):
        self.page_margin_x_pixel = int(self.a4_width_pixel / self.a4_width_mm * margin_x_mm)
        self.page_margin_y_pixel = int(self.a4_width_pixel / self.a4_width_mm * margin_y_mm)
        self.updatePosList()

    """
    setOutputFolder() set the output folder for export
    """
    def setOutputFolder(self, output_folder):
        self.output_folder = output_folder

    """
    setOutputPrefix() set the output file prefix
    """
    def setOutputPrefix(self, prefix):
        self.output_prefix = prefix

    """
    updateCardDimensionInPixel() calculate and store the card dimenion from mm to pixel on A4 pages
    """
    def updateCardDimensionInPixel(self):
        self.card_width_pixel = int(self.a4_width_pixel / self.a4_width_mm * self.card_width_mm)
        self.card_height_pixel = int(self.a4_height_pixel / self.a4_height_mm * self.card_height_mm)
        self.updatePosList()
 
    """
    validPosX check if the current pos_x is valid (not out of boundary)
    """
    def validPosX(self, pos_x):
        if pos_x + self.card_width_pixel + self.page_margin_x_pixel > self.a4_width_pixel:
            return False
        return True

    """
    validPosY check if the current pos_y is valid (not out of boundary)
    """
    def validPosY(self, pos_y):
        if pos_y + self.card_height_pixel + self.page_margin_y_pixel > self.a4_height_pixel:
            return False
        return True

    """
    updatePosList() calculate and update the pos_list to store all card position in A4 page
    """
    def updatePosList(self):
        self.pos_list = []

        pos_x, pos_y = self.page_margin_x_pixel, self.page_margin_y_pixel
        while self.validPosX(pos_x) and self.validPosY(pos_y):
            self.pos_list.append((pos_x, pos_y))

            # move pos_x
            pos_x += self.card_width_pixel + self.card_padding_x_pixel
            
            # reset pos_x to first column and move pos_y to next row if out of bound
            if self.validPosX(pos_x) == False:
                pos_x = self.page_margin_x_pixel
                pos_y += self.card_height_pixel + self.card_padding_y_pixel

    """
    exportAll() export the cards to multiple pngs
    """
    def exportAll(self):
        n, card_index, png_index = len(self.card_list), 0, 1

        while card_index < n:
            num = self.exportOne(card_index, png_index)
            if num == 0:
                print("Error: Unable to export images. Please check you card dimension, card padding and page margin.")
                exit()
            card_index += num
            png_index += 1

    """
    exportOne() export the cards to one png as much as possible
    """
    def exportOne(self, card_index, page_index):
        background_color = (255, 255, 255)
        a4im = Image.new("RGB", (self.a4_width_pixel, self.a4_height_pixel), background_color)
        n, output_count = len(self.card_list), 0

        while card_index < n and output_count < len(self.pos_list):
            # get the next image position
            pos_x, pos_y = self.pos_list[output_count][0], self.pos_list[output_count][1]

            # output resized image to a4im
            image = self.input_folder + "/" + self.card_list[card_index]
            im = Image.open(image).resize((self.card_width_pixel, self.card_height_pixel))
            a4im.paste(im, (pos_x, pos_y))

            card_index += 1
            output_count += 1

        output_filename = f"{self.output_prefix}{page_index}.png"
        output_path = self.output_folder + "/" + output_filename
        a4im.save(output_path, 'png', quality=100)

        return output_count
