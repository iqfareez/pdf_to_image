![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# PDF to PNG transparent background utility

<!-- image here -->

## Get Started

Step shown below are for MacOS/Linux

- Create virtual environment (optional) by running `python3 -m venv venv`
- Activate virtual environment by running `source venv/bin/activate`
- Install dependencies by running `pip install -r requirements.txt`
- Install ImageMagick by running `brew install imagemagick` or `sudo apt install imagemagick`

## Usage

- Run the script by running `python3 main.py`
- Sample PDF is provided `sample.pdf`. Output will be saved in `output` folder.


## Troubleshooting


**Error: `ImportError: MagickWand shared library not found. You probably had not installed ImageMagick library. Try to install: brew install freetype imagemagick`**

Try run the following command on the same terminal session where you run your python file: 

```zsh
export MAGICK_HOME=/opt/homebrew/opt/imagemagick
``` 
[Source](https://gist.github.com/dongyuwei/3668fcc69f557dd32c46?permalink_comment_id=4484086#gistcomment-4484086)

**wand.exceptions.PolicyError: attempt to perform an operation not allowed by the security policy `PDF' @ error/constitute.c/IsCoderAuthorized/421**

Run command below to turn off security setting

```
sudo mv /etc/ImageMagick-6/policy.xml /etc/ImageMagick-6/policy.xml.off
```

When you are done with the tool, revert the setting to its original

```
sudo mv /etc/ImageMagick-6/policy.xml.off /etc/ImageMagick-6/policy.xml
```

[Source](https://stackoverflow.com/a/57721936/13617136)



## Sample PDFs

`sample.pdf` is provided for you to test right away. You can get more sample pdf from:
- https://colortest.page/printer-color-test-page/#google_vignette
- https://www.maths.ed.ac.uk/~dmarsh/files/printer-testcard-colour.pdf
- https://cream.sourceforge.net/ColorCard.pdf
- etc.