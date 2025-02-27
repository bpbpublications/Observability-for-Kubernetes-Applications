1.	#setup polling and templates for demo.
2.	@app.route('/poll')
3.	def index():
4.	    with tracer.start_as_current_span("state-poll") as span:
5.	        span.set_attribute("language", "python-manual-instrumentation")
6.	        span.set_attribute("signal", "trace")
7.	        span.set_attribute("page", "poll")
8.	        span.add_event("Taking a poll of the audience.")
9.	        print("Polling for states")
10.	    return render_template('poll.html')
11.	
12.	#Generate unique url for demo.
13.	@app.route('/<state>')
14.	def state(state):
15.	    return render_template('state.html', state=state)
16.	
17.	#Run the app.
18.	if __name__ == '__main__':
19.	    # setting up instrumentation & opentelemetry
20.	    setup_instrumentation()
21.	    setup_opentelemetry(tracer, meter)
22.	    rmc = random_metrics.RandomMetricCollector()
23.	    rmc.register_metrics_client(cfg)
24.	    app.run(host=cfg['Host'], port=cfg['Port'])


