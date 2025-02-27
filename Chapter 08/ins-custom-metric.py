1.	# A route to return random number between 1 and 6
2.	    
3.	@app.route("/rolldice")
4.	def roll_dice():
5.	    return str(roll())
6.	# Below function returns a random number
7.	def roll():
8.	    with tracer.start_as_current_span("roll") as rollspan:
9.	        res = randint(1, 6)
10.	        rollspan.set_attribute("roll.value", res)
11.	        # This adds 1 to the counter for the given roll value
12.	        roll_counter.add(1, {"roll.value": res})
13.	        return res
14.	
15.	#Create a counter for the dice rolls. E.g how many times a 1 was rolled
16.	roll_counter = meter.create_counter(
17.	    name="dice.rolls",
18.	    description="The number of rolls by roll value",
19.	    )
20.	
21.	    
22.	\
23.	

