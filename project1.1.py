STRT_MILES = 16_637_000_000
SPD_MPH = 38241
T_HOURS = int(input("Enter time in days:"))*24

miles = STRT_MILES + T_HOURS*SPD_MPH
kilometers = round(1.60934*miles)
aus = 92_955_781.16*miles
print("Voyager-1 traveled:")
print(miles, ' miles, ', kilometers, ' kilometers,  ', aus, '  astronomical units.  ')

WVSPD_MPH = 299_792_458*2.23694
wv_delay = miles/WVSPD_MPH
print("Communication delay:")
print(wv_delay, " hours.")