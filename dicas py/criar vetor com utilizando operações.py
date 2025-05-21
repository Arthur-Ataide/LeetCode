timePoints = ["23:59","00:00"]

timeMin = [60*int(i[0:1])+int(i[3:4]) for i in timePoints]

print(timeMin)
