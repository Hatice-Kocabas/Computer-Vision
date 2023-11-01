from PIL import Image
import numpy as np


def detect_edges_with_prewitt(input_image):
    img = Image.open(input_image)

    img_array = np.array(img)

    if len(img_array.shape) == 3:
        img_array = img_array.mean(axis=2).astype(np.uint8)

    x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    edge_x = apply_kernel(img_array, x)
    edge_y = apply_kernel(img_array, y)

    gradient_magnitude = np.sqrt(edge_x**2 + edge_y**2)

    gradient_magnitude = (gradient_magnitude /
                          gradient_magnitude.max() * 255).astype(np.uint8)

    edge_image = Image.fromarray(gradient_magnitude)

    return edge_image


def apply_kernel(input_image, kernel):
    image_height, image_width = input_image.shape
    kernel_height, kernel_width = kernel.shape
    result = np.zeros_like(input_image)

    for i in range(image_height - kernel_height + 1):
        for j in range(image_width - kernel_width + 1):
            image_patch = input_image[i:i+kernel_height, j:j+kernel_width]
            result[i, j] = np.sum(image_patch * kernel)

    return result


def save_image(input_image, output_path):
    input_image.save(output_path)


if __name__ == "__main__":
    input_image_path = "input_image.jpeg"  # Provide the path to your input image
    # Provide the desired output path
    output_image_path = "prewit_edge_detection.jpeg"

    try:
        edge_image = detect_edges_with_prewitt(input_image_path)
        save_image(edge_image, output_image_path)
        print("The process is successfully completed! Prewitt edge detection completed and saved to", output_image_path)
    except Exception as e:
        print("An error occurred:", str(e))
