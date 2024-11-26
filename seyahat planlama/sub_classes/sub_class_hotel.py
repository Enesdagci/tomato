from Base_classes.base_class import Reservation

class HotelReservation(Reservation):
    reservation_number = 0

    def __init__(self,reservation_id,customer_id,reservation_date,price,room_type):
        super().__init__(reservation_id,customer_id,reservation_date,price)
        self.__room_type = room_type
    
    def setter(self,reser_num,custom_num,date,price,room_type):
        super().setter(reser_num,custom_num,date,price)
        self.__room_type = room_type
        return self.__room_type

    def getter(self):
        return super().getter() , self.__room_type

    def  displayDetails(self):
        return f"Reservation: {self.__reservation_id}, customer Id: {self.__customer_id}, reservation date: {self.__reservation_date}, price: {self.__price}, flight number: {self.__flight_num} "

    def addDetails(self,attr):
        return self.displayDetails().join(attr)
         
    @staticmethod
    def  getTotalFlightReservations(reservation_number):
        reservation_number += 1
        return reservation_number
 
