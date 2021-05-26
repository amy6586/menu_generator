import sys

from great_expectations import DataContext

# checkpoint configuration
context = DataContext("menu_generator/great_expectations")
checkpoint = context.get_checkpoint("pgfinaltable")

# run the Checkpoint
results = checkpoint.run()

# take action based on results
if not results["success"]:
    print("Validation failed!")
    sys.exit(1)

print("Validation succeeded!")
sys.exit(0)
