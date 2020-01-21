from openpyxl import Workbook
import xlsxwriter

outWorkbook = xlsxwriter.Workbook("JandJWarehouses.xlsx")
outSheet_A = outWorkbook.add_worksheet()
outSheet_B = outWorkbook.add_worksheet()
outSheet_C = outWorkbook.add_worksheet()
outSheet_D = outWorkbook.add_worksheet()

months_18 = ["Jan-18", "Feb-18", "Mar-18", "Apr-18", "May-18", "Jun-18", "Jul-18", "Aug-18", "Sep-18", "Oct-18", "Nov-18", "Dec-18"]
months_19 = ["Jan-19", "Feb-19", "Mar-19", "Apr-19", "May-19", "Jun-19", "Jul-19", "Aug-19", "Sep-19", "Oct-19", "Nov-19", "Dec-19"]
months_20 = ["Jan-20", "Feb-20", "Mar-20", "Apr-20", "May-20", "Jun-20", "Jul-20", "Aug-20", "Sep-20", "Oct-20", "Nov-20", "Dec-20"]

whole_months_list = []
whole_months_list.extend(months_18)
whole_months_list.extend(months_19)
whole_months_list.extend(months_20)

#trying to figure out payment system using list of months and boolean list has_paid
class Payment:
    def __init__(self, has_paid_2020, has_paid_2019, has_paid_2018):
        self.has_paid_2020 = has_paid_2020
        self.has_paid_2019 = has_paid_2019
        self.has_paid_2018 = has_paid_2018

#defined customer object
class Customer:
    def __init__(self, name, address, city_state_and_zipcode, phone_number, unit_number, payment):
        self.name = name
        self.address = address
        self.city_state_and_zipcode = city_state_and_zipcode
        self.phone_number = phone_number
        self.unit_number = unit_number
        self.payment = payment

#function to print customer information
def display_customer_information(customer):
    print("Name: " + customer.name)
    print("Address: " + customer.address)
    print("City, State, and Zip Code: " + customer.city_state_and_zipcode)
    print("Phone Number: " + customer.phone_number)
    print "Unit Number:",
    for x in range(len(customer.unit_number)):
        print customer.unit_number[x],
    print("\nPayment: $" + str(customer.payment) + "\n")

#function to find customer by unit number
def find_customer_by_unit_number(search, list):
    for customer in list:
        for unit in customer.unit_number:
            if unit == search:
                return customer

def print_months_to_excel(months, starting_col):
    for month in range(len(whole_months_list)):
        outSheet_A.write(0, starting_col+month, whole_months_list[month])
        outSheet_B.write(0, starting_col+month, whole_months_list[month])
        outSheet_C.write(0, starting_col+month, whole_months_list[month])
        outSheet_D.write(0, starting_col+month, whole_months_list[month])

def print_customer_information_to_excel_sheet(outSheet, customer, payment_history, starting_row, starting_col):
    list_of_units = ""
    for x in customer.unit_number:
        list_of_units += x + " "
    outSheet.write(starting_row-1, starting_col, list_of_units)
    outSheet.write(starting_row, starting_col, "Name: ")
    outSheet.write(starting_row+1, starting_col, "Phone Number: ")
    outSheet.write(starting_row+2, starting_col, "Payment Amount: ")
    outSheet.write(starting_row, starting_col+4, "Address: ")
    outSheet.write(starting_row, starting_col+2, customer.name)
    outSheet.write(starting_row+1, starting_col+2, customer.phone_number)
    outSheet.write(starting_row+2, starting_col+2, customer.payment)
    outSheet.write(starting_row, starting_col+5, customer.address + " " + customer.city_state_and_zipcode)

    whole_payment_list = []
    whole_payment_list.extend(payment_history.has_paid_2018)
    whole_payment_list.extend(payment_history.has_paid_2019)
    whole_payment_list.extend(payment_history.has_paid_2020)

    for item in range(len(whole_payment_list)):
        if whole_payment_list[item] == 1:
            outSheet.write(starting_row, starting_col+9+item, "paid")
        elif whole_payment_list[item] == -1:
            outSheet.write(starting_row, starting_col+9+item, "late")
        elif whole_payment_list[item] == 0:
            outSheet.write(starting_row, starting_col+9+item, "not due")

list_of_whole_lot = []
late_fee = 20

#for payment history, key is 1=paid 0=not paid yet -1=late
full_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
empty_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
full_payment = Payment(full_list, full_list, full_list)

paid_interim_2020 = Payment(empty_list, full_list, full_list)

empty = Customer("VACANT", "VACANT", "VACANT", "VACANT", ["VACANT"], 0)
empty_payment = Payment(empty_list, empty_list, empty_list)

#Customer information for lot A of J and J mini-warehouses
A1_payment_history = paid_interim_2020
A1 = Customer("Phyllis Moseley", "237 Hillcrest Ridge", "Canton, GA 30115", "678-880-7248", ["A1"], 35)

A2_payment_history = paid_interim_2020
A2 = Customer("Dorothy Robertson", "2642 Fortner Road", "Ball Ground, GA 30107", "770-893-2507", ["A2"], 40)

A3_payment_history = paid_interim_2020
A3 = Customer("Mountain Home Rentals", "130 Foothills Parkway", "Marble Hill, GA 30148", "770-894-4444", ["A3"], 120)

A4_has_paid_2019 = [-1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 0]
A4_has_paid_2018 = [1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1]
A4_payment_history = Payment(empty_list, A4_has_paid_2019, A4_has_paid_2018)
A4 = Customer("Nancy Martin", "5491 Emerald Court", "Acworth, GA 30102", "706-299-7612", ["A4"], 40)
A4.unit_number.extend(("B4", "B6", "C17", "D3", "D6"))

A5_payment_history = empty_payment
A5 = empty

A6_payment_history = paid_interim_2020
A6 = Customer("Pat Vose", "PO BOX 471245 or 1071 Hubbard RD", "Lake Monroe, FL 32747 or Dawsonville GA 30534", "706-255-6173 or 404-245-9535", ["A6"], 40)

A7_payment_history = empty_payment
A7 = empty

A8_payment_history = paid_interim_2020
A8 = Customer("Mary Raley", "269 Poole Rd", "Marble Hill, GA 30148", "770-710-4961", ["A8"], 40)

A8_payment_history = paid_interim_2020
A9 = A8
A8.unit_number.append("A9")

A10_payment_history = paid_interim_2020
A10 = Customer("Janice Young", "10408 Big Canoe", "Jasper, GA 30143", "Mark 770-560-4553 or Janice 770-894-3381", ["A10"], 30)

A11_payment_history = paid_interim_2020
A11 = A10
A11.unit_number.append("A11")

A12_has_paid_2019 = full_list
A12_has_paid_2019[10] = -1
A12_payment_history = Payment(empty_list, A12_has_paid_2019, full_list)
A12 = A3
A3.unit_number.append("A12")

A13_payment_history = paid_interim_2020
A13 = A6

A14_payment_history = paid_interim_2020
A14 = A6
A6.unit_number.extend(("A13", "A14"))

empty.unit_number.extend(("A5", "A7"))

#list for interating over customers in lot A
list_of_lot_A = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14]
payment_history_lot_A = [A1_payment_history, A2_payment_history, A3_payment_history, A4_payment_history, A5_payment_history, A6_payment_history, A7_payment_history, A8_payment_history, A8_payment_history, A10_payment_history, A11_payment_history, A12_payment_history, A13_payment_history, A14_payment_history]

#Customer information for lot B of J and J mini-warehouses
B1_payment_history = full_payment
B1 = Customer("Jason Mansfield", "161 Burnt Mtn Cove Rd", "Jasper, GA 30143", "770-402-3840", ["B1"], 40)

B2_payment_history = paid_interim_2020
B2 = Customer("Steven and Connie Cooper", "51 Pendley Woods Rd", "Marble Hill, GA 30148", "", ["B2"], 40)

B3_payment_history = paid_interim_2020
B3 = Customer("R.P Duncan", "PO BOX 10609 Big Canoe", "JASPER GA 30143", "706-268-3939", ["B3"], 40)

#B4_has_paid_2019 = [-1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 0]
#B4_has_paid_2018 = [1, 1, 1, 1, -1, -1, -1, 1, 1, -1, 1, -1]
B4_payment_history = A4_payment_history
#Payment(B4_has_paid_2019, B4_has_paid_2018)
B4 = A4

B5_payment_history = paid_interim_2020
B5 = Customer("Jamie West", "", "", "", ["B5"], 40)

#B6_has_paid_2019 = [1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1]
#B6_has_paid_2018 = [1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, -1]
B6_payment_history = A4_payment_history
B6 = A4

B7_payment_history = empty_payment
B7 = empty

B8_payment_history = empty_payment
B8 = empty

B9_payment_history = paid_interim_2020
B9 = Customer("John Fraker", "10967 Big Canoe", "Jasper, GA 30143", "706-579-1350", ["B9"], 35)

B10_has_paid_2019 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 0]
B10_payment_history = Payment(empty_list, B10_has_paid_2019, full_list)
B10 = Customer("David Hopkins", "", "", "706-268-4732", ["B10"], 35)

B11_has_paid_2018 = [1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
B11_payment_history = Payment(empty_list, full_list, B11_has_paid_2018)
B11 = Customer("Sheila Jarrett", "170 Old Dobson Rd", "Ball Ground, GA 30107", "678-294-7775", ["B11"], 40)

B12_has_paid_2018 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]
B12_has_paid_2019 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
B12_payment_history = Payment(empty_list, B12_has_paid_2019, B12_has_paid_2018)
B12 = Customer("Pete's Produce", "PO Box 802", "Jasper, GA 30143", "770-894-5153 or 404-313-6332", ["B12"], 40)

B13_payment_history = paid_interim_2020
B13 = Customer("Regis Falinski", "BOX 11388 BIG CANOE", "Jasper, GA 30143", "", ["B13"], 40)

B14_payment_history = paid_interim_2020
B14 = Customer("C Ray Smith", "11509 Big Canoe", "Jasper, GA 30143", "706-579-2075", ["B14"], 35)

B15_payment_history = paid_interim_2020
B15 = B14
B14.unit_number.append("B15")

B16_payment_history = empty_payment
B16 = empty

payment_history_lot_B = [B1_payment_history, B2_payment_history, B3_payment_history, B4_payment_history, B5_payment_history, B6_payment_history, B7_payment_history, B8_payment_history, B9_payment_history, B10_payment_history, B11_payment_history, B12_payment_history, B13_payment_history, B14_payment_history, B15_payment_history, B16_payment_history]

empty.unit_number.extend(("B7", "B8", "B16"))

#list for interating over customers in lot B
list_of_lot_B = [B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16]

#Customer information for lot C of J and J mini-warehouses
C1_has_paid_2018 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
C1_payment_history = Payment (empty_list, C1_has_paid_2018, C1_has_paid_2018)
C1 = Customer("Chris Kendrick", "189 Dove St.", "Ball Ground, GA 30107", "770-893-1944", ["C1"], 35)

C2_payment_history = paid_interim_2020
C2 = Customer("Naomi Baldwin", "865 Harley Trail", "Ball Ground, GA 30107", "770-893-2161", ["C2"], 35)

C3_payment_history = paid_interim_2020
C3 = Customer("George Cox", "PO Box 130", "Marble Hill, GA 30148", "770-893-1086", ["C3"], 40)

C4_payment_history = paid_interim_2020
C4 = Customer("Sean and Donna Hamby", "4015 Fortner Rd", "Ball Ground, GA 30107", "770-894-4317", ["C4"], 40)

C5_payment_history = paid_interim_2020
C5 = Customer("Pat Hall", "10466 Big Canoe", "Jasper, GA 30143", "706-579-1000", ["C5"], 40)

C6_payment_history = paid_interim_2020
C6 = C5
C5.unit_number.append("C6")

C7_payment_history = empty_payment
C7 = Customer("Peggy Jordan", "", "", "", ["C7"], 0)

C8_payment_history = paid_interim_2020
C8 = C3
C3.unit_number.append("C8")

C9_payment_history = paid_interim_2020
C9 = Customer("VALERIE AND DAVID HOLBROOK", "263 WILKIE RD", "Ball Ground, GA 30107", "", ["C9"], 40)

C10_payment_history = paid_interim_2020
C10 = Customer("GARY PENDLEY", "233 PARTAIN RD", "Marble Hill, GA 30148", "770-881-6362", ["C10"], 120)

C11_payment_history = paid_interim_2020
C11 = Customer("Morgan East Green", "35 Timber Ridge Trail", "Carrollton, GA 30117", "404-313-0307", ["C11"], -1)

C12_payment_history = paid_interim_2020
C12 = Customer("FAYE WEBSTER", "10426 BIG CANOE", "JASPER, GA 30143", "678-467-0336", ["C12"], 480)

C13_payment_history = paid_interim_2020
C13 = Customer("TONYA AND DANIEL KLEIN", "333 EAGLES PERCH", "MARBLE HILL, GA 30148", "404-630-9207", ["C13"], 40)

C14_payment_history = paid_interim_2020
C14 = Customer("BRYANT, ALLISON AND MICHAEL", "912 FOUR MILE CHURCH RD", "BALL GROUND, GA 30107", "678-469-3647", ["C14"], 40)

C15_has_paid_2019 = [1, 1, 1, 1, 1, 1, -1 ,- 1, -1 , -1, -1, -1]
C15_payment_history = Payment(empty_list, C15_has_paid_2019, full_list)
C15 = Customer("JERRY ROBERSON", "2512 FORTNER RD", "BALL GROUND, GA 30107", "470-302-9825", ["C15"], 40)

C16_has_paid_2018 = [-1, -1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1]
C16_has_paid_2019 = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
C16_payment_history = Payment(empty_list, C16_has_paid_2019, C16_has_paid_2018)
C16 = Customer("TIMOTHY SCOTT", "PO BOX 244", "TATE, GA 30177", "", ["C16"], 40)

C17_payment_history = A4_payment_history
C17 = A4

C18_payment_history = paid_interim_2020
C18 = Customer("Garth Barger", "2911 Pharr Court South, NW Apt 1180", "Atlanta, GA 30305", "404-850-9697 or 770-403-4500 cell", ["C18"], 35)

list_of_lot_C = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18]
payment_history_lot_C = [C1_payment_history, C2_payment_history, C3_payment_history, C4_payment_history, C5_payment_history, C6_payment_history, C7_payment_history, C8_payment_history, C9_payment_history, C10_payment_history, C11_payment_history, C12_payment_history, C13_payment_history, C14_payment_history, C15_payment_history, C16_payment_history, C17_payment_history, C18_payment_history]

D1_has_paid_2018 = [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
D1_has_paid_2019 = [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
D1_payment_history = Payment(empty_list, D1_has_paid_2019, D1_has_paid_2018)
D1 = Customer("Carol Goldsberry", "251 Brigidier Ct.", "Ball Ground, GA 30107", "770-595-0364", ["D1"], 45)

D2_payment_history = paid_interim_2020
D2 = Customer("American Telephone Co.", "10231 BIG CANOE", "JASPER, GA 30143", "770-309-8653 or 706-268-3086", ["D2"], 45)

D3_payment_history = A4_payment_history
D3 = A4

D4_payment_history = paid_interim_2020
D4 = Customer("BRETT RAY", "172 HOLLY HILL RD", "JASPER, GA 30143", "", ["D4"], 45)

D5_payment_history = paid_interim_2020
D5 = Customer("BIG CANOE ARTISTS ASSOC", "BOX 11366 BIG CANOE", "JASPER, GA 30143", "678-467-0036", ["D5"], 40)

D6_payment_history = A4_payment_history
D6 = A4

D7_payment_history = paid_interim_2020
D7 = Customer("RICHARD WATERS", "1033 GULF SHORES BLVD", "ALLIGATOR PT, FL 32346", "", ["D7"], 35)

D8_has_paid_2018 = [-1, -1, -1, -1 ,-1, -1, -1, -1, -1, 1, 1 ,1]
D8_has_paid_2019 = [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
D8_payment_history = Payment(empty_list, D8_has_paid_2019, D8_has_paid_2018)
D8 = Customer("Susan Wigington", "684 Pittman Rd", "Dawsonville GA 30534", "706-429-4478", ["D8"], 45)

D9_payment_history = paid_interim_2020
D9 = Customer("KAREN OR EDWARD O'DONNELL", "100 FOOTHILLS PKY", "MARBLE HILL, GA 30148", "770-893-2203 or 678-983-0608", ["D9"], 450)

D10_payment_history = paid_interim_2020
D10 = Customer("Lisa Schnellinger", "11075 Big Canoe", "Jasper, GA 30143", "678-654-6712", ["D10"], 45)

D11_has_paid_2018 = [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1]
D11_has_paid_2019 = [1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ,0]
D11_payment_history = Payment(empty_list, D11_has_paid_2019, D11_has_paid_2018)
D11 = Customer("Corey Goldsberry", "251 Brigadier Ct.", "Ball Ground, GA 30107", "770-595-0364 CAROL", ["D11"], 50)

D12_payment_history = paid_interim_2020
D12 = Customer("Max Bailey", "10957 BIG CANOE", "JASPER, GA 30143", "", ["D12"], 65)

D13_payment_history = paid_interim_2020
D13 = D12
D12.unit_number.append("D13")

D14_payment_history = paid_interim_2020
D14 = Customer("JESUS MANUEL SILVA MUELA", "3220 Farmington Circle", "DAWSONVILLE, GA 30534", "", ["D14"], 50)

D15_payment_history = paid_interim_2020
D15 = Customer("Jeff Dodson", "10507 Big Canoe", "Jasper, GA 30143", "706-248-9818", ["D15"], 35)

D16_payment_history = paid_interim_2020
D16 = A6
A6.unit_number.extend(("D16", "D17"))

D17_payment_history = paid_interim_2020
D17 = A6

D18_payment_history = paid_interim_2020
D18 = Customer("AMANDA PEACOCK", "3306 YELLOW CREEK ROAD", "BALL GROUND, GA 30107", "770-840-5178", ["D18"], -1)

D19_payment_history = paid_interim_2020
D19 = Customer("Diana Woodson", "173 Swanee Drive", "Woodstock, GA 30188", "706-268-3482", ["D19"], 40)

D20_payment_history = Payment(empty_list, [1,1,-1,1,1,1,1,1,1,1,1,1], [1,1,1,0,0,0,0,0,0,0,0,0])
D20 = Customer("Tona Dobson", "61 Dobson Lane", "Marble Hill, GA 30148", "770-893-2306", ["D20"], 40)

D21_payment_history = empty_payment
D21 = empty

D22_payment_history = D20_payment_history
D22 = D20
D20.unit_number.append("D22")

D23_payment_history = paid_interim_2020
D23 = B10
B10.unit_number.append("D23")

D24_payment_history = Payment(empty_list,[-1,-1,-1,-1,1,1,1,1,1,1,1,1], [1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1])
D24 = D20
D20.unit_number.append("D24")

list_of_lot_D = [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, D13, D14, D15, D16, D17, D18, D19, D20, D21, D22, D23, D24]
payment_history_lot_D = [D1_payment_history, D2_payment_history, D3_payment_history, D4_payment_history, D5_payment_history, D6_payment_history, D7_payment_history, D8_payment_history, D9_payment_history, D10_payment_history, D11_payment_history, D12_payment_history, D13_payment_history, D14_payment_history, D15_payment_history, D16_payment_history, D17_payment_history, D18_payment_history, D19_payment_history, D20_payment_history, D21_payment_history, D22_payment_history, D23_payment_history, D24_payment_history]

#extension of other lots into a whole list
list_of_whole_lot.extend(list_of_lot_A)
list_of_whole_lot.extend(list_of_lot_B)
list_of_whole_lot.extend(list_of_lot_C)
list_of_whole_lot.extend(list_of_lot_D)

"""
for list in list_of_whole_lot:
    display_customer_information(list)
    """

print_months_to_excel(months_18, 9)

for customer in range(len(list_of_lot_A)):
    print_customer_information_to_excel_sheet(outSheet_A, list_of_lot_A[customer], payment_history_lot_A[customer], 1+(5*customer), 0)

for customer in range(len(list_of_lot_B)):
    print_customer_information_to_excel_sheet(outSheet_B, list_of_lot_B[customer], payment_history_lot_B[customer], 1+(5*customer), 0)

for customer in range(len(list_of_lot_C)):
    print_customer_information_to_excel_sheet(outSheet_C, list_of_lot_C[customer], payment_history_lot_C[customer], 1+(5*customer), 0)

for customer in range(len(list_of_lot_D)):
    print_customer_information_to_excel_sheet(outSheet_D, list_of_lot_D[customer], payment_history_lot_D[customer], 1+(5*customer), 0)

outWorkbook.close()
