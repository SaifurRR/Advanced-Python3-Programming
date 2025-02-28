#define variable
weight=float(input('Enter Weight in lb'))# in lb
premium=125
#Ground Shipping
try: 
  if weight<0:
    raise ValueError('Weight cannot be negative')
  if weight<=2:
    print(f'cost of Ground shipping: ${weight*1.50+20}')
  elif 2<weight<=6 :
    print(f'cost of Ground shipping: ${weight*3.00+20}')
  elif 6<weight<=10 :
    print(f'cost of Ground shipping: ${weight*4.00+20}')  
  else:
    print(f'cost of Ground shipping: ${weight*4.75+20}')
except ValueError as e:
  print(e)    
#premium  
print(f'cost of Premium shipping: ${premium}')    
#Drone Shipping
try:
  if weight<0:
    raise ValueError('Weight cannot be negative')
  if weight<=2:
    print(f'cost of Drone shipping: ${weight*4.50}')
  elif 2<weight<=6 :
    print(f'cost of Drone shipping: ${weight*9.00}')
  elif 6<weight<=10 :
    print(f'cost of Drone shipping: ${weight*12.00}')  
  else:
    print(f'cost of Drone shipping: ${weight*14.25}')
except ValueError as e:
  print(e)

# Sals_Shipping={'Ground':{range(0,3):('cost of Ground shipping:$', {weight*1.50+20}),range(2,7):('cost of Ground shipping:$', {weight*3.00+20}), range(6,11):('cost of Ground shipping:$', {weight*4.00+20}), (10, float('inf')):('cost of Ground shipping:$', {weight*4.75 + 20}) }, 'premium': 125,
# 'Drone':{range(0,3):('cost of Drone shipping:$', {weight*4.50}),range(2,7):('cost of Drone shipping:$', {weight*9.00}), range(6,11):('cost of Drone shipping:$', {weight*12.00+20}), (10, float('inf')):('cost of Drone shipping:$', {weight*14.25})}}

# Sals_Shipping['Ground'][weight]   
