import os
import time
from utils import png_compression, jpeg_compression, webp_compression, gif_compression, bmp_compression

from tqdm import tqdm

def main():
    for file_name in tqdm(os.listdir('ppm_images')):
        png_compression(f'ppm_images/{file_name}')
        jpeg_compression(f'ppm_images/{file_name}')
        webp_compression(f'ppm_images/{file_name}')
        gif_compression(f'ppm_images/{file_name}')
        bmp_compression(f'ppm_images/{file_name}')
    
    for file_name in tqdm(os.listdir('ppm_images'), desc='Calculating rms_error'):
        os.system(f'python calculate_error.py ppm_images/{file_name}')

main()