from Base_classes.base_class import Reservation

class FlightReservation(Reservation):
    reservation_num = 0
    
    def __init__(self,reservation_id,customer_id,reservation_date,price,flight_number):
        super().__init__(reservation_id,customer_id,reservation_date,price)
        self.__flight_number = flight_number
    
    def setter(self,reser_num,custom_num,date,price,flight_num):
        super().setter(reser_num,custom_num,date,price)
        self.__flight_number = flight_num
        self.__flight_number
        return self.__flight_number

    def getter(self):
        return super().getter() , self.__flight_number
    
    def  displayDetails(self):
        return f"Reservation: {self.__reservation_id}, customer Id: {self.__customer_id}, reservation date: {self.__reservation_date}, price: {self.__price}, flight number: {self.__flight_num} "

    def addDetails(self,attr):
        return self.displayDetails().join(attr)
         

    @staticmethod
    def  getTotalFlightReservations(value):
        value += 1
        return value
    

