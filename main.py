import csv
import os
from os import listdir

class Category:	
	def __init__(self, file, name):
		self.total = 0	
		self.name = name
		self.keywords = []
		
		with open(file) as lines:
			for line in lines:
				self.keywords.append(line.strip())
				
	def handleInput(self, input, value):	
		containsInput = False
		
		input_lower = input.lower()
		
		for keyword in self.keywords:
			if keyword in input_lower:
				self.total += value
				
				containsInput = True
		
		return containsInput

#initialize categories from text files
categoryDir = "categories/"
categoryFiles = os.listdir(categoryDir)
currentDir = os.getcwd()

csvFiles = os.listdir(os.getcwd() + "/input")


for fileName in csvFiles:
	if not fileName.endswith(".csv"): 
		continue
	
	#init values
	categories = []
	for file in categoryFiles:
		categories.append(Category(currentDir + "/" + categoryDir + file, file))
	
	undefinedTotal = 0
		
	with open('input/' + fileName, newline='') as csvfile:
			reader = csv.DictReader(csvfile)
			
			for row in reader:
				entry = row['Bedrag']
				entry = entry.replace(',','.')
				value = float(entry)
				
				#Only for values that had to be paid for
				if value < 0:			
					name = row['Naam tegenpartij']	
					
					containsInput = False
					
					#handle event category
					for category in categories:
						if category.handleInput(name, value) == True:
							containsInput = True
					
					if not containsInput:
						#print(name, value)
						undefinedTotal += value

	print("***Overview " + fileName + " ***")
	for category in categories:
		print("%s %d" % ("Total cost (" + category.name +")", + category.total))
	print("%s %d" % ("Total cost (other) ", undefinedTotal))
	print("\n\n\n")
input()