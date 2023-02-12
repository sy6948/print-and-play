<!-- ABOUT THE PROJECT -->
## About The Project

This is an helper program to merge multiple images to A4 png for print-and-play purpose.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* Python 3

## Example
Run `python main.py` to merge all files in folder `input` and export to folder `output`.
```sh
python main.py
```

## Usage
Run `python main.py` with arguments.
```sh
python main.py [-h] [-i INPUT_FOLDER] [-p OUTPUT_PREFIX] [-o OUTPUT_FOLDER]
               [-ch CARD_HEIGHT] [-cw CARD_WIDTH] [-px CARD_PADDING_X]
               [-py CARD_PADDING_Y] [-mx PAGE_MARGIN_X] [-my PAGE_MARGIN_Y]
```
The optional arguments are:
- `-i INPUT_FOLDER`, `--input-folder INPUT_FOLDER` 
folder of input images
- `-p OUTPUT_PREFIX`, `--output prefix OUTPUT_PREFIX`
file prefix of the output images
- `-o OUTPUT_FOLDER`, `--output-folder OUTPUT_FOLDER`
folder for export the A4 pages
- `-ch CARD_HEIGHT`, `--card-height CARD_HEIGHT`
height of each card in Millimeter (mm)
- `-cw CARD_WIDTH`, `--card-width CARD_WIDTH`
width of each card in Millimeter (mm)
- `-px CARD_PADDING_X`, `--card-padding-x CARD_PADDING_X`
left and right padding in Millimeter (mm)
- `-py CARD_PADDING_Y`, `--card-padding-y CARD_PADDING_Y`
top and bottom padding in Millimeter (mm)
- `-mx PAGE_MARGIN_X`, `--page-margin-x PAGE_MARGIN_X`
page left and right margin in Millimeter (mm)
- `-my PAGE_MARGIN_Y`, `--page-margin-y PAGE_MARGIN_Y`
page top and bottom margin in Millimeter (mm)

<!-- LICENSE -->
## License

Distributed under the MIT License.

<!-- CONTACT -->
## Contact

Donald Cheung - [@linkedin](https://www.linkedin.com/in/kwan-yau-cheung-sy6948) - sy6948@gmail.com

Project Link: [https://github.com/sy6948/print-and-play](https://github.com/sy6948/print-and-play)

<!-- MARKDOWN LINKS & IMAGES -->
