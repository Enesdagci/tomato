from Base_classes.base_class import Reservation

class BusReservation(Reservation):
    reservation_number = 0

    def __init__(self,reservation_id,customer_id,reservation_date,price,seat_number):
        super().__init__(reservation_id,customer_id,reservation_date,price)
        self.__seat_number = seat_number
    
    def setter(self,reser_num,custom_num,date,price,seat_num):
        super().setter(reser_num,custom_num,date,price)
        self.__seat_number = seat_num

    def getter(self):
        return super().getter() , self.__seat_number
    
    def  displayDetails(self):
        return f"Reservation: {self.__reservation_id}, customer Id: {self.__customer_id}, reservation date: {self.__reservation_date}, price: {self.__price}, flight number: {self.__flight_num} "

    def addDetails(self,attr):
        return self.displayDetails().join(attr)
         
    @staticmethod
    def  getTotalBusReservations():
        value += 1
        return value