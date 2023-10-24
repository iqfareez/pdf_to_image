![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# PDF to PNG transparent background utility

<!-- image here -->

## Get Started

Step shown below are for MacOS (maybe can be use on Linux as well)

- Create virtual environment (optional) by running `python3 -m venv venv`
- Activate virtual environment by running `source venv/bin/activate`
- Install dependencies by running `pip install -r requirements.txt`
- Install ImageMagick by running `brew install imagemagick`
- Run the script by running `python3 main.py`

> [!NOTE]  
> If error `ImportError: MagickWand shared library not found. You probably had not installed ImageMagick library. Try to install: brew install freetype imagemagick` occured. Try run the following command on the same terminal session where you run your python file: `export MAGICK_HOME=/opt/homebrew/opt/imagemagick`.

Sample PDF is provided `sample.pdf`. Output will be saved in `output` folder.
