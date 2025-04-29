import sys

hottest_year = None
coolest_year = None
max_temp = float('-inf')
min_temp = float('inf')

for line in sys.stdin:
    year, temp = line.strip().split("\t")
    temp = float(temp)
    
    if temp > max_temp:
        max_temp = temp
        hottest_year = year

    if temp < min_temp:
        min_temp = temp
        coolest_year = year

print(f"Hottest Year: {hottest_year} with Temperature: {max_temp}°C")
print(f"Coolest Year: {coolest_year} with Temperature: {min_temp}°C")
