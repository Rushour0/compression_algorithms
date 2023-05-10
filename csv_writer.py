import csv


class CSVWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'w')
        self.writer = csv.writer(self.file)
        self.writer.writerow(('Original File Size', 'Compressed File Size', 'Image Format', 'Compression Time', 'Compression Ratio', 'RMS Error'))
        self.file.flush()

    def write(self, original_file_size, compressed_file_size, compression_time,  img_format, compression_ratio, rms_error):
        
        self.writer.writerow(
            (
                original_file_size,
                compressed_file_size,
                img_format,
                compression_time,
                compression_ratio,
                rms_error
            )
        )
