#Menu class -----------------------
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "{name} menu. It serves from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time=self.end_time)
  
  def calculate_bill(self, purchased_items):
    bill=0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill+=self.items[purchased_item]
      else: print("sorry, we don't have what you ordered")
    return bill

#items dictionaries --------------
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

#menus ----------------------
brunch_menu = Menu("brunch", brunch_items, 11, 16)

early_bird_menu = Menu("early bird", early_bird_items, 15, 18)

dinner_menu = Menu("dinner", dinner_items, 17, 23)

kids_menu = Menu("kids", kids_items, 11, 21)

menus = (brunch_menu, early_bird_menu, kids_menu, dinner_menu)

arepas_menu = Menu("Take a'Arepa", arepas_items, 10, 20)

#Menu class testing ----------------
#print(brunch)
#print(brunch.calculate_bill(['pancakes', "home fries", 'coffee']))
#print(early_bird.calculate_bill(['salumeria plate', "mushroom ravioli (vegan)"]))

#Franchise Class---------------------
class Franchise:
  def __init__(self, address, menus):
    self.address=address
    self.menus=menus
    
  def __repr__(self):
    return "This franchise is located at {address}".format(address=self.address)
  
  def available_menus(self, time):
    self.time = time
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time < menu.end_time:
        available_menus.append(menu)
    return available_menus

#franchise info ---------------------
flagship_address = "1232 West End Road"
flagship_store = Franchise(flagship_address, menus)
  
installment_address = "12 East Mulberry Street"
new_installment = Franchise(installment_address, menus)

arepas_address = "189 Fitzgerald Avenue"
arepas_place = Franchise(arepas_address, arepas_menu)

#Franchise Class testing -------------
#print(flagship_store.available_menus(12))

#Business Class----------------------
class Business:
  def __init__ (self, name, franchises):
    self.name = name
    self.franchises = franchises

Basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

Arepa = Business("Take a' Arepa", arepas_place)

#print(Arepa.franchises)
