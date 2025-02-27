1.	#Import libraries for instrumentation
2.	from opentelemetry import propagate, trace, metrics
3.	
4.	
5.	# Exporter Libraries
6.	from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
7.	
8.	# Metrics Library
9.	from opentelemetry.metrics import CallbackOptions, Observation
10.	
11.	# SDK Libraries
12.	from opentelemetry.sdk.trace import TracerProvider
13.	from opentelemetry.sdk.trace.export import BatchSpanProcessor
14.	from opentelemetry.sdk.extension.aws.trace import AwsXRayIdGenerator
15.	from opentelemetry.sdk.resources import SERVICE_NAME, Resource
16.	from opentelemetry.sdk.metrics import MeterProvider
17.	from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
18.	from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
19.	
20.	# Propogators Library
21.	from opentelemetry.propagators.aws import AwsXRayPropagator
22.	from opentelemetry.propagators.aws.aws_xray_propagator import (
23.	    TRACE_ID_DELIMITER,
24.	    TRACE_ID_FIRST_PART_LENGTH,
25.	    TRACE_ID_VERSION,
26.	)
27.	
28.	# Instrumentation Libraries
29.	# These provide pre-build instrumentation options for popular libaries such as Flask or Boto
30.	from opentelemetry.instrumentation.botocore import BotocoreInstrumentor
31.	from opentelemetry.instrumentation.flask import FlaskInstrumentor
32.	from opentelemetry.instrumentation.requests import RequestsInstrumentor
33.	
34.	# First we set up a global tracer and meter. Any function from here forward can re-use the tracer and meter to generate either traces or metrics. We can also generate unique tracers within function.
35.	tracer = trace.get_tracer(__name__)
36.	meter = metrics.get_meter(__name__)
37.	
38.	
39.	# We can set up a baseline of instrumentation by brining in instrumenation libararies for the pakages we are using. These give a good baseline to start from.
40.	def setup_instrumentation():
41.	    BotocoreInstrumentor().instrument()
42.	    FlaskInstrumentor().instrument_app(app)
43.	    RequestsInstrumentor().instrument()

