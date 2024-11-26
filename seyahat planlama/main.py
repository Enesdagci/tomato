# Menü sınıfı oluşturulacak ve kullanıcıdan girdi alınacak
from sub_classes.sub_class_bus import BusReservation
from sub_classes import FlightReservation
from sub_classes.sub_class_hotel import HotelReservation

class Menu:
    def reservation_add(value):
        if 1 == value:
            name = int(input("Rezervasyon numarasını giriniz: "))
            customer = (input("Müşteri numarasını giriniz: "))
            date = input("Rezervasyon tarihini giriniz: ")
            price = int(input("Fiyat giriniz: "))
            flight_number = int(input("Uçuş numarasını giriniz: "))
            obj = FlightReservation(name,customer,date,price,flight_number)
            return obj
        if 2 == value:
            name = int(input("Rezervasyon numarasını giriniz: "))
            customer = (input("Müşteri numarasını giriniz: "))
            date = input("Rezervasyon tarihini giriniz: ")
            price = int(input("Fiyat giriniz: "))
            seat_number= int(input("Koltuk numarasını giriniz: "))
            obj = FlightReservation(name,customer,date,price,seat_number)
            return obj
        if 3 == value:
            name = int(input("Rezervasyon numarasını giriniz: "))
            customer = (input("Müşteri numarasını giriniz: "))
            date = input("Rezervasyon tarihini giriniz: ")
            price = int(input("Fiyat giriniz: "))
            room_type = input("Oda tipini giriniz: ")
            obj = FlightReservation(name,customer,date,price,room_type)
            return obj
            

    def reservation_detail_list():
        BusReservation.displayDetails()
        FlightReservation.displayDetails()
        HotelReservation.displayDetails()

    def reservation_numbers():
        return 
    
if __name__ == "__main__":
    c1 = FlightReservation(1,1,"21/12/2020",125,121)
    c2 =BusReservation(1,2,"12/11/2010",75,16)
    c3 = HotelReservation(1,3,"12/12/2020",750,"3 yataklı oda")
    # print(c1.getter())
    # c1.setter(2,1,"25/11/2023",250,141)
    # print(c1.getter())

    # print(c2.getter())
    # c2.setter(2,2,"15/11/2023",150,19)
    # print(c2.getter())

    # print(c3.getter())
    # c3.setter(2,3,"10/09/2024",450,"2 yataklı oda")
    # print(c3.getter())

    print("Seyahat Planner")
    x = Menu()
    print("1. Uçuş seyahati")
    print("2. Otobüs Seyahati")
    print("3. Otel rezervasyonu")
    print("4. Rezervasyonun detayların göster")
    print("5. Rezervasyon sayısını göster")


    y = input("Yapmak istediğiniz işlemi giriniz: ")
    if y == 1:
        x.reservation_add(y)
    elif y == 2:
        x.reservation_add(y)
    elif y == 3:
        x.reservation_add(y)
    elif y ==  4:
        x.reservation_detail_list()
    elif y == 5:
        x.reservation_numbers()