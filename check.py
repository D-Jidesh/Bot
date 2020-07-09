def find(search_word=""):
	filepath = 'labs.json'
	#search_word = input("Enter destination: ")
	search_word=search_word.replace(" ",'_')
	with open(filepath) as fp:
		line = fp.readline()
		cnt = 0
		while line:
			if cnt==1:
				break
			if search_word.lower() in line:
				temp = ("{}".format(line.strip()))
				cnt = 1
				temp=temp.replace(",","")
				temp=temp.replace("_"," ")
				return temp
				"""for i in range(0,len(temp)):
					if(temp[i]!='"' or temp[i]!=","):
						print(temp[i],end="")
				#for i in temp:
					#if(i != '"' or i != ','):
						#print(i,end="")"""
			line = fp.readline()
			
	"""print()	
	print("Do you want to view the map? Y/N")
	c=input()
	if(c=='Y' or c== 'y'):

		print("Showing map...")
		from PIL import Image
		image = Image.open('/home/silvercrow/Desktop/asta.jpg')
		image.show()"""
