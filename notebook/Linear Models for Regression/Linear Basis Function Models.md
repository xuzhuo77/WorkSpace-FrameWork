
## linear model for regression
- 
$$
y(\mathbf{x}, \mathbf{w})
=w_{0}+w_{1} x_{1}+\ldots+w_{D} x_{D}
$$
- 
$$
y(\mathbf{x}, \mathbf{w})
=w_{0}+\sum_{j=1}^{M-1} w_{j} \phi_{j}(\mathbf{x})
$$
- 
$$
y(\mathbf{x}, \mathbf{w})
=\sum_{j=0}^{M-1} w_{j} \phi_{j}(\mathbf{x})
=\mathbf{w}^{\mathrm{T}} \phi(\mathbf{x})
$$
## basis functions
$$
\phi_{j}(x)
=\exp \left\{-\frac{\left(x-\mu_{j}\right)^{2}}{2 s^{2}}\right\}
$$
$$
\phi_{j}(x)
=\sigma\left(\frac{x-\mu_{j}}{s}\right)
$$
$$
\sigma(a)
=\frac{1}{1+\exp (-a)}
$$