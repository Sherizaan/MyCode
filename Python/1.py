class Names:
	def __init__(self):
		self.name_list = []

	def list_options(self):
		print('\n1.\tAdd Name')
		print('2.\tDelete Name')
		print('3.\tList Names')
		print('4.\tClose Program\n')

	def run_interface(self):
		self.list_options()
		choice = int(input('\tChoose an option from the list above: '))
		print(choice)
		if choice == 1:
			add_item = input('\tName you want to add: ')
			self.add_Name(add_item)
			self.run_interface()
		elif choice == 2:
			delete_item = input('\tName you want to delete: ')
			self.delete_Name(delete_item)
			self.run_interface()
		elif choice == 3:
			self.print_Names()
			self.run_interface()
		elif choice == 4:
			print('Closing Program!')
	def add_Name(self, name):
		if name in self.name_list:
			print('{} is already in the list!'.format(name))
		else:
			self.name_list.append(name)
			print('{} was successfully added to the list!'.format(name))

	def delete_name(self, name):
		if name in self.name_list:
			self.name_list.pop(self.name_list.index(name))
			print('{} was successfully removed from the list!'.format(name))
		else:
			print('{} is not in the list of brands!'.format(name))

	def get_name(self):
		return self.name_list

	def print_names(self):
		if len(self.get_name()) == 0:
			print('\t\tName List\n')
			print('No Names listed')
		else:
			print('\t\tName List\n')
			for x in self.get_name():
				print(x)

start = Names()
start.run_interface()
#start.add_brand('BMW')
#start.add_brand('Bugatti')
#start.add_brand('Ford')
#start.add_brand('Ford')
#start.add_brand('Toyota')
#start.delete_brand('Ford')
#start.delete_brand('Ford')
#start.print_brands()