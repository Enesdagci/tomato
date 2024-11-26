
class Reservation:
    def __init__(self,reservation_id,customer_id,reservation_date,price):
        self.__reservation_id = reservation_id
        self.__customer_id = customer_id
        self.__reservation_date = reservation_date
        self.__price = price

    def setter(self,reser_num,custom_num,date,value):
        self.__reservation_id = reser_num
        self.__customer_id = custom_num
        self.__reservation_date = date
        self.__price = value
        return self.__reservation_id,self.__customer_id,self.__reservation_date,self.__price

    
    # def getter(self):
    #     return f"Reservation Id: {self.__reservation_id}, Customer Id: {self.__customer_id}, Reservation date: {self.__resrevation_date}, Price: {self.__price}"
    
    def getter(self):
        return self.__reservation_id,self.__customer_id,self.__reservation_date,self.__price
    