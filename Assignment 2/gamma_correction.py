from PIL import Image
import numpy as np


def gamma_correct(input_image, gamma):

    img = Image.open(input_image)
    img_array = np.array(img)
    img_normalized = img_array / 255.0
    gamma_image = img_normalized ** (1.0 / gamma)
    gamma_image = (gamma_image * 255).astype(np.uint8)
    gamma_img = Image.fromarray(gamma_image)
    return gamma_img


def save_image_function(input_image, output_image_path):
    input_image.save(output_image_path)


if __name__ == "__main__":
    input_image_path = "input_image.jpeg"
    output_image_path = "gamma_correction.jpeg"
    gamma_value = 2.0

    try:
        gamma_image = gamma_correct(input_image_path, gamma_value)
        save_image_function(gamma_image, output_image_path)
        print("The process is successfull. The gamma correction applied to the image and saved to ", output_image_path)
    except Exception as e:
        print("The process is failured. An error has occurred:", str(e))
