from PIL import Image
from pytesseract import pytesseract
from os import listdir

#Define path to tessaract.exe

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

# #Define path to image
# path_to_image = 'test2.png'

# #Open image with PIL
# img = Image.open(path_to_image)

# #Extract text from image
# text = pytesseract.image_to_string(img)

# # print(text)

# data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME)

# # print(data['text'][15])

# # for i in range(135):
# # 	print(data['level'][i])
# # 	print(data['block_num'][i])
# # 	print(data['par_num'][i])
# # 	print(data['word_num'][i])
# # 	print(data['text'][i])
# # 	print('=====')

# # block number 4 for "Active"
# # website from block 5

# # currentText = ''
# # text_by_rows = []

# # for i in range(len(data)):
# # 	if str(data['text'][i]) == 'nan':
# # 		if currentText != '':
# # 			text_by_rows.append(currentText)
# # 		currentText = ''
# # 	else:
# # 		currentText += ' '
# # 		currentText += str(data['text'][i])

# # for row in text_by_rows:	
# # 	print(row)
# # 	print('=====')





# currentRow = []
# text_by_rows = []

# for i in range(len(data)):
# 	if str(data['text'][i]) == 'nan':
# 		if len(currentRow) != 0:
# 			text_by_rows.append(currentRow)
# 		currentRow = []
# 	else:
# 		currentRow.append(str(data['text'][i]).lower())


# # for row in text_by_rows:	
# # 	print(row)
# # 	print('=====')



# look_for_status = True
# look_for_website = False
# look_for_money_statement = False
# look_for_founders = False


# money_keywords = ['$', 'dollar', 'dollars', 'million', 'millions', 'save', 'saving', 'saves', '%', 'reduces', 'reduce', 'billion', 'billions']
# money_statement_count = 0


# product_keywords = ['cpo', 'pm', 'product', 'cto']
# product_count = 0

# startup_knowledge_keywords = ['led', 'startup', 'ceo', 'cto', 'cpo', 'co-founded', 'manager']
# startup_knowledge_count = 0

# domain_knowledge_keywords = ['ai', 'artificial', 'medic', 'phd', 'patent', 'transport']
# domain_knowledge_count = 0


# title = ' '.join(text_by_rows[1])

# for row in text_by_rows:
# 	for i in range(len(row)):
# 		if look_for_status:
# 			if 's22' in row[i]:
# 				status = row[i+2]
# 				look_for_status = False
# 				look_for_website = True
# 		elif look_for_website:
# 			if 'http' in row[i] or 'www' in row[i]:
# 				website = row[i]
# 				look_for_website = False
# 				look_for_money_statement = True
# 		elif look_for_money_statement:
# 			if row[i] in money_keywords or '$' in row[i] or '%' in row[i]:
# 				money_statement_count += 1
# 		elif look_for_founders:
# 			if row[i] in product_keywords:
# 				product_count += 1
# 			if row[i] in startup_knowledge_keywords:
# 				startup_knowledge_count += 1
# 			if row[i] in domain_knowledge_keywords:
# 				domain_knowledge_count += 1

# 		if row[i] == 'jobs':
# 			if row[i+1] == 'at':
# 				look_for_money_statement = False
# 				look_for_founders = True
# 		if row[i] == 'company':
# 			if row[i+1] == 'launches':
# 				look_for_money_statement = False
# 				look_for_founders = True
# 		if row[i] == 'active':
# 			if row[i+1] == 'founders':
# 				look_for_money_statement = False
# 				look_for_founders = True
		
# print(f'title: {title}')
# print(f'status: {status}')
# print(f'website: {website}')
# print(f'money_statement_count: {money_statement_count}')
# print('==========')
# print('Founders: ')
# print(f'product_count: {product_count}')
# print(f'startup_knowledge_count: {startup_knowledge_count}')
# print(f'domain_knowledge_count: {domain_knowledge_count}')

# # Milestones

# # title -> second row

# # the second word after S22
# # S22 @ active_status

# # Company Jobs
# # http -> on the same row
# # ‘Company Jobs 0 @ https://wwwjambleapp.com/

# # Description
# # money statements
# # keywords: $, dollar, million, save, saving, saves, %, reduce, billion

# # JOBS AT
# # - 

# # COMPANY LAUNCHES
# # - 

# # ACTIVE FOUNDERS
# # product keywords: cpo, pm, product, cto
# # startup knowledge keywords : led, startup 2x, ceo 2x, cto 2x, cpo 2x, co-founded, manager 
# # domain-knowledge keywords: ai, artificial, medic, phd, patent, transport 2x, 


def run_on_all_images():

	my_path = './images'

	image_paths = listdir(my_path)

	image_paths = ['./images/' + str(img) for img in image_paths]

	for image_path in image_paths:

		#Open image with PIL
		img = Image.open(image_path)

		#Extract text from image
		text = pytesseract.image_to_string(img)


		data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DATAFRAME)


		currentRow = []
		text_by_rows = []

		for i in range(len(data)):
			if str(data['text'][i]) == 'nan':
				if len(currentRow) != 0:
					text_by_rows.append(currentRow)
				currentRow = []
			else:
				currentRow.append(str(data['text'][i]).lower())
				



		look_for_status = True
		look_for_website = False
		look_for_money_statement = False
		look_for_founders = False

		money_keywords = ['$', 'dollar', 'dollars', 'million', 'millions', 'save', 'saving', 'saves', '%', 'reduces', 'reduce', 'billion', 'billions']
		money_statement_count = 0


		product_keywords = ['cpo', 'pm', 'product', 'cto']
		product_count = 0

		startup_knowledge_keywords = ['led', 'startup', 'ceo', 'cto', 'cpo', 'co-founded', 'manager']
		startup_knowledge_count = 0

		domain_knowledge_keywords = ['ai', 'artificial', 'medic', 'phd', 'patent', 'transport']
		domain_knowledge_count = 0



		title = ' '.join(text_by_rows[1])
		print(f'title: {title}')

		for row in text_by_rows:
			for i in range(len(row)):
				if look_for_status:
					if 's22' in row[i]:
						status = row[i+2]
						print(f'status: {status}')

						look_for_status = False
						look_for_website = True

				elif look_for_website:
					if 'http' in row[i] or 'www' in row[i]:
						website = row[i]
						print(f'website: {website}')	

						look_for_website = False
						look_for_money_statement = True

				elif look_for_money_statement:
					if row[i] in money_keywords or '$' in row[i] or '%' in row[i]:
						money_statement_count += 1
				elif look_for_founders:
					if row[i] in product_keywords:
						product_count += 1
					if row[i] in startup_knowledge_keywords:
						startup_knowledge_count += 1
					if row[i] in domain_knowledge_keywords:
						domain_knowledge_count += 1

				try:
					if row[i] == 'jobs':
						if row[i+1] == 'at':
							look_for_money_statement = False
							look_for_founders = True
					if row[i] == 'company':
						if row[i+1] == 'launches':
							look_for_money_statement = False
							look_for_founders = True
					if row[i] == 'active':
						if row[i+1] == 'founders':
							look_for_money_statement = False
							look_for_founders = True
				except:
					continue


		print(f'money_statement_count: {money_statement_count}')
		print('==========')
		print('Founders: ')
		print(f'product_count: {product_count}')
		print(f'startup_knowledge_count: {startup_knowledge_count}')
		print(f'domain_knowledge_count: {domain_knowledge_count}')
		print('==================================================================')




run_on_all_images()
