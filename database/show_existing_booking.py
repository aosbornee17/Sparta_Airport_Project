import time
from database.create_connection import Database_OOP
from FrontEndInterface.menu_interface import Menu_interface
from FrontEndInterface.welcome_interface import Welcome_interface

class Show_existing_booking():

    def existing_booking_query(self):
        obj1 = Database_OOP()
        cursor = obj1.establish_connection()
        booking_id = input("Please input your bookingID: ")
        print("One moment please... Loading your booking details!")
        time.sleep(3)
        query = "SELECT * FROM Bookings WHERE BookingID = {} ".format(booking_id)
        cursor.execute(query)
        cursor.commit()
