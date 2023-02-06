from functions import *

extremum_x = find_extrem_x()
extremum_y = find_extrem_y(extremum_x)
roots = get_roots(extremum_x)

plt.figure(figsize=(10,6))
print_exrem(extremum_x, extremum_y)
print_roots(roots)
prin_function()

plt.xlabel('x', fontsize=16, fontweight='bold')
plt.ylabel('f(x)', fontsize=16, fontweight='bold')
plt.title('f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30', fontsize=16, fontweight='bold')

plt.legend()
plt.grid()
plt.show()