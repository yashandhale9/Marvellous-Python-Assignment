class Vehicle:
    def start(self):
        print("Vehicle start..")

class Car(Vehicle):
    def start(self):
        print("Car is starting..")
        print("Drive carefully....")

def main():
    print("Using Vehicle object:")
    obj1 = Vehicle()
    obj1.start()  

    print("\nUsing Car object:")
    obj1 = Car()
    obj1.start()  

if __name__ == "__main__":
    main()
