import calendar
import datetime
import numpy as np 
import pandas as pd 
import random


# Dictionary of products:
# First element in value is price.
# Second element in value is weight of product being purchased.
# Third element in value is weight of M/F buying the product 
#  (0.5 ==> neutral, >0.5 leans F, <0.5 leans M).
# Fourth element in value is array of weights for being within age bracket:
#   4.1 ==> 18-25
#   4.2 ==> 25-40
#   4.3 ==> 40-60
#   4.4 ==> 60+
#                                          1     2    3    _____4____
products = {#                                              1  2  3  4
  'AA Batteries (12 Pack)':             [11.95, 42, 0.52, [4, 7, 8, 7]],
  'Bike Helmet':                        [27.95, 19, 0.60, [2, 4, 6, 8]],
  'Bungee Cords (10 Pack)':             [11.45, 35, 0.48, [3, 5, 8, 8]],
  'Cherry & Oliver Pitter':             [15.49,  6, 0.68, [3, 6, 7, 9]],
  'Craft Scissors (8 Pack)':            [36,    11, 0.50, [5, 7, 4, 4]],
  'Earthworm Fishing Lure (32 Pack)':   [7.28,   2, 0.10, [4, 4, 5, 6]],
  'Hair Curler':                        [93.31, 15, 0.75, [8, 7, 6, 3]],
  'Knee High Boots':                    [129.2, 13, 0.80, [5, 6, 8, 7]],
  'Mechanical Scale':                   [38.88,  8, 0.55, [1, 3, 6, 7]],
  'Milky Mama Nursing Cover':           [20,     4, 0.90, [6, 8, 1, 1]],
  'Noahs Arc Soundbar':                 [799,    2, 0.40, [5, 8, 6, 3]],
  'Shooter Video Game':                 [59.99, 38, 0.35, [9, 7, 5, 1]],
  'Shower Grab Bar':                    [34.98, 10, 0.40, [1, 1, 2, 10]],
  'Snazzy Hair Clips (3 Pack)':         [5.30,  26, 0.85, [6, 5, 4, 4]],
  'Space Cadet Snow Blower':            [1399,   1, 0.30, [1, 4, 6, 9]],
  'Sun Hat':                            [24.96, 30, 0.60, [4, 5, 6, 7]],
  'Tub of 50 Marbles':                  [17.75,  5, 0.65, [5, 7, 5, 7]],
  'Velcro Shoes':                       [43.16, 17, 0.20, [5, 2, 4, 7]],
  'Vuvuzela':                           [4.99,   8, 0.33, [7, 5, 5, 3]],
  'Wireless Phone Charger':             [42.42, 41, 0.45, [8, 7, 7, 6]],
}

columns = ['id', 'product', 'quantity', 'price', 'date', 'address', 'sex', 'age', 'age_group'] 

### Generate a random date. ###
def random_day(month):
    """Return a random int within the range of the month provided."""
    dayRange = calendar.monthrange(2020, month)[1]
    return random.randint(1, dayRange)

def random_date(month):
    """Return a random date for the month specified.
    Comes in form '11/23/20 10:09'.
    """
    day = random_day(month)
    if random.random() < 0.5:
        date = datetime.datetime(2020, month, day, 12, 00)
    else:
        date = datetime.datetime(2020, month, day, 20, 00)
    offset = np.random.normal(loc=0.0, scale=180)
    time = date + datetime.timedelta(minutes=offset)
    return time.strftime("%m/%d/%y %H:%M")
### End date. ###

def get_sex(sexWeight):
    """Third element of a product value is the weight of a certain sex
    buying a product.
    `random.random()` returns a float in (0, 1), thus if sexWeight=0.4,
    40% of the time it will return 'F', 60% 'M'.
    """
    if random.random() <= sexWeight: 
        return 'F'
    else:
        return 'M'

def get_age_group(ageWeights):
    """Fourth element of product value is an array of 4 weights that
    map the age groups buying a product.  
    """
    index = random.choices(range( len(ageWeights) ), weights=ageWeights)[0]
    ages = [1, 2, 3, 4]
    age = ages[index]
    return age

def get_age(ageGroup):
    """Once we have the age group (1-4), turn it into an age."""
    if ageGroup == 1:
        age = random.randint(18, 25)
    elif ageGroup == 2:
        age = random.randint(26, 40)
    elif ageGroup == 3: 
        age = random.randint(41, 60)
    elif ageGroup == 4:
        age = random.randint(61, 90)
    return age


def random_address():
    """Create random address."""
    streetNames = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', 'Main', 'MLK', 'Redwood', 'Cypress', 'Sunset', 'Washington', 'Lincoln', 'Chestnut', 'South', 'North', 'West', 'Virginia', 'Ridge', 'Dogwood', 'Knoll', 'Bell']
    streetTypes = ['Ave', 'St', 'Dr', 'Way', 'Lane', 'Rd', 'Court', 'Blvd']
    streetTypesWeights = [7, 9, 3, 3, 2, 8, 1, 4]
    cities = ['Sacramento', 'Minneapolis', 'Providence', 'Las Vegas', 'Omaha', 'Baton Rouge', 'Miami', 'New York City', 'Chicago', 'Denver']
    zips = ['94203', '55111', '02902', '88901', '68007', '70808', '33133', '10001', '60007', '80259']
    states = ['CA', 'MN', 'RI', 'NV', 'NE', 'LA', 'FL', 'NY', 'IL', 'CO']
    weights = [7, 5, 1, 7.5, 2, 2, 8, 9, 8, 3]

    street = random.choice(streetNames)
    streetTypeIndex = random.choices(range( len(streetTypes) ), weights=streetTypesWeights)[0]
    index = random.choices(range( len(weights) ), weights=weights)[0]

    return f"{random.randint(1,999)} {street} {streetTypes[streetTypeIndex]}, {cities[index]}, {states[index]} {zips[index]}"


def create_row(orderId, product, orderDate, address):
    """Create a list that can be entered as a row into the dataframe."""
    productPrice = products[product][0]
    quantity = np.random.geometric(p=1.0-(1.0/productPrice), size=1)[0]
    sex = get_sex(products[product][2])
    ageGroup = get_age_group(products[product][3])
    age = get_age(ageGroup)
    output = [orderId, product, quantity, productPrice, orderDate, address, sex, age, ageGroup]
    return output


def add_row(orderId, product, orderDate, address, sex, age, ageGroup):
    """If item added randomly, add new row but keep everything except 
    the product, quantity, and price the same.
    """
    productPrice = products[product][0]
    quantity = np.random.geometric(p=1.0-(1.0/productPrice), size=1)[0]
    output = [orderId, product, quantity, productPrice, orderDate, address, sex, age, ageGroup]
    return output

if __name__ == '__main__':
    # Time how long it takes to generate data files.
    startTime = datetime.datetime.now()
    print(f'Starting script at: {startTime}\n')
    
    orderId = 123456 # id of the first order.
    for month in range(1, 13):
        if month <= 10: # January through October
            numberOrders = int(np.random.normal(loc=12000, scale=4000))
        elif month == 11: # November
            numberOrders = int(np.random.normal(loc=20000, scale=3000))
        else: # December
            numberOrders = int(np.random.normal(loc=26000, scale=3000))

        productList = [product for product in products]
        weights = [products[product][1] for product in products]

        df = pd.DataFrame(columns=columns)

        monthName = calendar.month_name[month]
        print(f'{numberOrders} orders for {monthName}.')

        i = 0
        while numberOrders > 0:
            # Create one row in the dataframe.
            address = random_address()
            orderDate = random_date(month)
            productChoice = random.choices(productList, weights)[0]
            df.loc[i] = create_row(orderId, productChoice, orderDate, address)
            i += 1

            # Add *related* items occasionally.
            loc6 = df.loc[i-1][6]
            loc7 = df.loc[i-1][7]
            loc8 = df.loc[i-1][8]
            if productChoice == "Hair Curler":
                if random.random() < 0.22:
                    df.loc[i] = add_row(orderId, "Snazzy Hair Clips (3 Pack)", orderDate, address, loc6, loc7, loc8)
                    i += 1
                if random.random() < 0.05:
                    df.loc[i] = add_row(orderId, "AA Batteries (12 Pack)", orderDate, address, loc6, loc7, loc8)
                    i += 1
                if random.random() < 0.07:
                    df.loc[i] = add_row(orderId, "Milky Mama Nursing Cover", orderDate, address, loc6, loc7, loc8)
                    i += 1 
            elif productChoice == "Craft Scissors (8 Pack)" or productChoice == "Bungee Cords (10 Pack)":
                if random.random() < 0.09:
                    df.loc[i] = add_row(orderId, "Tub of 50 Marbles", orderDate, address, loc6, loc7, loc8)
                    i += 1
                if random.random() < 0.04:
                    df.loc[i] = add_row(orderId, "Earthworm Fishing Lure (32 Pack)", orderDate, address, loc6, loc7, loc8)
                    i += 1
            elif productChoice == "Velcro Shoes":
                if random.random() < 0.18:
                    df.loc[i] = add_row(orderId, "Shower Grab Bar", orderDate, address, loc6, loc7, loc8)
                    i += 1
                if random.random() < 0.04:
                    df.loc[i] = add_row(orderId, "Sun Hat", orderDate, address, loc6, loc7, loc8)
                    i += 1
                if random.random() < 0.07:
                    df.loc[i] = add_row(orderId, "Tub of 50 Marbles", orderDate, address, loc6, loc7, loc8)
                    i += 1 

            # Add random product to basket.
            if random.random() <= 0.02:
                productChoice = random.choices(productList, weights)[0]
                df.loc[i] = add_row(orderId, productChoice, orderDate, address, loc6, loc7, loc8)
                i += 1

            # Create junk row with names of columns for row values.
            if random.random() <= 0.002:
                df.loc[i] = columns
                i += 1

            # Create NaN rows occasionally.
            if random.random() <= 0.003:
                df.loc[i] = ["","","","","","","","",""]
                i += 1

            orderId += 1 # Increment the id of the order.
            numberOrders -= 1 # Decrement number of orders (want to loop to zero).

        df.to_csv(f"./data/{monthName}_2020.csv", index=False)
        print(f"{monthName}_2020.csv file complete.\n")

runTime = datetime.datetime.now() - startTime
print(f'Ending script. Execution time: {runTime}')