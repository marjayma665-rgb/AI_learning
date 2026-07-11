from pathlib import Path

def run_ocr(images: list[Path]) -> list[dict]:

    ocr_result_list = []
    for img_path in images:
        mock_text = f"Mock OCR result for {img_path.name}"
        single_result = {
            "image_file": img_path.name,
            "ocr_text": mock_text
        }
        ocr_result_list.append(single_result)

    return ocr_result_list