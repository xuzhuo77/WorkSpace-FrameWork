# 1 curve fitting
## polynomial 
$$
p(t|x, \boldsymbol{w}, \beta) 
= \mathcal{N}(t|y(x,\boldsymbol{w}),\beta^{-1})
$$ 


##  likelihood function 
$$
p(\boldsymbol {t}|\boldsymbol{x}, \boldsymbol{w}, \beta) 
= \prod_{n=1}^N \mathcal{N}(t_n|y(x_n,\boldsymbol{w}),\beta^{-1})
$$

##  log likelihood function
$$
\ln p(\boldsymbol {t}|\boldsymbol{x}, \boldsymbol{w}, \beta) 
=-\frac{\beta}{2}\sum_{n=1}^{N}\{y(x_n,w)-t_n\}^2
+\frac{N}{2}\ln \beta
-\frac{N}{2}\ln (2\pi)
$$
- we can equivalently minimize the negative log likelihood.
- to minimizing the sum-of-squares error function
## Maximizing[[#log likelihood function]] with respect to β gives 
$$
\frac{1}{\beta_{ML}}
= \frac {1}{N}  \sum_{n=1}^{N}\{y(x_n,w_{ML})-t_n\}^2
$$
## predictive distribution
- make predictions for new values of x
- substituting the maximum likelihood parameters into [[curve fitting#polynomial]] to give 
$$
p(t|x, \boldsymbol{w}_{ML}, \beta_{ML}) 
= \mathcal{N}(t|y(x,\boldsymbol{w}_{ML}),\beta^{-1}_{ML})
$$
## a prior distribution over the polynomial coefficients w.
- a Gaussian distribution of the form
$$
p(\boldsymbol{w}|\alpha)
=\mathcal{N}(\boldsymbol{w}|\boldsymbol{0},\alpha^{-1}\boldsymbol{I})
=(\frac{\alpha}{2\pi})^{(M+1)/2} exp\{ - \frac{\alpha}{2} \boldsymbol{w} ^T \boldsymbol{w}\}
$$

## product of the prior distribution and the likelihood function 
$$
p(\boldsymbol{w}|\boldsymbol{x}, \boldsymbol {t}, \alpha, \beta)
\propto
p(\boldsymbol {t}|\boldsymbol{x}, \boldsymbol{w}, \beta) p(\boldsymbol{w}|\alpha)
$$
- [[Bayesian  probabilities#in words]]









# 2 Bayesian curve fitting


## predictive distribution
$$
p(t|x, \boldsymbol{x}, \boldsymbol{t}) 
= \sum p(t|x, w) p(w|\boldsymbol{x}, \boldsymbol{t}) \mathrm{d}\boldsymbol{w}
$$
- p(t|x, w) is giv en by [[curve fitting#polynomial]]
- omitted the dependence on α and β to simplify the notation.
- Here p(w|x, t) is the posterior distribution over parameters, and can be found by normalizing the right-hand side of
##  predictive distribution
$$
p(t|x, \boldsymbol{x}, \boldsymbol{t}) 
= \mathcal{N}(t|m(x),s^2(X))
$$
- mean and variance
$$
m(x)
=\beta \boldsymbol{\phi(x)}^T\boldsymbol{S}\sum_{n=1}^N\boldsymbol{\phi}(x_n)t_n
$$
$$
s^2(x)
=\beta^{-1}+\boldsymbol{\phi}(x)^T\boldsymbol{S}\boldsymbol{\phi}(x)
$$
- Here the matrix S is given by
$$
\boldsymbol{S}^{-1}=\alpha \boldsymbol{I}+\beta\sum_{n=1}^N\boldsymbol{\phi}(x_n)\boldsymbol{\phi}(x)^T
$$

































