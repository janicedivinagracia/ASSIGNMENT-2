class Shop:
    def __init__(self, name, description, categories, items, url):
        self.name = name
        self.description = description
        self.categories = categories
        self.items = items
        self.url = url
        self.shopping_cart = []

    def viewCategory(self, category):
        if category in self.categories:
            items_in_category = [item for item in self.items if item['category'] == category]
            print(f"Items in category '{category}':")
            for item in items_in_category:
                print(f"- {item['name']}")
        else:
            print(f"Category '{category}' not found.")

    def searchItems(self, query):
        matching_items = [item for item in self.items if query.lower() in item['name'].lower()]
        print(f"Search results for '{query}':")
        for item in matching_items:
            print(f"- {item['name']} ({item['category']}) - {item['price']}")

    def viewItem(self, item_name):
        item = next((item for item in self.items if item['name'].lower() == item_name.lower()), None)
        if item:
            print(f"Item: {item['name']} ({item['category']})")
            print(f"Description: {item['description']}")
            print(f"Price: {item['price']}")
        else:
            print(f"Item '{item_name}' not found.")

    def viewShoppingCart(self):
        if self.shopping_cart:
            print("Shopping cart:")
            total_price = 0
            for item in self.shopping_cart:
                print(f"- {item['name']} ({item['category']}) - {item['price']}")
                total_price += item['price']
            print(f"Total price: {total_price}")
        else:
            print("Shopping cart is empty.")

