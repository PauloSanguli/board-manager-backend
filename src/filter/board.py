"""extract text from image with pytesseract"""
from PIL import Image
import pytesseract

import os



class ProcessImage:
    @staticmethod
    def extract_text(img: str) -> None:
        # """read text"""
        
        # try:
        #     pytesseract.pytesseract.\
        #         tesseract_cmd = "C://Users//Paulo Sanguli//AppData//Local//Programs//Tesseract-OCR//tesseract.exe"
                

                
        #     text_image = pytesseract.\
        #         image_to_string(Image.open(img))
        #     print(f"[INFO]: EXTRATING TEXT FROM IMAGE NAME '{img}'...")
        # except Exception as error:
        #     print("Image or cmd tesseract dont finded! {}".format(error))
        # else:    
        #     ProcessImage.write_txt(
        #         text=text_image,
        #         dir_image=img[0:img.rfind(".")]
        #     )
        #     return text_image
        import aspose.ocr as ocr

        # Instantiate Aspose.OCR API
        api = ocr.AsposeOcr()

        # Add image to the recognition batch
        input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE)
        input.add("test.png")

        # Recognize the image
        result = api.recognize_car_plate(input)

        # Print recognition result
        print(result[0].recognition_text)
            
    @staticmethod
    def write_txt(text: str, dir_image) -> None:
        """write in txt file"""
        with open(f"{dir_image}.txt", "w") as file:
            file.writelines(text)
            file.close()
        print("[INFO]: TEXT EXTRACTED WITH SUCESS AND SAVED!")
        print(f"[INFO]: TEXT EXTRACTED SAVED IN '{dir_image.upper()}'")
