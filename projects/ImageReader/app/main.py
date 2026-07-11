from pathlib import Path
from app.utils import get_images
from app.ocr import run_ocr

def main():

    input_folder = Path("data/input")
    all_images = get_images(input_folder)

    print("All images found in the input folder:")
    for img_path in all_images:
        print(img_path.name)

    ocr_results = run_ocr(all_images)
    print("\nOCR Results:")
    for res in ocr_results:
        print(f"图片：{res['image_file']}")
        print(f"识别文字：{res['ocr_text']}\n")

if __name__ == "__main__":
    main()