import random
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
print("Before swapping:")
print(f"a = {a}, b = {b}, c = {c}")
swap_type = random.choice(["rotate_left", "rotate_right", "reverse"])
if swap_type == "rotate_left":
    a, b, c = b, c, a
elif swap_type == "rotate_right":
    a, b, c = c, a, b
else:
    a, b, c = c, b, a
print(f"\nSwap type: {swap_type}")
print("After swapping:")
print(f"a = {a}, b = {b}, c = {c}")