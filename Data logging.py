import pandas as pd

name_list = []
phone_list = []
place_list = []
temp_list = []
while True:
    try:
        name = input("Name: ")                      # name
        if name == 'Done' or name == 'done':
            break
        phone = int(input("Phone Number: "))        # phone number
        place = input("Place: ")                    # place
        temp = int(input("Body temperature: "))     # body temperature
    except:
        print('Try again')                          #error msg

    name_list.append(name)                          # append all values to the created list
    phone_list.append(phone)
    place_list.append(place)
    temp_list.append(temp)

# Input taken from receptionist will put in dictionary
data = {
    'Name': name_list,
    'Phone_number': phone_list,
    'Place': phone_list,
    'Temperature': temp_list
}

# Creating dataframe from the data
df = pd.DataFrame(data)

# Convert dataframe to .csv file
df.to_csv('Data.csv')
