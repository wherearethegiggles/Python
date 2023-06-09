# Data for cities, return flight cost ($), hotel cost per day ($), and weekly car rental cost ($)
cities = ["Paris", "London", "Dubai", "Mumbai"]
return_flight_cost = [200, 250, 370, 450]
hotel_cost_per_day = [20, 30, 15, 10]
weekly_car_rental_cost = [200, 120, 80, 70]

# Calculate the total cost for each city for a 1-week trip
def cost_cal(return_flight_cost, hotel_cost_per_day, weekly_car_rental_cost):
  total_costs = []
  for i in range(len(cities)):
    total_cost = return_flight_cost[i] + (hotel_cost_per_day[i] * 7) + weekly_car_rental_cost[i]
    total_costs.append(total_cost)
# Find the index of the city with the minimum total cost
    cheapest_city_index = total_costs.index(min(total_costs))
    cheapest_city = cities[cheapest_city_index]
    return total_cost,cheapest_city

# Print the total cost for each city
for i in range(len(cities)):
    print(f"Total cost for {cities[i]}: ${total_costs[i]}")

# Print the city with the least amount of expense
print(f"The city with the least expense for a 1-week trip is {cheapest_city}.")