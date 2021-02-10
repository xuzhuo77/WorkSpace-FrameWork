## gaussian distribution
$$\mathcal{N}(x|\mu,\sigma^2)=\frac{1}{(2\pi\sigma^2)^{\frac{1}{2}}}exp\{ - \frac{1}{2\sigma^2}(x-\mu^2)\}$$

- average
$$E[x]=\int^{\infty}_{-\infty} \mathcal{N}(x|\mu,\sigma^2) x\mathrm{d}x =\mu$$
- second order moment
$$E[x^2]=\mu^2+\sigma^2$$
- variance 
$$ var[x]=E[x^2]-E[x]^2=\sigma^2$$

## gaussian distribution over D-dimensional 
$$\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu},\Sigma^2)
=\frac{1}{(2\pi)^{D/2}}\frac{1}{\left|\Sigma\right|^{1/2}}
exp\{ 
	-\frac{1}{2}
	(\boldsymbol{x}-\boldsymbol{\mu})^T 
	\Sigma^{-1}
	(\boldsymbol{x}-\boldsymbol{\mu})
\}$$

## dataset probability 
$$
p(\boldsymbol{x}|\mu,\sigma^2)
=\prod^{N}_{n=1}\mathcal{N}(x_n|\mu,\sigma^2)
$$
## log likelihood
$$
lnp(\boldsymbol{x}|\mu,\sigma^2)
=-\frac{1}{2\sigma^2}\sum^N_{n=1}(x_n-\mu)^2 
-\frac{N}{2}ln\sigma^2
-\frac{N}{2}ln(2\pi)
$$
## sample mean  and variance
- Maximizing (1.54) with respect to µ and σ2, we obtain the maximum likelihood solution
$$
\mu_{ML}
=\frac{1}{N}\sum_{n=1}^Nx_n
$$
$$
\sigma^2_{ML}
=\frac{1}{N}\sum_{n=1}^{N}(x_n-\mu_{ML})^2
$$

- on average the maximum likelihood estimate will obtain the correct mean but
will underestimate the true variance by a factor (N − 1)/N.
$$E[\mu_{ML}]=\mu$$
$$E[\sigma^2_{ML}]=(\frac{N-1}{N})\sigma^2$$
- unbiased
$$
\widetilde {\sigma^2}
=\frac{N}{N-1}\sigma^2
=\frac{1}{N-1}\sum_{n-1}^N(x_n-\mu_{ML})^2
$$



