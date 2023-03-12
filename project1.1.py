starting_distance = 16637000000
speed = 38241
print("Enter time in days:")
time = int(input())*24
miles = starting_distance + time*speed
kilometers = round(1.60934*miles)
au = 92955781.16*miles
print("Voyager-1 traveled:")
print(miles, ' miles, ', kilometers, ' kilometers,  ', au, '  astronomical units.  ')

wave_speed = 299792458*2.23694
wave_delay = miles/wave_speed
print("Communication delay:")
print(wave_delay, " hours.")