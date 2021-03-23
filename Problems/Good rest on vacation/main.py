# put your python code here
duration_days = int(input())
total_food_day = int(input())
cost_one_way = int(input())
cost_one_night = int(input())

print(total_food_day
      * duration_days
      + cost_one_way * 2
      + cost_one_night
      * (duration_days - 1))
