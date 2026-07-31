class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
class Cart:
    def __init__(self):
        self.__items = []
    def add_item(self, product, quantity):
        self.__items.append([product, quantity])
        print("Product Added Successfully!")
    def remove_item(self, product_id):
        for item in self.__items:
            if item[0].product_id == product_id:
                self.__items.remove(item)
                print("Product Removed Successfully!")
                return
        print("Product Not Found")
    def display_cart(self):
        if len(self.__items) == 0:
            print("Cart is Empty")
            return
        print("\nID\tProduct\tQuantity\tPrice\tTotal")
        for item in self.__items:
            product = item[0]
            quantity = item[1]
            total = product.price * quantity
            print(product.product_id, "\t", product.name, "\t", quantity,
                  "\t\t", product.price, "\t", total)
    def calculate_total(self):
        total = 0
        for item in self.__items:
            total += item[0].price * item[1]
        return total
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = Cart()
    def checkout(self):
        total = self.cart.calculate_total()
        print("Total Amount =", total)
class PremiumCustomer(Customer):
    def checkout(self):
        total = self.cart.calculate_total()
        discount = total * 0.10
        final_amount = total - discount
        print("Total Amount =", total)
        print("Discount (10%) =", discount)
        print("Final Amount =", final_amount)
class Order:
    order_no = 1001

    def place_order(self, customer):
        print("\n===== ORDER SUMMARY =====")
        customer.cart.display_cart()
        customer.checkout()
        print("Order Number:", Order.order_no)
        print("Order Placed Successfully!")
        Order.order_no += 1
products = [
    Product(101, "Laptop", 50000),
    Product(102, "Mouse", 500),
    Product(103, "Keyboard", 1200),
    Product(104, "Headphones", 2000),
]

print("1. Normal Customer")
print("2. Premium Customer")
choice = int(input("Enter Choice: "))
cid = input("Enter Customer ID: ")
name = input("Enter Customer Name: ")

if choice == 1:
    customer = Customer(cid, name)
else:
    customer = PremiumCustomer(cid, name)

while True:
    print("\n====== ONLINE SHOPPING CART ======")
    print("1. View Products")
    print("2. Add Product")
    print("3. Remove Product")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        print("\nID\tProduct\t\tPrice")
        for p in products:
            print(p.product_id, "\t", p.name, "\t\t", p.price)
    elif ch == 2:
        pid = int(input("Enter Product ID: "))
        qty = int(input("Enter Quantity: "))
        found = False
        for p in products:
            if p.product_id == pid:
                customer.cart.add_item(p, qty)
                found = True
                break
        if not found:
            print("Product Not Found")
    elif ch == 3:
        pid = int(input("Enter Product ID to Remove: "))
        customer.cart.remove_item(pid)
    elif ch == 4:
        customer.cart.display_cart()
    elif ch == 5:
        order = Order()
        order.place_order(customer)
    elif ch == 6:
        print("Thank You for Shopping!")
        break
    else:
        print("Invalid Choice")