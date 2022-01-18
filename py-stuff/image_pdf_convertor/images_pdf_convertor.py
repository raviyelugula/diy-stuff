#################################  Objective  ############################################
### Read all the files in a given inputs folder location and convert images into pdf file
### take the inputs foldername and output pdf file name as run time parameters

################################# Execution ##############################################
### python3 images_pdf_convertor.py aws_prep aws_prep_material_50 50

##########################################################################################

import glob
import img2pdf
import sys
from PIL import Image

if __name__ == "__main__":
	if len(sys.argv) < 4:
		print('Error encountered, the code is expecting 2 parameters \n1. inputs foldername\n2. output filename\n3. the quality of the pictures(0-100)')
	else: 
                output_filename = sys.argv[2]
                input_foldername = sys.argv[1]
                image_quality = sys.argv[3]
                
                jpg_files_list_original = []
                jpg_files_list_processed = []
                width = []
                height = []
                
                # read all the images and collect the individual images width and height
                for image_filename in glob.glob("inputs/"+input_foldername+"/*.jpg"):
                    jpg_files_list_original.append(image_filename)
                    image = Image.open(image_filename)
                    width.append(image.size[0])
                    height.append(image.size[1])

                # sorting the images to get the right order.
                # sorting width and height to get the 85% (percentile) values. to make all images look same size
                jpg_files_list_original.sort()
                width.sort()
                height.sort()

                common_width = width[int(len(width)*0.85)]
                common_height = height[int(len(height)*0.85)]
               
                # processing the image to get lower resolution and also same width and height (80%)
                for image_filename in jpg_files_list_original:
                    image = Image.open(image_filename)
                    image = image.resize((common_width, common_height))
                    image.save("temp/"+image_filename.split('/')[-1], quality = int(image_quality))
                    jpg_files_list_processed.append("temp/"+image_filename.split('/')[-1])

                # pdf conversion based on processed files
                with open('outputs/'+output_filename+'.pdf','wb') as f:
                    f.write(img2pdf.convert(jpg_files_list_processed))
                print('program completed')

 
