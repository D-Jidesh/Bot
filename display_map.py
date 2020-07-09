def show_map(c):
	
	if(c=="Y" or c== "y"):

		print("Showing map...")
		from PIL import Image
		image = Image.open('/home/silvercrow/Downloads/college_2.jpg')
		image.show()
        
