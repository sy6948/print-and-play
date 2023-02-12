import argparse, os
from CardPrinter import CardsPrinter

def main():
    # arguments parser
    parser = argparse.ArgumentParser(
        description = 'This program merge multiple images to A4 png for "print and play" purpose.'
    )

    # add arguments
    parser.add_argument("-i", "--input-folder", help="the folder of input images", default="input")
    parser.add_argument("-p", "--output-prefix", help="the file prefix of the output images", default="output ")
    parser.add_argument("-o", "--output-folder", help="the folder for export the A4 pages", default="output")
    parser.add_argument("-ch", "--card-height", help="height of each card in Millimeter (mm)", type=int, default=88)
    parser.add_argument("-cw", "--card-width", help="width of each card in Millimeter (mm)", type=int, default=63)
    parser.add_argument("-px", "--card-padding-x", help="left and right padding in Millimeter (mm)", type=int, default=1)
    parser.add_argument("-py", "--card-padding-y", help="top and bottom padding in Millimeter (mm)", type=int, default=1)
    parser.add_argument("-mx", "--page-margin-x", help="page left and right margin in Millimeter (mm)", type=int, default=5)
    parser.add_argument("-my", "--page-margin-y", help="page top and bottom margin in Millimeter (mm)", type=int, default=5)
    
    args = parser.parse_args()
    # check if input folder exist
    if not os.path.exists(args.input_folder):
        parser.exit(message=f"Error: input folder \"{args.input_folder}\" does not exist!")

    # create output folder if not exist
    if not os.path.exists(args.output_folder):
        os.mkdir(args.output_folder)    
    
    # printer config
    printer = CardsPrinter(args.input_folder)
    if args.output_folder != None:
        printer.setOutputFolder(args.output_folder)
    if args.output_prefix != None:
        printer.setOutputPrefix(args.output_prefix)

    printer.setCardDimension(args.card_height, args.card_width)
    printer.setCardPadding(args.card_padding_x, args.card_padding_y)
    printer.setPageMargin(args.page_margin_x, args.page_margin_y)

    # export the pngs
    printer.exportAll()

if __name__ == "__main__":
    main()