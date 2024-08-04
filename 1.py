import pulp

# Створення моделі
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Об'єктивна функція
model += lemonade + fruit_juice, "Total Production"

# Обмеження ресурсів
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
model += 1 * lemonade <= 50, "Sugar Constraint"
model += 1 * lemonade <= 30, "Lemon Juice Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язання моделі
print("Solving the model...")
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade Production: {lemonade.varValue}")
print(f"Fruit Juice Production: {fruit_juice.varValue}")
print(f"Total Production: {lemonade.varValue + fruit_juice.varValue}")
