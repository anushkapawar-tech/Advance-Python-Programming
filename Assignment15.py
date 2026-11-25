import gc

# Check garbage collection status
print("Garbage collection enabled:",
      gc.isenabled())

# Display initial garbage collection count
print("Initial GC count:", gc.get_count())

# Create a class
class Student:
    def __init__(self, name):
        self.name = name
        self.ref = None

# Create circular references
s1 = Student("Rahul")
s2 = Student("Amit")

s1.ref = s2
s2.ref = s1

print("\nCircular references created.")

# Delete references
del s1
del s2

print("Objects are now unreachable.")

# Disable automatic garbage collection
gc.disable()
print("\nAutomatic GC disabled:",
      gc.isenabled())

# Perform manual garbage collection
collected = gc.collect()

print("Objects collected manually:", collected)

# Display garbage collection statistics
print("GC count after collection:", gc.get_count())
print("GC statistics:", gc.get_stats())

# Enable automatic garbage collection
gc.enable()

print("\nAutomatic GC enabled:",
      gc.isenabled())
