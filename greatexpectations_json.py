import json
import great_expectations as ge
from great_expectations.profile.json_schema_profiler import JsonSchemaProfiler

jsonschema_file = "raw_data/2021-04-23_recipes_random.json"
suite_name = "JSON_CHECK"

context = ge.data_context.DataContext()

with open(jsonschema_file, "r") as f:
    raw_json = f.read()
    schema = json.loads(raw_json)

print("Generating suite...")
profiler = JsonSchemaProfiler()
suite = profiler.profile(schema, suite_name)
context.save_expectation_suite(suite)
