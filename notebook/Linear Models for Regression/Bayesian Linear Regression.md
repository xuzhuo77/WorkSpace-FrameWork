# Parameter distribution
## a prior probability distribution over the model parameters w
- First note that the likelihood function p(t|w) defined by [[Maximum likelihood and least squares#logarithm of the likelihood function]] is the exponential of a quadratic function of w.
- The corresponding conjugate prior is therefore given by a Gaussian distribution of the form
$$
p(\mathbf{w})=\mathcal{N}\left(\mathbf{w} \mid \mathbf{m}_{0}, \mathbf{S}_{0}\right)
$$
- having mean m0 and covariance S0.
## posterior distribution
- which is proportional to the product of the likelihood function and the prior.
- Due to the choice of a conjugate Gaussian prior distribution, the posterior will also be Gaussian.
- [[Marginal and Conditional Gaussians]]
$$
p(\mathbf{w} \mid \mathbf{t})=\mathcal{N}\left(\mathbf{w} \mid \mathbf{m}_{N}, \mathbf{S}_{N}\right) 
$$
(3.49)
-  
$$
\mathbf{m}_{N} =\mathbf{S}_{N}\left(\mathbf{S}_{0}^{-1} \mathbf{m}_{0}+\beta \mathbf{\Phi}^{\mathrm{T}} \mathbf{t}\right) 
$$
(3.50)
$$
\mathbf{S}_{N}^{-1} =\mathbf{S}_{0}^{-1}+\beta \mathbf{\Phi}^{\mathrm{T}} \mathbf{\Phi}
$$
- (3.51)
### Gaussian prior
-  a particular form of Gaussian prior in order to simplify the treatment.
- consider a zero-mean isotropic Gaussian governed by a single precision parameter α
$$
p(\mathbf{w} \mid \alpha)=\mathcal{N}\left(\mathbf{w} \mid \mathbf{0}, \alpha^{-1} \mathbf{I}\right)
$$
- corresponding posterior distribution over w is then given by [[#posterior distribution]] (3.49)  with
$$
\mathbf{m}_{N} =\beta \mathbf{S}_{N} \boldsymbol{\Phi}^{\mathrm{T}} \mathbf{t}
$$
(3.53)
$$
\mathbf{S}_{N}^{-1} =\alpha \mathbf{I}+\beta \boldsymbol{\Phi}^{\mathrm{T}} \mathbf{\Phi}
$$

$$
\ln p(\mathbf{w} \mid \mathbf{t})=-\frac{\beta}{2} \sum_{n=1}^{N}\left\{t_{n}-\mathbf{w}^{\mathrm{T}} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right)\right\}^{2}-\frac{\alpha}{2} \mathbf{w}^{\mathrm{T}} \mathbf{w}+\mathrm{const.}
$$
- Other forms of prior over the parameters
 $$
p(\mathbf{w} \mid \alpha)=\left[\frac{q}{2}\left(\frac{\alpha}{2}\right)^{1 / q} \frac{1}{\Gamma(1 / q)}\right]^{M} \exp \left(-\frac{\alpha}{2} \sum_{j=1}^{M}\left|w_{j}\right|^{q}\right)
$$
- in which q = 2 corresponds to the Gaussian distribution, and only in this case is the
prior conjugate to the likelihood function (3.10)[[Maximum likelihood and least squares#logarithm of the likelihood function]]. 
# Predictive distribution

$$
p(t \mid \mathbf{t}, \alpha, \beta)=\int p(t \mid \mathbf{w}, \beta) p(\mathbf{w} \mid \mathbf{t}, \alpha, \beta) \mathrm{d} \mathbf{w}
$$
- omitted the corresponding input vectors x from the right-hand side 
- conditional distribution p(t|x, w, β) is given by [[Maximum likelihood and least squares#Gaussian noise model]]
- posterior weight distribution  p(w|t, α, β)   is given by [[#posterior distribution]] (3.49)


### predictive distribution
$$
p(t \mid \mathbf{x}, \mathbf{t}, \alpha, \beta)=\mathcal{N}\left(t \mid \mathbf{m}_{N}^{\mathrm{T}} \boldsymbol{\phi}(\mathbf{x}), \sigma_{N}^{2}(\mathbf{x})\right)
$$

-  the variance $\sigma_{N}^{2}(\mathbf{x})$ of the predictive distribution is given by
$$\sigma_{N}^{2}(\mathbf{x})=\frac{1}{\beta}+\phi(\mathbf{x})^{\mathrm{T}} \mathbf{S}_{N} \boldsymbol{\phi}(\mathbf{x})$$
(3.59)
$$
\sigma_{N+1}^{2}(\mathbf{x}) \leqslant \sigma_{N}^{2}(\mathbf{x})
$$

# Equivalent kernel
## predictive mean
-  (3.53)[[#Gaussian prior]]
$$
y\left(\mathbf{x}, \mathbf{m}_{N}\right)
=\mathbf{m}_{N}^{\mathrm{T}} \boldsymbol{\phi}(\mathbf{x})
=\beta \boldsymbol{\phi}(\mathbf{x})^{\mathrm{T}} \mathbf{S}_{N} \mathbf{\Phi}^{\mathrm{T}} \mathbf{t}
=\sum_{n=1}^{N} \beta \boldsymbol{\phi}(\mathbf{x})^{\mathrm{T}} \mathbf{S}_{N} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right) t_{n}
$$
## the equivalent kernel. 
$$
y(x,m_N)=\sum_{n=1}^Nk(x,x_n)t_n
$$

$$
k(\mathbf{x},\mathbf{x}^`)
= \beta \phi (\mathbf{x})^{T} S_N \phi (\mathbf{x}^`)
$$
- where SN is defined by (3.51). [[#posterior distribution]]
## equivalent kernel
- e equivalent kernel can be obtained by considering the covariance between y(x) and $y(x^`)$
$$
cov[y(\mathbf{x}),y(\mathbf{x}^`)]
= cov[\boldsymbol{\phi}^Tw,w^T\boldsymbol{\phi}(\mathbf{x}^`)]
= \boldsymbol{\phi}^TS_N\boldsymbol{\phi}(\mathbf{x}^`)
= \beta^{-1}k(\mathbf{x},\mathbf{x}^`)
$$

$$ 
\sum_{n=1}^N k(x,x_n)=1
$$

- in the form an inner product with respect to a vector ψ(x) of nonlinear functions,
$$
k(\mathbf{x}, \mathbf{z})=\boldsymbol{\psi}(\mathbf{x})^{\mathrm{T}} \boldsymbol{\psi}(\mathbf{z})
$$
$$
\boldsymbol{\psi}(\mathbf{x})
=\beta^{1/2}\mathbf{S}_{N} ^{1/2}\boldsymbol{\phi}(\mathbf{x})
$$