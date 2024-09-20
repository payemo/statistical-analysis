import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні для кількості годин, які кожен верстат працює на виготовленні деталей 1 та 2
x1 = pulp.LpVariable('x1', lowBound=0, upBound=3, cat='Continuous') # Фрезерний верстат для деталі 1
y1 = pulp.LpVariable('y1', lowBound=0, upBound=3, cat='Continuous') # Фрезерний верстат для деталі 2

x2 = pulp.LpVariable('x2', lowBound=0, upBound=3, cat='Continuous') # Револьверний верстат для деталі 1
y2 = pulp.LpVariable('y2', lowBound=0, upBound=3, cat='Continuous') # Револьверний верстат для деталі 2

x3 = pulp.LpVariable('x3', lowBound=0, upBound=1, cat='Continuous') # Автоматичний револьверний верстат для деталі 1
y3 = pulp.LpVariable('y3', lowBound=0, upBound=1, cat='Continuous') # Автоматичний револьверний верстат для деталі 2

model += 10 * x1 + 20 * y1 + 20 * x2 + 30 * y2 + 30 * x3 + 80 * y3, "Total_Production"

# Загальний час для фрезерного верстата
model += x1 + y1 <= 3, "Time_Frezerniy"
model += x2 + y2 <= 3, "Time_Revolverniy"
model += x3 + y3 <= 1, "Time_AvtoRevolverniy"

model.solve()

print(f"Фрезерний верстат: {x1.varValue} годин для деталі 1, {y1.varValue} годин для деталі 2")
print(f"Револьверний верстат: {x2.varValue} годин для деталі 1, {y2.varValue} годин для деталі 2")
print(f"Автоматичний револьверний верстат: {x3.varValue} годин для деталі 1, {y3.varValue} годин для деталі 2")
print(f"Загальна кількість деталей: {pulp.value(model.objective)}")

