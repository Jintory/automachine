import glob
import os
import sys
import logging
import shutil
import CaptchaCracker as cc

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def process_multiple_targets():
    try:
        img_width = 200
        img_height = 50
        max_length = 6
        characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        
        user_home = os.path.expanduser("~")
        weight_path = os.path.join(user_home, "Documents", "weight.h5")
        
        logging.info(f"Attempting to load model with weights from {weight_path}")
        AM = cc.ApplyModel(weight_path, img_width, img_height, max_length, characters)
        
        input_dir = "sample/test_numbers_only"
        output_dir = "sample/decoded_results"
        
        # 출력 디렉토리가 없으면 생성
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        target_img_paths = glob.glob(os.path.join(input_dir, "target (*).png"))
        logging.info(f"Found {len(target_img_paths)} target images")
        
        for img_path in target_img_paths:
            try:
                logging.info(f"Processing image: {img_path}")
                pred = AM.predict(img_path)
                logging.info(f"Prediction result for {os.path.basename(img_path)}: {pred}")
                
                # 새 파일 이름 생성 및 복사
                new_filename = f"{pred}.png"
                new_filepath = os.path.join(output_dir, new_filename)
                shutil.copy2(img_path, new_filepath)
                logging.info(f"Created new file: {new_filepath}")
            
            except Exception as e:
                logging.error(f"Error processing {img_path}: {e}")
    
    except Exception as e:
        logging.error(f"Error in process_multiple_targets: {e}")
        logging.error(f"Error type: {type(e).__name__}")
        logging.error(f"Error details: {str(e)}")
        logging.error(f"Stack trace: {sys.exc_info()}")

if __name__ == "__main__":
    process_multiple_targets()