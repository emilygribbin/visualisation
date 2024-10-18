# GIF Creator from Image Files

This is a Python script that converts a series of images (such as SVG, PNG, or other formats) into an animated GIF. It includes functionality to find image files in a directory, convert non-PNG formats (e.g., SVG) to PNG, and create a GIF with adjustable duration and looping settings.

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
The main function to use is `create_gif`. Here’s an example of how to call it:
```
create_gif(
    directory='path/to/your/images',  # The folder containing your images
    output_filename='output.gif',     # The name of the generated GIF
    file_extension='svg',             # The image format to look for (default: 'svg')
    dpi=300,                          # DPI for SVG conversion to PNG (default: 300)
    duration=750,                     # Duration for each frame in milliseconds (default: 750ms)
    loop=0                            # Loop count for GIF (0 for infinite loop)
)
```

### 3. Steps Performed by the Script

1. Find Image Files: The script searches for all files with the specified extension (e.g., .svg, .png) in the target directory. It can optionally sort files by numbers in their filenames.

2. Convert to PNG: If the images are not already in PNG format, the script converts them to PNG. It uses CairoSVG for SVG files and Pillow for other formats.

3. Create Animated GIF: Once all images are in PNG format, the script compiles them into an animated GIF. You can customise the duration of each frame and the number of loops.

## Example of Usage

Here is a simple example demonstrating how to use the script:

```
from gif_creator import create_gif

# Example: Create a GIF from SVG files in the 'images' directory
create_gif(
    directory='images', 
    output_filename='my_animation.gif', 
    file_extension='svg', 
    dpi=300, 
    duration=750, 
    loop=0
)
```

## File Structure Requirements

Ensure that your files are stored in a structured directory like this:

  ```
/images
    image_1.svg
    image_2.svg
    image_3.png
```
If you are using SVG files, they will automatically be converted to PNG before being added to the GIF. If the files are named with numbers (like image_1.svg, image_2.png), the script will sort them by the numbers.

## Output

After running the script, the output will be an animated GIF saved to the path you provided (e.g., my_animation.gif).


## Error Handling

If no files with the specified extension are found in the directory, the script will raise a `ValueError`.
If any image file fails to convert, the script will skip that file and print an error message.

### License

This project is licensed under the MIT License.

