# Probability densities

 1. interval $(x,x+\delta x)$  by $p(x)\delta x$ for  $\delta x  \rightarrow 0$

$$p(x)=\int^b_a p(x)\mathrm{d}x$$

2. p(x) 满足两个条件
$p(x)\ge0$
$\int^{\infty} _{-\infty} p(x)dx=1$

3. if $x=g(y)$ then f(x) becomes $\tilde{f}(y)=f(g(y))$
$(x,x+\delta x)$transformed into the range $(y,y+\delta y)$ where $p_x(x)\delta x\simeq p_y(y)\delta y$
$$p_y(y) = p_x(x)\left| \frac{\mathrm{d}x}{\mathrm{d}y} \right|    
=p_x(g(y))\left|g^`(y)\right|$$

## cumulative distribution function 
$$P(z)=\int^{z}_{-\infty}p(x)\mathrm{d}x$$
- which $P^{`}(x)=p(x)$

## sum and product rules
- sum  $$p(x)=\int p(x,y)\mathrm{d}y$$
- product  $$ p(x,y)=p(y|x)p(x)$$

# Expectation and covariances
- discrete and continuous 
 $$E[f]=\sum_x p(x)f(x)$$
 $$E[f]=\int p(x)f(x)\mathrm{d}x$$
 ## sum over these points
- a finite number N of points drawn from the probability distribution or probability density .
$$E[f]=\simeq \frac{1}{N}\sum_{n=1}^N f(x_n)$$
## serval variables
$$E_x[f(x,y)]$$ denotes the average of the function f(x, y) with respect to the distribution of x.Note that $E_x[f(x,y)]$ will be a function of y
- Conditional expectation 
	$$\mathbb{E}_x[f|y]=\sum_x p(x|y)f(x)$$
- variance of f(x)
	$$\mathbb{var}[f]=\mathbb{E}[(f(x)-\mathbb{E}[f(x)])^2]$$
- variance of variable x itself
	$$\mathbb{var} [x]= \mathbb{E} [x^2]- \mathbb{E} [x]^2$$
- covariance 
	$$ cov[x,y]=E_{x,y}[\{ x-E[x] \}\{y-E[y]\}]\quad\quad =E_{x,y}[\boldsymbol{xy^T}]-E[\boldsymbol{x}]E[\boldsymbol{y^T}]$$