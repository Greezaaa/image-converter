import os
from PIL import Image
from tqdm import tqdm

def get_user_input() -> tuple[str, int]:
    """
    Prompts the user to enter:
    - Folder path with images
    - Image quality for conversion

    Returns:
        tuple[str, int]: (Input folder path, Quality percentage between 0-100)
    """
    while True:
        input_folder = input("Enter the path to the input folder: ").strip()
        if not os.path.exists(input_folder):
            print(f"The folder '{input_folder}' does not exist. Please try again.")
            continue

        image_files = [f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        if not image_files:
            print(f"No supported image files found in '{input_folder}'. Please try again.")
            continue

        print(f"Found {len(image_files)} images to convert.")

        try:
            quality = int(input("Enter the quality for output images (0-100): ").strip())
            if 0 <= quality <= 100:
                return input_folder, quality
            else:
                print("Quality must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")

def convert_images(input_folder: str, quality: int) -> None:
    """
    Converts images from JPEG/PNG to WebP format with specified quality.

    Args:
        input_folder (str): Path to the folder containing images.
        quality (int): Compression quality (0-100).

    Returns:
        None
    """
    output_folder = os.path.join(input_folder, f"webp-{quality}")
    os.makedirs(output_folder, exist_ok=True)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif"))]

    for image_file in tqdm(image_files, desc="Converting images"):
        try:
            image_path = os.path.join(input_folder, image_file)
            image = Image.open(image_path)
            filename = os.path.splitext(image_file)[0]
            output_path = os.path.join(output_folder, f"{filename}.webp")
            image.save(output_path, "webp", quality=quality)
        except Exception as e:
            print(f"Error converting {image_file}: {e}")

    print(f"✅ Conversion complete! {len(image_files)} images saved in '{output_folder}'.")

def main() -> None:
    """
    Main entry point of the program.
    Handles user input and starts the image conversion process.

    Returns:
        None
    """
    print("=== Image Converter ===")
    input_folder, quality = get_user_input()
    convert_images(input_folder, quality)

if __name__ == "__main__":
    main()
