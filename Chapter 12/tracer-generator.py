1.	# First we set up a global tracer and meter. Any function from here forward can re-use the tracer and meter to generate either traces or metrics. We can also generate unique tracers within function.
2.	tracer = trace.get_tracer(__name__)
3.	meter = metrics.get_meter(__name__)
4.	
5.	# We can set up a baseline of instrumentation by brining in instrumenation libararies for the pakages we are using. These give a good baseline to start from.
6.	def setup_instrumentation():
7.	    BotocoreInstrumentor().instrument()
8.	    FlaskInstrumentor().instrument_app(app)
9.	    RequestsInstrumentor().instrument()
10.	
11.	# Setting up opentelemetry, we will pass in our global tracer and meter we created earlier.
12.	def setup_opentelemetry(tracer, meter):
13.	    # Set up AWS X-Ray Propagator, we do this because we need to create trace-ids in a format that x-ray can understand.
14.	    propagate.set_global_textmap(AwsXRayPropagator())
15.	    
16.	    # Service name is required for most backends. We can try to grab additional attributes from the environment.
17.	    resource_attributes = { 'service.name': 'python-manual-instrumentation-sample-app' }
18.	    if (os.environ.get("OTEL_RESOURCE_ATTRIBUTES")):
19.	        resource_attributes = None
20.	    resource = Resource.create(attributes=resource_attributes)
21.	
22.	    # Setting up Tracer Provider, we will batch up spans and then send them to an exporter. We also need to add the resources we defined earlier and use our x-ray generator.
23.	    processor = BatchSpanProcessor(OTLPSpanExporter())
24.	    tracer_provider = TracerProvider(
25.	        resource=resource, 
26.	        active_span_processor=processor,
27.	        id_generator=AwsXRayIdGenerator())
28.	    
29.	    # Initalize the tracer provider with the configuration defined above.
30.	    trace.set_tracer_provider(tracer_provider)

