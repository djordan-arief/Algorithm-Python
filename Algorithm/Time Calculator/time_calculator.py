def add_time(start, duration, starting_day=""):
  DaysOfTheWeek = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday", 
    "Sunday"]
  
  startTime = start.split()
  dayTime = startTime[1] # Get the AM or PM
  numTime = startTime[0].split(":") # [hours: minutes]
  durationTime = duration.split(":")

  # check if the minute is not greater or equal to 60
  if int(durationTime[1]) >= 60:
    print("Error: minutes cannot be 60 or more")
    return 

  #calculate time
  addMinutes = int(numTime[1]) + int(durationTime[1])
  addHours = int(numTime[0]) + int(durationTime[0])
  
  # 24 hours format
  daysPassed = 0
  newHours = addHours
  if newHours > 24:
    while newHours > 24: 
      daysPassed = daysPassed + 1
      newHours = newHours - 24
  addHours = newHours
  
  # adding 1 to hours if minutes >= 60
  if addMinutes >= 60: 
    addMinutes = addMinutes - 60
    if addMinutes == 0:
      addMinutes = str(addMinutes) + "0"
    elif addMinutes < 10:
      addMinutes = "0" + str(addMinutes)

  # modifying the day time
  if addHours > 12: 
    addHours = addHours - 12
    if dayTime == 'AM':
      dayTime = "PM"
    else:
      dayTime = "AM"

  
  #Final results
  if starting_day == "":
    new_time = str(addHours) + ":" + str(addMinutes) + " " + dayTime
  else:
    new_time = str(addHours) + ":" + str(addMinutes) + " " + dayTime
    if daysPassed > 0:
     new_time = new_time + " " + f"({daysPassed} days later)"
 
  return new_time
  

print(add_time("03:11 AM", "48:00", "Wednesday"))