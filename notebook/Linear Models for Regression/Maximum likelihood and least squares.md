##  Gaussian noise model
- [[curve fitting#polynomial]]
$$
p(t \mid \mathbf{x}, \mathbf{w}, \beta)
=\mathcal{N}\left(t \mid y(\mathbf{x}, \mathbf{w}), \beta^{-1}\right)
$$
-  target variable t is given by a deterministic function y(x, w) with additive Gaussian noise
$$
t=y(\mathbf{x}, \mathbf{w})+\epsilon
$$
## a Gaussian conditional distribution 
-In the case of a Gaussian conditional distribution of the form [[#Gaussian noise model]], the conditional mean

$$
\mathbb{E}[t \mid \mathbf{x}]
=\int t p(t \mid \mathbf{x}) \mathrm{d} t
=y(\mathbf{x}, \mathbf{w})
$$
##  logarithm of the likelihood function
- which is extend by [[curve fitting#likelihood function]] and [[curve fitting#log likelihood function]]
- governed by the number of [[Linear Basis Function Models#basis functions]]
- $$
p(\mathbf{t} \mid \mathbf{X}, \mathbf{w}, \beta)=\prod_{n=1}^{N} \mathcal{N}\left(t_{n} \mid \mathbf{w}^{\mathrm{T}} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right), \beta^{-1}\right)
$$
(3.10)
- 
$$
\begin{aligned}
\ln p(\mathbf{t} \mid \mathbf{w}, \beta) &=\sum_{n=1}^{N} \ln \mathcal{N}\left(t_{n} \mid \mathbf{w}^{\mathrm{T}} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right), \beta^{-1}\right) \\
&=\frac{N}{2} \ln \beta-\frac{N}{2} \ln (2 \pi)-\beta E_{D}(\mathbf{w})
\end{aligned}
$$
- sum-of-squares error function
$$
E_{D}(\mathbf{w})=\frac{1}{2} \sum_{n=1}^{N}\left\{t_{n}-\mathbf{w}^{\mathrm{T}} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right)\right\}^{2}
$$
## sum-of-squares error function
$$
E_{D}(\mathbf{w})=\frac{1}{2} \sum_{n=1}^{N}\left\{t_{n}-\mathbf{w}^{\mathrm{T}} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right)\right\}^{2}
$$
## The gradient of the log likelihood function   
- Setting this gradient to zero gives
$$
\nabla \ln p(\mathbf{t} \mid \mathbf{w}, \beta)=\sum_{n=1}^{N}\left\{t_{n}-\mathbf{w}^{\mathrm{T}} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right)\right\} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right)^{\mathrm{T}}
$$
$$
0=\sum_{n=1}^{N} t_{n} \phi\left(\mathbf{x}_{n}\right)^{\mathrm{T}}-\mathbf{w}^{\mathrm{T}}\left(\sum_{n=1}^{N} \phi\left(\mathbf{x}_{n}\right) \phi\left(\mathbf{x}_{n}\right)^{\mathrm{T}}\right)
$$
- Solving for w we obtain
$$
\mathbf{w}_{\mathrm{ML}}=\left(\mathbf{\Phi}^{\mathrm{T}} \mathbf{\Phi}\right)^{-1} \mathbf{\Phi}^{\mathrm{T}} \mathbf{t}
$$
$$
\Phi=\left(\begin{array}{cccc}
\phi_{0}\left(\mathbf{x}_{1}\right) & \phi_{1}\left(\mathbf{x}_{1}\right) & \cdots & \phi_{M-1}\left(\mathbf{x}_{1}\right) \\
\phi_{0}\left(\mathbf{x}_{2}\right) & \phi_{1}\left(\mathbf{x}_{2}\right) & \cdots & \phi_{M-1}\left(\mathbf{x}_{2}\right) \\
\vdots & \vdots & \ddots & \vdots \\
\phi_{0}\left(\mathbf{x}_{N}\right) & \phi_{1}\left(\mathbf{x}_{N}\right) & \cdots & \phi_{M-1}\left(\mathbf{x}_{N}\right)
\end{array}\right)
$$
- Moore-Penrose pseudo-inverse of the matrix Φ
- [[pseudo-inverse matrix]]
$$
\boldsymbol{\Phi}^{\dagger} \equiv\left(\boldsymbol{\Phi}^{\mathrm{T}} \boldsymbol{\Phi}\right)^{-1} \boldsymbol{\Phi}^{\mathrm{T}}
$$
- Indeed, if Φ is square and invertible,then using the property 
$(\mathbf{A B})^{-1}=\mathbf{B}^{-1} \mathbf{A}^{-1}$ we see that $\boldsymbol{\Phi}^{\dagger} \equiv \boldsymbol{\Phi}^{-1}$
## Error function
- [[#sum-of-squares error function]]
$$
E_{D}(\mathbf{w})=\frac{1}{2} \sum_{n=1}^{N}\left\{t_{n}-w_{0}-\sum_{i=1}^{M-1} w_{j} \phi_{j}\left(\mathbf{x}_{n}\right)\right\}^{2}
$$
- solving for w0
$$
w_{0}=\bar{t}-\sum_{j=1}^{M-1} w_{j} \overline{\phi_{j}}
$$
$$
\bar{t}=\frac{1}{N} \sum_{n=1}^{N} t_{n}
$$
$$
\overline{\phi_{j}}=\frac{1}{N} \sum_{n=1}^{N} \phi_{j}\left(\mathbf{x}_{n}\right)
$$
- maximize [[#logarithm of the likelihood function]] with respect to the noise precision parameter β
$$
\frac{1}{\beta_{\mathrm{ML}}}=\frac{1}{N} \sum_{n=1}^{N}\left\{t_{n}-\mathbf{w}_{\mathrm{ML}}^{\mathrm{T}} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right)\right\}^{2}
$$