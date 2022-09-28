with open("input.txt", "r") as f:
    modules = [int(line) for line in f]


def calculate_fuel(mass_module: int) -> int:
    mass_module = mass_module // 3  # Divide and get floor
    mass_module = mass_module - 2
    return mass_module


def calculate_fuel_all(mass: int) -> int:
    sum_ = 0
    while mass > 0:
        mass = calculate_fuel(mass)
        if mass > 0:
            sum_ += mass
    return sum_


# PART 1
sum_ = 0
for number in modules:
    fuel_weight = calculate_fuel(number)
    sum_ += calculate_fuel(number)
print(sum_)


# PART 2
sum_ = 0
for number in modules:
    fuel_weight = calculate_fuel_all(number)
    sum_ += calculate_fuel_all(number)
print(sum_)
