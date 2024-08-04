import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло
n = 1000000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)

# Підрахунок кількості точок під кривою
under_curve = y_random < f(x_random)
monte_carlo_integral = (b - a) * f(b) * np.sum(under_curve) / n

print("Monte-Carlo Integral:", monte_carlo_integral)

# Порівняння із аналітичним методом
result, error = spi.quad(f, a, b)
print("Analitical Integral:", result)
print("Absolute error:", abs(monte_carlo_integral - result))

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Plot of the Integral of Function f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()
