class Cars:
	def __init__(self):
		self.car_list = []

	def list_options(self):
		print('\n1.\tAdd Brand')
		print('2.\tDelete Brand')
		print('3.\tList Brands')
		print('4.\twrite brands to TextFile')
		print('5.\tClose Program\n')

	def run_interface(self):
		self.list_options()
		choice = int(input('\tChoose an option from the list above: '))
		print(choice)
		if choice == 1:
			add_item = input('\tBrand you want to add: ')
			self.add_brand(add_item)
			self.run_interface()
		elif choice == 2:
			delete_item = input('\tBrand you want to delete: ')
			self.delete_brand(delete_item)
			self.run_interface()
		elif choice == 3:
			self.print_brands()
			self.run_interface()
		elif choice==4:
			self.write_to_file()
			self.run_interface()
		elif choice == 5:
			print('Closing Program!')
	def add_brand(self, brand):
		if brand in self.car_list:
			print('{} is already in the list!'.format(brand))
		else:
			self.car_list.append(brand)
			print('{} was successfully added to the list!'.format(brand))

	def delete_brand(self, brand):
		if brand in self.car_list:
			self.car_list.pop(self.car_list.index(brand))
			print('{} was successfully removed from the list!'.format(brand))
		else:
			print('{} is not in the list of brands!'.format(brand))

	def get_brand(self):
		return self.car_list

	def print_brands(self):
		if len(self.get_brand()) == 0:
			print('\t\tCar List\n')
			print('No Cars listed')
		else:
			print('\t\tCar List\n')
			for x in self.get_brand():
				print(x)
	def write_to_file(self):
		f = open("CarBrands.txt", "w")
		list_string=""
		for x in self.get_brand():
			list_string=list_string + x + "\n"
		f.write(list_string)
		f.close()
		print("Brand List was written to the text file")
start = Cars()
start.run_interface()
#start.add_brand('BMW')
#start.add_brand('Bugatti')
#start.add_brand('Ford')
#start.add_brand('Ford')
#start.add_brand('Toyota')
#start.delete_brand('Ford')
#start.delete_brand('Ford')
#start.print_brands()