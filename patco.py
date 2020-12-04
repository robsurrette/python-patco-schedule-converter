# coding: utf-8
# 06/27/2018   //   Version 1.0
# 10/10/2018   //   Version 1.1 - updated arrow lengths
# 05/08/2019   //   Version 1.2 - added "CLOSED" replacements
# 09/12/2020   //   Version 1.3 - added "# coding: utf-8" to handle Non-ASCII Characters: "---4"


fileNames = ["WestWeekday.txt", "WestSaturday.txt", "WestSunday.txt"]

for i in range(3):

	lindenwoldHour = []
	ashlandHour = []
	woodcrestHour = []
	haddonfieldHour = []
	westmontHour = []
	collingswoodHour = []
	ferryAveHour = []
	broadwayHour = []
	cityHallHour = []
	x8marketHour = []
	x910locustHour = []
	x1213locustHour = []
	x1516locustHour = []


	lindenwoldMin = []
	ashlandMin = []
	woodcrestMin = []
	haddonfieldMin = []
	westmontMin = []
	collingswoodMin = []
	ferryAveMin = []
	broadwayMin = []
	cityHallMin = []
	x8marketMin = []
	x910locustMin = []
	x1213locustMin = []
	x1516locustMin = []





	with open(fileNames[i], "r") as ins:
		times = []
		for line in ins:
			times.append(line.rstrip('\n'))




	for y in range(len(times)):

		times[y] = times[y].replace(" A","A")
		times[y] = times[y].replace(" P","P")

		times[y] = times[y].replace("A","")
		times[y] = times[y].replace("P","")
		times[y] = times[y].replace("X","")
		times[y] = times[y].replace("W","")


		#times[y] = times[y].replace(" —————————————4","99:99 99:99 99:99")
		#times[y] = times[y].replace(" ————————4","99:99 99:99")						 
		times[y] = times[y].replace("————4","99:99")



		for x in range(13):

			colon = times[y].find(":")

			if x == 0:
				lindenwoldHour.append(int(times[y][:colon]))
			if x == 1:
				ashlandHour.append(int(times[y][:colon]))
			if x == 2:
				woodcrestHour.append(int(times[y][:colon]))
			if x == 3:
				haddonfieldHour.append(int(times[y][:colon]))
			if x == 4:
				westmontHour.append(int(times[y][:colon]))
			if x == 5:
				collingswoodHour.append(int(times[y][:colon]))
			if x == 6:
				ferryAveHour.append(int(times[y][:colon]))
			if x == 7:
				broadwayHour.append(int(times[y][:colon]))
			if x == 8:
				cityHallHour.append(int(times[y][:colon]))
			if x == 9:
				x8marketHour.append(int(times[y][:colon]))
			if x == 10:
				x910locustHour.append(int(times[y][:colon]))
			if x == 11:
				x1213locustHour.append(int(times[y][:colon]))
			if x == 12:
				x1516locustHour.append(int(times[y][:colon]))

				
			times[y] = times[y][colon+1:]


			if x == 0:
				lindenwoldMin.append(int(times[y][:2]))
			if x == 1:
				ashlandMin.append(int(times[y][:2]))
			if x == 2:
				woodcrestMin.append(int(times[y][:2]))
			if x == 3:
				haddonfieldMin.append(int(times[y][:2]))
			if x == 4:
				westmontMin.append(int(times[y][:2]))
			if x == 5:
				collingswoodMin.append(int(times[y][:2]))
			if x == 6:
				ferryAveMin.append(int(times[y][:2]))
			if x == 7:
				broadwayMin.append(int(times[y][:2]))
			if x == 8:
				cityHallMin.append(int(times[y][:2]))
			if x == 9:
				x8marketMin.append(int(times[y][:2]))
			if x == 10:
				x910locustMin.append(int(times[y][:2]))
			if x == 11:
				x1213locustMin.append(int(times[y][:2]))
			if x == 12:
				x1516locustMin.append(int(times[y][:2]))


			times[y] = times[y][3:]
			




	militaryTimeChange = 0

	# Lindenwold
	for z in range(8, len(lindenwoldHour)):
		if lindenwoldHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(lindenwoldHour)):
		lindenwoldHour[z] = lindenwoldHour[z]+12

	for z in range(0, 5):
		if lindenwoldHour[z] == 12:
			lindenwoldHour[z] = 0


	# Ashland
	for z in range(8, len(ashlandHour)):
		if ashlandHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(ashlandHour)):
		ashlandHour[z] = ashlandHour[z]+12

	for z in range(0, 5):
		if ashlandHour[z] == 12:
			ashlandHour[z] = 0


	# Woodcrest
	for z in range(8, len(woodcrestHour)):
		if woodcrestHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(woodcrestHour)):
		woodcrestHour[z] = woodcrestHour[z]+12

	for z in range(0, 5):
		if woodcrestHour[z] == 12:
			woodcrestHour[z] = 0


	# Haddonfield
	for z in range(8, len(haddonfieldHour)):
		if haddonfieldHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(haddonfieldHour)):
		haddonfieldHour[z] = haddonfieldHour[z]+12

	for z in range(0, 5):
		if haddonfieldHour[z] == 12:
			haddonfieldHour[z] = 0


	# Westmont
	for z in range(8, len(westmontHour)):
		if westmontHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(westmontHour)):
		westmontHour[z] = westmontHour[z]+12

	for z in range(0, 5):
		if westmontHour[z] == 12:
			westmontHour[z] = 0


	# Collingswood
	for z in range(8, len(collingswoodHour)):
		if collingswoodHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(collingswoodHour)):
		collingswoodHour[z] = collingswoodHour[z]+12

	for z in range(0, 5):
		if collingswoodHour[z] == 12:
			collingswoodHour[z] = 0


	# Ferry Ave
	for z in range(8, len(ferryAveHour)):
		if ferryAveHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(ferryAveHour)):
		ferryAveHour[z] = ferryAveHour[z]+12

	for z in range(0, 5):
		if ferryAveHour[z] == 12:
			ferryAveHour[z] = 0


	# Broadway
	for z in range(8, len(broadwayHour)):
		if broadwayHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(broadwayHour)):
		broadwayHour[z] = broadwayHour[z]+12

	for z in range(0, 5):
		if broadwayHour[z] == 12:
			broadwayHour[z] = 0


	# City Hall
	for z in range(8, len(cityHallHour)):
		if cityHallHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(cityHallHour)):
		cityHallHour[z] = cityHallHour[z]+12

	for z in range(0, 5):
		if cityHallHour[z] == 12:
			cityHallHour[z] = 0


	# 8th and market
	for z in range(8, len(x8marketHour)):
		if x8marketHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(x8marketHour)):
		x8marketHour[z] = x8marketHour[z]+12

	for z in range(0, 5):
		if x8marketHour[z] == 12:
			x8marketHour[z] = 0


	# 9 10 locust
	for z in range(8, len(x910locustHour)):
		if x910locustHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(x910locustHour)):
		x910locustHour[z] = x910locustHour[z]+12

	for z in range(0, 5):
		if x910locustHour[z] == 12:
			x910locustHour[z] = 0


	# 12 13 locust
	for z in range(8, len(x1213locustHour)):
		if x1213locustHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(x1213locustHour)):
		x1213locustHour[z] = x1213locustHour[z]+12

	for z in range(0, 5):
		if x1213locustHour[z] == 12:
			x1213locustHour[z] = 0


	# 15 16 locust
	for z in range(8, len(x1516locustHour)):
		if x1516locustHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(x1516locustHour)):
		x1516locustHour[z] = x1516locustHour[z]+12

	for z in range(0, 5):
		if x1516locustHour[z] == 12:
			x1516locustHour[z] = 0






	# clear times.txt file
	f = open(fileNames[i], 'w')
	f.write("")
	f.close()



	f = open(fileNames[i], 'a')


	f.write(repr(lindenwoldHour).replace(" ", "")+"\n")
	f.write(repr(lindenwoldMin).replace(" ", "")+"\n")

	f.write(repr(ashlandHour).replace(" ", "")+"\n")
	f.write(repr(ashlandMin).replace(" ", "")+"\n")

	f.write(repr(woodcrestHour).replace(" ", "")+"\n")
	f.write(repr(woodcrestMin).replace(" ", "")+"\n")

	f.write(repr(haddonfieldHour).replace(" ", "")+"\n")
	f.write(repr(haddonfieldMin).replace(" ", "")+"\n")

	f.write(repr(westmontHour).replace(" ", "")+"\n")
	f.write(repr(westmontMin).replace(" ", "")+"\n")

	f.write(repr(collingswoodHour).replace(" ", "")+"\n")
	f.write(repr(collingswoodMin).replace(" ", "")+"\n")

	f.write(repr(ferryAveHour).replace(" ", "")+"\n")
	f.write(repr(ferryAveMin).replace(" ", "")+"\n")

	f.write(repr(broadwayHour).replace(" ", "")+"\n")
	f.write(repr(broadwayMin).replace(" ", "")+"\n")

	f.write(repr(cityHallHour).replace(" ", "")+"\n")
	f.write(repr(cityHallMin).replace(" ", "")+"\n")

	f.write(repr(x8marketHour).replace(" ", "")+"\n")
	f.write(repr(x8marketMin).replace(" ", "")+"\n")

	f.write(repr(x910locustHour).replace(" ", "")+"\n")
	f.write(repr(x910locustMin).replace(" ", "")+"\n")

	f.write(repr(x1213locustHour).replace(" ", "")+"\n")
	f.write(repr(x1213locustMin).replace(" ", "")+"\n")

	f.write(repr(x1516locustHour).replace(" ", "")+"\n")
	f.write(repr(x1516locustMin).replace(" ", ""))

	f.close()




print('West Done')

stationList = ["Lindenwold", "Ashland", "Woodcrest", "Haddonfield", "Westmont", "Collingswood", "Ferry Ave", "Broadway", "City Hall", "8th and Market", "9/10 and Locust", "12/13 and Locust", "15/16 and Locust"]


with open("WestSaturday.txt", "r") as ins:
	saturdayTimes = []
	for line in ins:
		saturdayTimes.append(line.rstrip('\n'))

with open("WestSunday.txt", "r") as ins:
	sundayTimes = []
	for line in ins:
		sundayTimes.append(line.rstrip('\n'))

with open("WestWeekday.txt", "r") as ins:
	weekdayTimes = []
	for line in ins:
		weekdayTimes.append(line.rstrip('\n'))




y = 0
for x in range(0, 13):
	
	print("\t\t\tcase " + str(x) + " :")
	print('\t\t\t\tprint("' + stationList[x] + ' West")')
	
	print("\t\t\t\tif weekday == 7 { //Saturday")
	print("\t\t\t\t\tstationHour = " + saturdayTimes[y])
	print("\t\t\t\t\tstationMinute = " + saturdayTimes[y+1])

	print("\t\t\t\t} else if weekday == 1 { //Sunday")
	print("\t\t\t\t\tstationHour = " + sundayTimes[y])
	print("\t\t\t\t\tstationMinute = " + sundayTimes[y+1])

	print("\t\t\t\t} else { //Weekday")
	print("\t\t\t\t\tstationHour = " + weekdayTimes[y])
	print("\t\t\t\t\tstationMinute = " + weekdayTimes[y+1])

	print("\t\t\t\t}")

	y = y+2










print("")
print("")
print("===================================================================================")
print("")
print("")
print("East:")
print("")









fileNames = ["EastWeekday.txt", "EastSaturday.txt", "EastSunday.txt"]

for i in range(3):

	lindenwoldHour = []
	ashlandHour = []
	woodcrestHour = []
	haddonfieldHour = []
	westmontHour = []
	collingswoodHour = []
	ferryAveHour = []
	broadwayHour = []
	cityHallHour = []
	x8marketHour = []
	x910locustHour = []
	x1213locustHour = []
	x1516locustHour = []


	lindenwoldMin = []
	ashlandMin = []
	woodcrestMin = []
	haddonfieldMin = []
	westmontMin = []
	collingswoodMin = []
	ferryAveMin = []
	broadwayMin = []
	cityHallMin = []
	x8marketMin = []
	x910locustMin = []
	x1213locustMin = []
	x1516locustMin = []





	with open(fileNames[i], "r") as ins:
		times = []
		for line in ins:
			times.append(line.rstrip('\n'))




	for y in range(len(times)):

		times[y] = times[y].replace(" A","A")
		times[y] = times[y].replace(" P","P")

		times[y] = times[y].replace("A","")
		times[y] = times[y].replace("P","")
		times[y] = times[y].replace("X","")

		times[y] = times[y].replace("W","")


		#times[y] = times[y].replace("—————————————4","99:99 99:99 99:99")
		#times[y] = times[y].replace("————————4","99:99 99:99")						 
		times[y] = times[y].replace("————4","99:99")

		

		for x in range(13):

			colon = times[y].find(":")

			if x == 12:
				lindenwoldHour.append(int(times[y][:colon]))
			if x == 11:
				ashlandHour.append(int(times[y][:colon]))
			if x == 10:
				woodcrestHour.append(int(times[y][:colon]))
			if x == 9:
				haddonfieldHour.append(int(times[y][:colon]))
			if x == 8:
				westmontHour.append(int(times[y][:colon]))
			if x == 7:
				collingswoodHour.append(int(times[y][:colon]))
			if x == 6:
				ferryAveHour.append(int(times[y][:colon]))
			if x == 5:
				broadwayHour.append(int(times[y][:colon]))
			if x == 4:
				cityHallHour.append(int(times[y][:colon]))
			if x == 3:
				x8marketHour.append(int(times[y][:colon]))
			if x == 2:
				x910locustHour.append(int(times[y][:colon]))
			if x == 1:
				x1213locustHour.append(int(times[y][:colon]))
			if x == 0:
				x1516locustHour.append(int(times[y][:colon]))

				

			times[y] = times[y][colon+1:]



			if x == 12:
				lindenwoldMin.append(int(times[y][:2]))
			if x == 11:
				ashlandMin.append(int(times[y][:2]))
			if x == 10:
				woodcrestMin.append(int(times[y][:2]))
			if x == 9:
				haddonfieldMin.append(int(times[y][:2]))
			if x == 8:
				westmontMin.append(int(times[y][:2]))
			if x == 7:
				collingswoodMin.append(int(times[y][:2]))
			if x == 6:
				ferryAveMin.append(int(times[y][:2]))
			if x == 5:
				broadwayMin.append(int(times[y][:2]))
			if x == 4:
				cityHallMin.append(int(times[y][:2]))
			if x == 3:
				x8marketMin.append(int(times[y][:2]))
			if x == 2:
				x910locustMin.append(int(times[y][:2]))
			if x == 1:
				x1213locustMin.append(int(times[y][:2]))
			if x == 0:
				x1516locustMin.append(int(times[y][:2]))
				

			times[y] = times[y][3:]




	militaryTimeChange = 0

	# Lindenwold
	for z in range(8, len(lindenwoldHour)):
		if lindenwoldHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(lindenwoldHour)):
		lindenwoldHour[z] = lindenwoldHour[z]+12

	for z in range(0, 5):
		if lindenwoldHour[z] == 12:
			lindenwoldHour[z] = 0


	# Ashland
	for z in range(8, len(ashlandHour)):
		if ashlandHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(ashlandHour)):
		ashlandHour[z] = ashlandHour[z]+12

	for z in range(0, 5):
		if ashlandHour[z] == 12:
			ashlandHour[z] = 0


	# Woodcrest
	for z in range(8, len(woodcrestHour)):
		if woodcrestHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(woodcrestHour)):
		woodcrestHour[z] = woodcrestHour[z]+12

	for z in range(0, 5):
		if woodcrestHour[z] == 12:
			woodcrestHour[z] = 0


	# Haddonfield
	for z in range(8, len(haddonfieldHour)):
		if haddonfieldHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(haddonfieldHour)):
		haddonfieldHour[z] = haddonfieldHour[z]+12

	for z in range(0, 5):
		if haddonfieldHour[z] == 12:
			haddonfieldHour[z] = 0


	# Westmont
	for z in range(8, len(westmontHour)):
		if westmontHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(westmontHour)):
		westmontHour[z] = westmontHour[z]+12

	for z in range(0, 5):
		if westmontHour[z] == 12:
			westmontHour[z] = 0


	# Collingswood
	for z in range(8, len(collingswoodHour)):
		if collingswoodHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(collingswoodHour)):
		collingswoodHour[z] = collingswoodHour[z]+12

	for z in range(0, 5):
		if collingswoodHour[z] == 12:
			collingswoodHour[z] = 0


	# Ferry Ave
	for z in range(8, len(ferryAveHour)):
		if ferryAveHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(ferryAveHour)):
		ferryAveHour[z] = ferryAveHour[z]+12

	for z in range(0, 5):
		if ferryAveHour[z] == 12:
			ferryAveHour[z] = 0


	# Broadway
	for z in range(8, len(broadwayHour)):
		if broadwayHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(broadwayHour)):
		broadwayHour[z] = broadwayHour[z]+12

	for z in range(0, 5):
		if broadwayHour[z] == 12:
			broadwayHour[z] = 0


	# City Hall
	for z in range(8, len(cityHallHour)):
		if cityHallHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(cityHallHour)):
		cityHallHour[z] = cityHallHour[z]+12

	for z in range(0, 5):
		if cityHallHour[z] == 12:
			cityHallHour[z] = 0


	# 8th and market
	for z in range(8, len(x8marketHour)):
		if x8marketHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(x8marketHour)):
		x8marketHour[z] = x8marketHour[z]+12

	for z in range(0, 5):
		if x8marketHour[z] == 12:
			x8marketHour[z] = 0


	# 9 10 locust
	for z in range(8, len(x910locustHour)):
		if x910locustHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(x910locustHour)):
		x910locustHour[z] = x910locustHour[z]+12

	for z in range(0, 5):
		if x910locustHour[z] == 12:
			x910locustHour[z] = 0


	# 12 13 locust
	for z in range(8, len(x1213locustHour)):
		if x1213locustHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(x1213locustHour)):
		x1213locustHour[z] = x1213locustHour[z]+12

	for z in range(0, 5):
		if x1213locustHour[z] == 12:
			x1213locustHour[z] = 0


	# 15 16 locust
	for z in range(8, len(x1516locustHour)):
		if x1516locustHour[z] == 1:
			militaryTimeChange = z
			break

	for z in range(militaryTimeChange, len(x1516locustHour)):
		x1516locustHour[z] = x1516locustHour[z]+12

	for z in range(0, 5):
		if x1516locustHour[z] == 12:
			x1516locustHour[z] = 0






	# clear times.txt file
	f = open(fileNames[i], 'w')
	f.write("")
	f.close()



	f = open(fileNames[i], 'a')


	f.write(repr(lindenwoldHour).replace(" ", "")+"\n")
	f.write(repr(lindenwoldMin).replace(" ", "")+"\n")

	f.write(repr(ashlandHour).replace(" ", "")+"\n")
	f.write(repr(ashlandMin).replace(" ", "")+"\n")

	f.write(repr(woodcrestHour).replace(" ", "")+"\n")
	f.write(repr(woodcrestMin).replace(" ", "")+"\n")

	f.write(repr(haddonfieldHour).replace(" ", "")+"\n")
	f.write(repr(haddonfieldMin).replace(" ", "")+"\n")

	f.write(repr(westmontHour).replace(" ", "")+"\n")
	f.write(repr(westmontMin).replace(" ", "")+"\n")

	f.write(repr(collingswoodHour).replace(" ", "")+"\n")
	f.write(repr(collingswoodMin).replace(" ", "")+"\n")

	f.write(repr(ferryAveHour).replace(" ", "")+"\n")
	f.write(repr(ferryAveMin).replace(" ", "")+"\n")

	f.write(repr(broadwayHour).replace(" ", "")+"\n")
	f.write(repr(broadwayMin).replace(" ", "")+"\n")

	f.write(repr(cityHallHour).replace(" ", "")+"\n")
	f.write(repr(cityHallMin).replace(" ", "")+"\n")

	f.write(repr(x8marketHour).replace(" ", "")+"\n")
	f.write(repr(x8marketMin).replace(" ", "")+"\n")

	f.write(repr(x910locustHour).replace(" ", "")+"\n")
	f.write(repr(x910locustMin).replace(" ", "")+"\n")

	f.write(repr(x1213locustHour).replace(" ", "")+"\n")
	f.write(repr(x1213locustMin).replace(" ", "")+"\n")

	f.write(repr(x1516locustHour).replace(" ", "")+"\n")
	f.write(repr(x1516locustMin).replace(" ", ""))

	f.close()






stationList = ["Lindenwold", "Ashland", "Woodcrest", "Haddonfield", "Westmont", "Collingswood", "Ferry Ave", "Broadway", "City Hall", "8th and Market", "9/10 and Locust", "12/13 and Locust", "15/16 and Locust"]


with open("EastSaturday.txt", "r") as ins:
	saturdayTimes = []
	for line in ins:
		saturdayTimes.append(line.rstrip('\n'))

with open("EastSunday.txt", "r") as ins:
	sundayTimes = []
	for line in ins:
		sundayTimes.append(line.rstrip('\n'))

with open("EastWeekday.txt", "r") as ins:
	weekdayTimes = []
	for line in ins:
		weekdayTimes.append(line.rstrip('\n'))




y = 0
for x in range(0, 13):
	
	print("\t\t\tcase " + str(x) + " :")
	print('\t\t\t\tprint("' + stationList[x] + ' East")')
	
	print("\t\t\t\tif weekday == 7 { //Saturday")
	print("\t\t\t\t\tstationHour = " + saturdayTimes[y])
	print("\t\t\t\t\tstationMinute = " + saturdayTimes[y+1])

	print("\t\t\t\t} else if weekday == 1 { //Sunday")
	print("\t\t\t\t\tstationHour = " + sundayTimes[y])
	print("\t\t\t\t\tstationMinute = " + sundayTimes[y+1])

	print("\t\t\t\t} else { //Weekday")
	print("\t\t\t\t\tstationHour = " + weekdayTimes[y])
	print("\t\t\t\t\tstationMinute = " + weekdayTimes[y+1])

	print("\t\t\t\t}")

	y = y+2
