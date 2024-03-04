from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name", ["Indrajit", "Atul", "Shubham", "Gayatri", "Pranita", "Pramod"])
table.add_column("Occupation", ["IT ENGG", "Auto Engg", "Footware Products", "HouseWife", "IT ENGG", "Tour and Travels Bussiness"])


print(table)