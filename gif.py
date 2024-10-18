"""
GIF Creator from Image Files

This script finds image files (e.g., SVG, PNG) in a specified directory, converts them to PNG (if necessary),
and compiles them into an animated GIF with customisable frame duration and looping.

Author: Emily Gribbin
GitHub: https://github.com/emilygribbin/Visualisation
Date: 18th October 2024

Usage:
------
Please refer to the README.md file for detailed usage instructions and examples.

License:
--------
This project is licensed under the MIT License - see the LICENSE file for details.

Citation:
---------
If you use this project in your research or for any academic purpose, please cite it using the following:

Gribbin, Emily. 2024. Gif Creator. GitHub Repository: https://github.com/emilygribbin/Visualisation
"""

import os
import re
from pathlib import Path
from typing import List
from PIL import Image
import cairosvg
import imageio.v2 as imageio

def find_image_files(directory: str, file_extension: str = 'svg', sort_by_numbers: bool = True) -> List[str]:
    """
    Finds and returns a list of image files with a specific extension in a directory.

    Parameters
    ----------
    directory : str
        Directory where the image files are located.
    file_extension : str, optional
        File extension to filter by (e.g., 'svg', 'png'). Default is 'svg'.
    sort_by_numbers : bool, optional
        If True, sorts files by numbers found in filenames. Default is True.

    Returns
    -------
    List[str]
        List of image file paths, optionally sorted by numbers in filenames.
    """
    file_pattern = Path(directory).glob(f'*.{file_extension}')
    image_files = [str(f) for f in file_pattern]

    if sort_by_numbers:
        numbered_files = [(int(re.search(r'\d+', os.path.basename(f)).group()), f) for f in image_files if re.search(r'\d+', os.path.basename(f))]
        sorted_files = [f[1] for f in sorted(numbered_files, key=lambda x: x[0])]
    else:
        sorted_files = sorted(image_files)

    if not sorted_files:
        raise ValueError(f"No {file_extension.upper()} files found in the directory: {directory}")
    else:
        print(f"Found and sorted {len(sorted_files)} {file_extension.upper()} files.")
    
    return sorted_files


def convert_to_pngs(image_files: List[str], dpi: int = 300) -> List[str]:
    """
    Converts a list of image files to PNG format, handling various input formats.
    
    Parameters
    ----------
    image_files : List[str]
        List of image file paths to convert.
    dpi : int, optional
        DPI (Dots Per Inch) resolution for the PNG output (applies to SVG conversions). Default is 300.

    Returns
    -------
    List[str]
        List of generated PNG file paths.
    """
    png_files = []
    
    for image in image_files:
        # Skip if the file is already in PNG format
        if image.lower().endswith('.png'):
            print(f"Skipping PNG file: {image}")
            png_files.append(image)
            continue

        # Handle SVG conversion using CairoSVG
        if image.lower().endswith('.svg'):
            png_filename = f"{os.path.splitext(image)[0]}.png"
            try:
                cairosvg.svg2png(url=image, write_to=png_filename, dpi=dpi)
                png_files.append(png_filename)
                print(f"Converted {image} (SVG) to {png_filename}")
            except Exception as e:
                print(f"Failed to convert {image} (SVG): {e}")
            continue

        # For other image formats, use PIL (Pillow) for conversion
        try:
            with Image.open(image) as img:
                png_filename = f"{os.path.splitext(image)[0]}.png"
                img.save(png_filename, 'PNG')
                png_files.append(png_filename)
                print(f"Converted {image} to {png_filename}")
        except Exception as e:
            print(f"Failed to convert {image}: {e}")

    return png_files



def create_gif(directory: str, output_filename: str, file_extension: str = "svg", dpi: int = 300, duration: int = 750, loop: int = 0):
    """
    Finds image files, converts non-PNG files to PNG, and creates an animated GIF.

    Parameters
    ----------
    directory : str
        Directory where the image files are located.
    output_filename : str
        Output filename for the GIF.
    file_extension : str, optional
        The type of image files to look for (e.g., 'svg', 'jpg', 'png'). Default is 'svg'.
    dpi : int, optional
        DPI (Dots Per Inch) resolution for the PNG output (applies to SVG conversions). Default is 300.
    duration : int, optional
        Duration in milliseconds for each frame in the GIF. Default is 750ms.
    loop : int, optional
        Number of loops for the GIF (0 for infinite loop). Default is 0.

    Returns
    -------
    None
    """
    # Step 1: Find all image files with the specified extension
    image_files = find_image_files(directory, file_extension=file_extension)

    if not image_files:
        print(f"No {file_extension.upper()} files found to process.")
        return

    # Step 2: Convert non-PNG files to PNG
    if file_extension != "png":
        print("Converting non-PNG files to PNG...")
        image_files = convert_to_pngs(image_files, dpi=dpi)

    # Step 3: Create GIF from PNG files
    images = [imageio.imread(img) for img in image_files]

    # Customise frame durations (e.g., first and last frame extended)
    durations = [duration] * len(images)
    if images:
        durations[0] = 2 * duration  # Double duration for the first frame
        durations[-1] = 4 * duration  # Quadruple duration for the last frame

    imageio.mimsave(output_filename, images, duration=durations, loop=loop)
    print(f"GIF saved as {output_filename}")
