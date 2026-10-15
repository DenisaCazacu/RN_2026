import numpy as np
import matplotlib.pyplot as plt


def generate_points(a, b, n):

	rng = np.random.default_rng()
	x = rng.uniform(-10.0, 10.0, size=n)
	c = 1*rng.uniform(0.0, 2.0, size=n)
	print(np.mean(c))
	print(np.max(c))
	print(np.min(c))
	y = a * x + b + c

	return np.column_stack((x, y))


def generate_random_line():
	rng = np.random.default_rng()
	while True:
		a = rng.uniform(-5.0, 5.0)
		b = rng.uniform(-5.0, 5.0)
		c = rng.uniform(-10.0, 10.0)
		if a != 0 or b != 0:
			return a, b, c


def distance_from_line(line, point):
	a, b, c = line
	x0, y0 = point
	return abs(a * x0 + b * y0 + c) / np.sqrt(a ** 2 + b ** 2)

if __name__ == "__main__":
	points = generate_points(2, 1, 50)

	trials = 100000
	best_line = None
	best_mean_distance = None
	for i in range(trials):
		line = generate_random_line()
		distances = [distance_from_line(line, point) for point in points]
		mean_distance = np.mean(distances)
		if best_mean_distance is None or mean_distance < best_mean_distance:
			best_line = line
			best_mean_distance = mean_distance

	print(f"cea mai buna dreapta: {best_line}")
	print(f"media distantelor: {best_mean_distance}")

	x_values = points[:, 0]
	y_values = points[:, 1]

	plt.scatter(x_values, y_values, color="blue", label="puncte")

	a, b, c = best_line
	x_min = -12
	x_max = 12
	x_line = np.linspace(x_min, x_max, 200)
	if abs(b) > 1e-12:
		y_line = -(a * x_line + c) / b
		plt.plot(x_line, y_line, color="red", label="dreapta cu media minima")
	else:
		x_line_vertical = -c / a
		plt.axvline(x_line_vertical, color="red", label="dreapta cu media minima")

	plt.xlabel("x")
	plt.ylabel("y")
	plt.grid(True)
	plt.legend()
	plt.show()
