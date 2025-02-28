#constant
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c=3*10**8
# write your code below: 
#fahrenheit to celsius
def f_to_c(f_temp):
  if not isinstance(f_temp, (int,float)):
    raise ValueError('Temperature must be a number')
  c_temp = (f_temp - 32)*(5/9)  
  return c_temp
#celsius to fahrenheit
def c_to_f(c_temp): 
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)
#get_force
def get_force(mass, acceleration):
  return mass*acceleration 
#train_force
train_force = get_force(train_mass,train_acceleration)
#get_energy
def get_energy(mass,c):  
  return mass*c**2
bomb_energy = get_energy(train_mass,c)
#get_work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force*distance
#train_work
train_work = get_work(train_mass, train_acceleration, train_distance)

#o/p
print(f'Fahrenheit to Celsius: {f_to_c(100):.2e}\u00B0C \n')
print(f'Fahrenheit @ 0\u00B0C : {c_to_f(0):.2e}\u00B0F\n')
print(f'The GE train supplies {train_force:.2e} Newtons of force.\n')
print(f'A 1kg bomb supplies {bomb_energy:.2e} Joules.\n')
print(f'The GE train does {train_work:.2e} Joules of work over {train_distance} meters.')
