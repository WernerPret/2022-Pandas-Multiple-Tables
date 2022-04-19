import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
  
# 1
# print(visits)
# print(cart)
# print(checkout)
# print(purchase)

# 2
visits_cart = pd.merge(visits, cart, how="left")
# print(visits_cart)

# 3
# print(visits_cart['user_id'].count())
# print(len(visits_cart))

# 4 + 5 
isnull = len(visits_cart[visits_cart['cart_time'].isnull()])
isnotnull = len(visits_cart) - isnull
total = isnull+isnotnull
perc_not = isnull/total*100
# print(perc_not)
# print(isnotnull)

# 6
cart_check = pd.merge(cart, checkout, how="left")
# print(cart_check)
not_check = cart_check[cart_check['checkout_time'].isnull()]
# print(len(not_check))

# 7
all_data = visits.merge(cart, how="left").merge(checkout, how="left").merge(purchase, how="left")
# print(all_data)

# 8
check_not_pur = all_data[(all_data['checkout_time'].notnull()) & (all_data['purchase_time'].isnull())]
# print(len(check_not_pur))

# 9
not_visit = len(all_data[all_data['visit_time'].isnull()])/len(all_data)*100
not_cart = len(all_data[all_data['cart_time'].isnull()])/len(all_data)*100
not_check = len(all_data[all_data['checkout_time'].isnull()])/len(all_data)*100
not_purch = len(all_data[all_data['purchase_time'].isnull()])/len(all_data)*100
# print(all_data)
# print(not_purch)

all_data['Diff'] = all_data['purchase_time'] - all_data['visit_time']

print(all_data['Diff'].mean())





