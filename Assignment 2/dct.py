import numpy as np
from scipy.fftpack import dct, idct
from PIL import Image


def discrete_cosine_transform(a):
    return dct(dct(a, axis=0, norm='ortho'), axis=1, norm='ortho')


def inverse_discrete_cosine_transform(a):
    return idct(idct(a, axis=0, norm='ortho'), axis=1, norm='ortho')


def dct_image(input_image):
    img = Image.open(input_image)
    img_array = np.array(img, dtype=float)

    if len(img_array.shape) == 3:
        img_array = img_array.mean(axis=2)

    dct_coefficients = discrete_cosine_transform(img_array)
    return dct_coefficients


def save_dct_image(dct_image, output_path):
    normalized_dct = normalize_dct(dct_image)
    dct_img = Image.fromarray(normalized_dct.astype(np.uint8))
    dct_img.save(output_path)


def normalize_dct(dct_image):
    min_val = np.min(dct_image)
    max_val = np.max(dct_image)
    normalized_dct = 255 * (dct_image - min_val) / (max_val - min_val)
    normalized_dct = np.clip(normalized_dct, 0, 255)
    return normalized_dct.astype(np.uint8)


if __name__ == "__main__":
    input_image_path = "input_image.jpeg"
    output_image_path = "dct_image.jpeg"

    try:
        dct_image = dct_image(input_image_path)
        save_dct_image(dct_image, output_image_path)
        print("DCT operation completed and saved to", output_image_path)
    except Exception as e:
        print("An error occurred:", str(e))
