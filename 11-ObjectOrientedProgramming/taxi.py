class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
        print(f'Distance: {self.distance}')
        print(f'Rate: {self.rate_per_km}')
        print(f'Fare: {self.fare}\n')


def main():
    ride1 = TaxiRide(5)
    ride1.calculate_fare(20)
    ride1.print_receipt()
    
    ride2 = TaxiRide(4)
    ride2.calculate_fare(14)
    ride2.print_receipt()

if __name__ == "__main__":
    main()
