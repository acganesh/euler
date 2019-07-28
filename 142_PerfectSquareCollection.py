import itertools

mod_vals = [0,1,4]

for mods in itertools.product(mod_vals,repeat=3):
	x = mods[0]
	y = mods[1]
	z = mods[2]

	if (x+y)%8 in mod_vals and (x-y)%8 in mod_vals and (x+z)%8 in mod_vals and (x-z)%8 in mod_vals and (y+z)%8 in mod_vals and (y-z)%8 in mod_vals:
		print "VALS:",x,y,z
