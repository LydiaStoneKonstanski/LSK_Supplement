weight = 4.8
cost_ground = 0.00
cost_drone = 0.00

flat_charge_ground = 20.00
ground_shipping_premium = 125.00

print('Premium Ground Shipping costs $', ground_shipping_premium)

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + flat_charge_ground
  print('Ground shipping will cost: $',cost_ground)
elif (weight > 2) and (weight <= 6):
  cost_ground = weight * 3.00 + flat_charge_ground
  print('Ground shipping will cost: $' , cost_ground)
elif (weight > 6) and (weight <= 10):
  cost_ground = weight * 4.00 + flat_charge_ground
  print('Ground shipping will cost: $' , cost_ground)
elif weight > 10:
  cost_ground = weight * 4.75 + flat_charge_ground
  print('Ground shipping will cost: $' , cost_ground)
else:
  print('Weight Entry Error')

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
  print('Drone shipping will cost: $',cost_drone)
elif (weight > 2) and (weight <= 6):
  cost_drone = weight * 9.00
  print('Drone shipping will cost: $',cost_drone)
elif (weight > 6) and (weight <= 10):
  cost_drone = weight * 12.00
  print('Drone shipping will cost: $',cost_drone)
elif weight > 10:
  cost_drone = weight * 14.25
  print('Drone shipping will cost: $',cost_drone)
else:
  print('Weight Entry Error')