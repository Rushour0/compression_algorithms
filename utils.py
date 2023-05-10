from csv_writer import CSVWriter
from PIL import Image
import time
import os
import sys
sys.path.append('ppm_images')
# GIF, WebP, JPEG, BMP, and PNG

# GIF Compression


writer = CSVWriter('params.csv')


def gif_compression(file_name: str):
    original_file_name = file_name
    start_time = time.time()
    im = Image.open(file_name)
    original_file_size = os.path.getsize(file_name)

    file_name = file_name.split('.')[0].split('/')[1]

    im.save(f"compressed/gif/{file_name}.gif")
    total_time = time.time() - start_time

    compressed_file_size = os.path.getsize(f"compressed/gif/{file_name}.gif")

    # rms_error = calculate_rms_error(
    #     original_file_name, f"compressed/gif/{file_name}.gif")

    writer.write(original_file_size, compressed_file_size,
                 total_time, 'gif', original_file_size / compressed_file_size, 0)


# WebP Compression


def webp_compression(file_name: str):
    original_file_name = file_name
    start_time = time.time()
    im = Image.open(file_name)
    original_file_size = os.path.getsize(file_name)

    file_name = file_name.split('.')[0].split('/')[1]

    im.save(f"compressed/webp/{file_name}.webp")
    total_time = time.time() - start_time

    compressed_file_size = os.path.getsize(f"compressed/webp/{file_name}.webp")

    rms_error = calculate_rms_error(
        original_file_name, f"compressed/webp/{file_name}.webp")

    writer.write(original_file_size, compressed_file_size, total_time,
                 'webp', original_file_size / compressed_file_size, rms_error)


# JPEG Compression


def jpeg_compression(file_name: str):
    original_file_name = file_name
    start_time = time.time()
    im = Image.open(file_name)
    original_file_size = os.path.getsize(file_name)

    file_name = file_name.split('.')[0].split('/')[1]

    im.save(f"compressed/jpeg/{file_name}.jpeg")
    total_time = time.time() - start_time

    compressed_file_size = os.path.getsize(f"compressed/jpeg/{file_name}.jpeg")

    rms_error = calculate_rms_error(
        original_file_name, f"compressed/jpeg/{file_name}.jpeg")

    writer.write(original_file_size, compressed_file_size, total_time,
                 'jpeg', original_file_size / compressed_file_size, rms_error)


# PNG Compression


def png_compression(file_name: str):
    original_file_name = file_name
    start_time = time.time()
    im = Image.open(file_name)
    original_file_size = os.path.getsize(file_name)

    file_name = file_name.split('.')[0].split('/')[1]

    im.save(f"compressed/png/{file_name}.png")
    total_time = time.time() - start_time

    compressed_file_size = os.path.getsize(f"compressed/png/{file_name}.png")

    rms_error = calculate_rms_error(
        original_file_name, f"compressed/png/{file_name}.png")

    writer.write(original_file_size, compressed_file_size, total_time,
                 'png', original_file_size / compressed_file_size, rms_error)


# BMP Compression


def bmp_compression(file_name: str):
    original_file_name = file_name
    start_time = time.time()
    im = Image.open(file_name)
    original_file_size = os.path.getsize(file_name)

    file_name = file_name.split('.')[0].split('/')[1]

    im.save(f"compressed/bmp/{file_name}.bmp")
    total_time = time.time() - start_time

    compressed_file_size = os.path.getsize(f"compressed/bmp/{file_name}.bmp")

    rms_error = calculate_rms_error(
        original_file_name, f"compressed/bmp/{file_name}.bmp")

    writer.write(original_file_size, compressed_file_size, total_time,
                 'bmp', original_file_size / compressed_file_size, rms_error)


def calculate_rms_error(original_image, compressed_image):
    """
    Calculate the RMS error between two images.
    """
    original_image = Image.open(original_image)
    compressed_image = Image.open(compressed_image)
    width, height = original_image.size
    rms_error = 0
    for x in range(width):
        for y in range(height):
            r1, g1, b1 = original_image.getpixel((x, y))
            r2, g2, b2 = compressed_image.getpixel((x, y))
            rms_error += ((r1 - r2) ** 2 + (g1 - g2) ** 2 +
                          (b1 - b2) ** 2) / (width * height)
    rms_error = rms_error ** 0.5
    return rms_error
