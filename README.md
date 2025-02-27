# Image Converter

Python script to convert `JPEG`, `JPG`, and `PNG` images to `WebP` format while allowing users to set image quality.

## Version

**v1.0.0**

## Installation

Make sure you have **Python 3.10+** installed.

### 1. Clone the repository
```bash
git clone https://github.com/Greezaaa/image-converter
cd image-converter
```

Create virtual environment
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate       # Windows
```

Then, install the required dependencies:

```sh
pip install -r requirements.txt
``` 

## Usage
Run the script and follow the prompts:

```sh 
python app.py
```

### You'll be asked to:

1. Enter the path to the folder containing images.
2. Specify the output quality (0-100).

Converted images will be saved in a subfolder named webp-[quality] inside the original folder.

## Features
✅ Supports .jpg, .jpeg, and .png

✅ Converts images to .webp

✅ Customizable quality

✅ Progress bar with tqdm

✅ Automatic folder creation

## Error Handling
- If the input folder doesn't exist → ❌ Error message + Retry prompt.
- If the folder contains no supported images → ❌ Error message + Retry prompt.
- Invalid quality values → ❌ Error message + Retry prompt.
- Conversion errors → Logs the filename and the error.

### Example Output
```sh 
=== Image Converter ===
Enter the path to the input folder: /path/to/images
Found 10 images to convert.
Enter the quality for output images (0-100): 80
Converting images: 100%|███████████████| 10/10 [00:03<00:00, 3.29it/s]
Conversion complete! 10 images saved in '/path/to/images/webp-80'.
```

## Folder structure
```
📁 image_converter/
├─ image_converter.py
├─ README.md
└─ requirements.txt
``` 

## Roadmap

Planned features for future versions:

- [ ] Automatically convert images inside subfolders  
- [ ] Resize images during conversion (optional)  
- [ ] Support more output formats like `PNG`, `JPEG`, or `TIFF`  
- [ ] Command-line usage without asking questions  
- [ ] Remove metadata (camera info, GPS location, etc.) 

## License
MIT License


### Made with ❤️ Jeka