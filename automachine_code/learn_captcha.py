# learn_captcha.py

import glob
import os
import sys
import logging
import CaptchaCracker as cc

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def learn_img():
    try:
        train_img_path_list = glob.glob("sample/train_numbers_only/*.png")
        logging.info(f"Found {len(train_img_path_list)} training images")
        
        img_width = 200
        img_height = 50
        
        logging.info("Creating model")
        CM = cc.CreateModel(train_img_path_list, img_width, img_height)
        
        logging.info("Starting model training")
        model = CM.train_model(epochs=100)
        
        user_home = os.path.expanduser("~")
        weight_path = os.path.join(user_home, "Documents", "weight.h5")
        
        logging.info(f"Attempting to save weights to {weight_path}")
        model.save_weights(weight_path)
        logging.info("Weights saved successfully")
    
    except Exception as e:
        logging.error(f"Error in learn_img: {e}")
        logging.error(f"Error type: {type(e).__name__}")
        logging.error(f"Error details: {str(e)}")
        logging.error(f"Stack trace: {sys.exc_info()}")

if __name__ == "__main__":
    learn_img()