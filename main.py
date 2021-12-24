import mysql.connector
import smtplib, ssl
from messege import booking_message as message

# Your email and password. The password should be 2-step verified in google account
# and 'App password' in google account, if necessary
sender = 'your@gmail.com'
password = 'your_password'


# Client's input: name, email
user_name = input(str('Type your name: '))
receiver = input(str('Type your e-mail: '))

context = ssl.create_default_context()  # Email ssl setting


def email_sender(): # Function for email sending
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()


mydb = mysql.connector.connect(  # Mysql connection
    host="localhost",
    user="root",
    password="6283307sh",
    database="office"
)

# Database queries to identify available room in day of the week
mycursor = mydb.cursor()
mycursor.execute("""SELECT rooms 
                 FROM room_days 
                 WHERE monday=0
                 """)
available_monday = mycursor.fetchall()


mycursor.execute("""SELECT rooms 
                 FROM room_days 
                 WHERE tuesday=0
                 """)
available_tuesday = mycursor.fetchall()

mycursor.execute("""SELECT rooms 
                 FROM room_days 
                 WHERE wednesday=0
                 """)
available_wednesday = mycursor.fetchall()

mycursor.execute("""SELECT rooms 
                 FROM room_days 
                 WHERE thursday=0
                 """)
available_thursday = mycursor.fetchall()

mycursor.execute("""SELECT rooms 
                 FROM room_days 
                 WHERE friday=0
                 """)
available_friday = mycursor.fetchall()

mycursor.execute("""SELECT rooms 
                 FROM room_days 
                 WHERE saturday=0
                 """)
available_saturday = mycursor.fetchall()

mycursor.execute("""SELECT rooms 
                 FROM room_days 
                 WHERE sunday=0
                 """)
available_sunday = mycursor.fetchall()


def update_db(key1, key2):  # Database updater for rooms
    mycursor.execute(f"""UPDATE room_days
                        SET {key1} = 1
                        WHERE room_id = {key2};""")

    mydb.commit()


def update_user_db(key1, key2, key3):  # Database updater for clients
    mycursor.execute(f"""UPDATE customers
                         SET {key1} = '{key3}'
                         WHERE room_id = {key2}
                             """)
    mydb.commit()


def main():  # Main func and logic
    print('')
    print('     -----DAYS-----')
    print('')
    print('        *Monday')
    print('        *Tuesday')
    print('        *Wednesday')
    print('        *Thursday')
    print('        *Friday')
    print('        *Saturday')
    print('        *Sunday')
    user_day = input(str('Choose a day you want: ')).lower()
    print('')
    print('   -----OFFICE ROOMS-----')
    print('')
    print('           *room1')
    print('           *room2')
    print('           *room3')
    print('           *room4')
    print('           *room5')
    user_room = input('Choose your room: ').lower()
    if user_day == 'monday':
        for i in available_monday:
            if user_room in i[0]:
                print('Room is available for this day. Do you want to book?')
                answer = input(str('Type Y/N: ')).lower()
                if answer == 'y':
                    if user_room == 'room1':
                        user_room = '1'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room2':
                        user_room = '2'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        print('E-mail sent')
                    if user_room == 'room3':
                        user_room = '3'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room4':
                        user_room = '4'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room5':
                        user_room = '5'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                        break
    if user_day == 'tuesday':
        for i in available_tuesday:
            if user_room in i[0]:
                print('Room is available for this day. Do you want to book?')
                answer = input(str('Type Y/N: ')).lower()
                if answer == 'y':
                    if user_room == 'room1':
                        user_room = '1'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room2':
                        user_room = '2'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        print('E-mail sent')
                    if user_room == 'room3':
                        user_room = '3'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room4':
                        user_room = '4'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room5':
                        user_room = '5'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                        break
    if user_day == 'wednesday':
        for i in available_wednesday:
            if user_room in i[0]:
                print('Room is available for this day. Do you want to book?')
                answer = input(str('Type Y/N: ')).lower()
                if answer == 'y':
                    if user_room == 'room1':
                        user_room = '1'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room2':
                        user_room = '2'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room3':
                        user_room = '3'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room4':
                        user_room = '4'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room5':
                        user_room = '5'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                        break
    if user_day == 'thursday':
        for i in available_thursday:
            if user_room in i[0]:
                print('Room is available for this day. Do you want to book?')
                answer = input(str('Type Y/N: ')).lower()
                if answer == 'y':
                    if user_room == 'room1':
                        user_room = '1'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room2':
                        user_room = '2'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room3':
                        user_room = '3'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room4':
                        user_room = '4'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room5':
                        user_room = '5'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                        break
    if user_day == 'friday':
        for i in available_friday:
            if user_room in i[0]:
                print('Room is available for this day. Do you want to book?')
                answer = input(str('Type Y/N: ')).lower()
                if answer == 'y':
                    if user_room == 'room1':
                        user_room = '1'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room2':
                        user_room = '2'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room3':
                        user_room = '3'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room4':
                        user_room = '4'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room5':
                        user_room = '5'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                        break
    if user_day == 'saturday':
        for i in available_saturday:
            if user_room in i[0]:
                print('Room is available for this day. Do you want to book?')
                answer = input(str('Type Y/N: ')).lower()
                if answer == 'y':
                    if user_room == 'room1':
                        user_room = '1'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room2':
                        user_room = '2'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room3':
                        user_room = '3'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room4':
                        user_room = '4'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room5':
                        user_room = '5'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                        break
    if user_day == 'sunday':
        for i in available_sunday:
            if user_room in i[0]:
                print('Room is available for this day. Do you want to book?')
                answer = input(str('Type Y/N: ')).lower()
                if answer == 'y':
                    if user_room == 'room1':
                        user_room = '1'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room2':
                        user_room = '2'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room3':
                        user_room = '3'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room4':
                        user_room = '4'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                    if user_room == 'room5':
                        user_room = '5'
                        update_db(user_day, user_room)
                        update_user_db(user_day, user_room, user_name)
                        email_sender()
                        print('E-mail sent')
                        break


main()
