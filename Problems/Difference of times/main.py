# put your python code here
hours_one = int(input())
minutes_one = int(input())
seconds_one = int(input())
hours_two = int(input())
minutes_two = int(input())
seconds_two = int(input())
print((hours_two - hours_one) * 3600
      + (minutes_two - minutes_one) * 60
      + (seconds_two - seconds_one))
