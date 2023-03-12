starting_distance = 16637000000
speed = 38241
time = int(input())*24
miles = starting_distance + time*speed
kilometers = 1.60934*miles
astronomical = 92955781.16*miles
print(miles, ' ', kilometers, ' ', astronomical)

wave_speed = 299792458*2.23694
wave_delay = miles/wave_speed
print(wave_delay)