from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
# Read in the data
df = pd.read_csv('params.csv')

# X = []

# for i, size in enumerate(df['Original File Size']):
#     if i % 5 == 0:
#         X.append(f"{size / (1024*1024):.2f}MB")


# for type in df['Image Format'].unique():
#     plt.plot(X, df[df['Image Format'] == type]
#              ['Compression Ratio'], label=type)


# plt.xlabel("File Size")
# plt.ylabel("Compression Ratio")
# plt.title("Compression Ratio vs File Size")

# # Adding legend, which helps us recognize the curve according to it's color
# plt.legend()

# # To load the display window
# plt.show()
# plt.savefig('compression_ratio.png')

# plt.clf()

# for type in df['Image Format'].unique():
#     plt.plot(X, df[df['Image Format'] == type]
#              ['Compression Time'], label=type)

# plt.xlabel("File Size")
# plt.ylabel("Compression Time")
# plt.title("Compression Time vs File Size")


# plt.legend()
# # To load the display window
# plt.show()
# plt.savefig('compression_time.png')

# plt.clf()

data = {}

for format in df['Image Format'].unique():
    if format not in data:
        data[format] = sum(
            map(float, df['Compression Ratio'].loc[df['Image Format'] == format])) / 14

pprint(data)
# plt.bar(data.keys(),data.values())

# plt.show()