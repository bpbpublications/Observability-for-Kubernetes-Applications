1.	# Setting up poll and instrumenting to collect the state info
2.	@app.route('/poll')
3.	def index():
4.	    with tracer.start_as_current_span("state-poll") as span:
5.	        span.set_attribute("language", "python-manual-instrumentation")
6.	        span.set_attribute("signal", "trace")
7.	        span.set_attribute("page", "poll")
8.	        span.add_event("Taking a poll of the audience.")
9.	        print("Polling for states")
10.	    return render_template('poll.html')

