from usda import UsdaClient
client=UsdaClient('YbjOfDNfLsdwRwAff2ZTtOXye6wR9KrZcWHjAPQ7')
foods_list = client.list_foods(5)
for _ in range(5):
	food_item = next(foods_list)
	print(food_item.name)
foods_search = client.search_foods('cabbage',1)
coffee=next(foods_search)
print(coffee)
report = client.get_food_report(coffee.id)
for nutrient in report.nutrients:
	print(nutrient.name,nutrient.value,nutrient.unit)