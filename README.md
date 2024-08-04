# goit-algo-hw-10

# Monte Carlo Integration and Analytical Calculation

## Description

### Monte Carlo Method Calculation
- **Generating Random Points**: We generate `n` random points within the interval [0, 2] for x and [0, f(2)] for y.
- **Counting Points Under the Curve**: We count the number of points that lie under the curve of the function and calculate the area under the graph using the Monte Carlo method.

### Analytical Calculation Using `quad`
- **Usage of `quad` Function**: We use the `quad` function from the `integrate` submodule of the SciPy library to calculate the exact integral of the function $f(x) = x^2$ over the interval [0, 2]. The function returns the result and an estimate of the absolute error.

### Comparison of Results

|$f(x)$  |Monte Carlo|Analytical Integral|**Absolute Error**|
|--|-----------|-------------------|------------------|
|$\int_{0}^{2} x^2 \ \mathrm{d}x $|2.671416|2.666667|0.004749|

## Conclusions
The Monte Carlo method provides an approximate result, which is close to the analytical value obtained using the `quad` function. The absolute error can be reduced by increasing the number of random points `n`. The use of the `quad` function provides an exact result with high accuracy, allowing for verification of the calculations.
