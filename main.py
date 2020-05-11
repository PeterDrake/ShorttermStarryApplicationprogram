# Liz: Let's try an experiment in collaboration

# Here's a function definition:
def square(x):
  return x * x

# Here's an invocation:
print(square(4))

# Run it by clicking the "run" button at the top

# Now can you try defining and invoking "cube" below this?

# If this works, it could be fantastic for interactive live coding.
def cube(x):
  return x*x*x
print(cube(3))

def power(x, n):
  if n == 1:
    return x
  return x * power(x, n - 1)

print(power(2, 3))
