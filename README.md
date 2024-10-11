# GIF Creator from Image Files

This Python project provides a script that converts a series of images (such as SVG, PNG, or other formats) into an animated GIF. It includes functionality to find image files in a directory, convert non-PNG formats (e.g., SVG) to PNG, and create a GIF with adjustable duration and looping settings.

## Requirements

Make sure the following Python packages are installed before running the script:

- `Pillow`: for handling image formats.
- `CairoSVG`: for converting SVG files to PNG format.
- `imageio`: for creating animated GIFs from a series of PNG files.

## How to use

### 1. Organise your files

To use the script, you need to store your images in a directory. The supported formats include:
- .svg
- .png
- Other formats supported by Pillow (e.g., .jpg, .jpeg).

The script expects the files to be named with numbers if you wish to sort them by numerical order. For example:

```
image_1.svg
image_2.svg
image_3.png
```

### 2. Call the `create_gif` function
