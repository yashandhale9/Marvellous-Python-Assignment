class Product:
    def __init__(self, pname, pprice):
        self.name = pname
        self.price = pprice

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

    def display(self):
        print(f"Product Name: {self.name}, Price: ₹{self.price}")

def main():
    obj1 = Product("Mobile", 100000)
    obj2 = Product("Laptop", 200000)

    obj1.display()
    obj2.display()
    
    print("Comparing...")
    if obj1 == obj2:
        print("Product 1 and 2 have same price.")
    else:
        print("Product 1 and 2 have different prices.")


if __name__ == "__main__":
    main()
