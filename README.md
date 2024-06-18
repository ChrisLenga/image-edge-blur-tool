# Image Edge Blur Tool

This Python script applies a Gaussian blur to the edges of images, leaving the central part unblurred. It's particularly useful for preparing images for printing on items like mugs, where edge blending can help create a more seamless appearance.

An example below and the size and radius can be configured in the script.
![image](https://github.com/ChrisLenga/image-edge-blur-tool/assets/15137702/e9d276ac-4eaa-42d6-923c-01637fb54bd9)

## Features

- Processes multiple image formats including PNG, JPEG, and WEBP.
- Allows customization of blur intensity and the width of the central unblurred area.
- Handles images with alpha transparency.

## Requirements

- Python 3.x
- Pillow

## Installation

First, you'll need to install Python and Pillow. You can install Pillow using pip:

```bash
pip install Pillow
```

## Usage

1. Create a directory called `input` and `output`.
2. Place your images in an `input` directory.
3. Run the script using Python:

```bash
python edge_blur.py
```

3. Processed images will be saved in an `output` directory with blurred edges.

## Configuration

You can adjust the blur intensity and the width of the unblurred central area by modifying the following variables in the script:

- `blur_radius`: Controls the strength of the blur (default is 5).
- `border_size`: Defines the width of the unblurred central area (default is 30).

Modify these variables to achieve the desired effect based on your specific needs.

## Contributing

Contributions are welcome! If you have improvements or bug fixes, please open a pull request or issue.
