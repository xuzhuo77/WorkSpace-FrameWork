### posterior probability for class C1
$$
p(c_1|x)
=\frac
{ p(x|c_1)p(c_1)}
{p(x|c_1)p(c_1)+p(x|c_2)p(c_2)}
$$
### logistic sigmoid function
$$
=\frac{1}{1+exp(-a)}=\sigma(a)
$$
$$
a=\ln \frac
{p(x|c_1)p(c_1)}
{p(x|c_2)p(c_2)}
$$
### symmetry property
$$
\sigma(-a)=1-\sigma(a)
$$
###  inverse of the logistic sigmoid
$$
a=\ln(\frac{\sigma}{1-\sigma})
$$

### log odds
$$
\ln[\frac{p(C_1|x)}{p(C_2|x)}]
$$

## softmax function
$$
p(C_k|x)  =\frac{p(x|C_k)p(C_k)}{\sum_j p(x|C_j)p(C_j)}
 =\frac{exp(a_k)}{\sum_j exp(a_j)}
$$
- where 
$$a_k=\ln p(x|C_k)p(C_k)$$

## continuous inputs
$$p(x|C_k)
=\frac{1}{(2\pi)^{D/2}}\frac{1}{\left|\Sigma\right|^{1/2}}
exp\{ 
	-\frac{1}{2}
	(\boldsymbol{x}-\boldsymbol{\mu_k})^T 
	\Sigma^{-1}
	(\boldsymbol{x}-\boldsymbol{\mu_k})
\}$$
- two classes
$$
p(C_1|x)=\sigma (w^T x+w_0)
$$
$$
w=\Sigma^{-1}(\mu_1-mu_2) 
$$
$$
w_0=-\frac{1}{2}\mu_1^T\Sigma^{-1}\mu_1+\frac{1}{2}\mu_2^T\Sigma^{-1}\mu_2+\ln \frac{p(C_1)}{p(C_2)}
$$

- K classes 
$$
a_k(x)=w^T_k x+w_{k0}
$$
$$
\mathrm{w}_k=\Sigma^{-1}\mu_k
$$
$$
w_{k0}=-\frac{1}{2}\mu_k^T\Sigma^{-1}\mu_k+\ln p(C_k)
$$

## maximum likelihood solution
$$
p(C_1)=\pi \quad p(C_2)=1-\pi 
$$
$$
p(x_n,C_1)=p(C_1)p(x_n|C_1)=\pi \mathcal{N}(x_n|\mu_1,\Sigma)
$$
$$
p(x_n,C_2)=p(C_1)p(x_n|C_2)=(1-\pi) \mathcal{N}(x_n|\mu_2,\Sigma)
$$
### likelihood function
$$
p(\mathrm{t}|\pi,\mu_1,\mu_2,\Sigma)
=\prod^{N}_{n=1} p(x_n,C_1)^{t_n} p(x_n,C_2)^{1-t_n}
$$
$$
=\prod^{N}_{n=1} [\pi \mathcal{N}(x_n|\mu_1,\Sigma)]^{t_n} 
[(1-\pi) \mathcal{N}(x_n|\mu_2,\Sigma)]^{1-t_n}
$$
###  log likelihood function
- Consider first the maximization with respect to π
$$
\sum_{n=1}^{N}\{t_n \ln\pi+(1-t_n)\ln(1-\pi))
\}
$$
$$
\pi=\frac{1}{N}\sum_{n=1}{N}t_n=\frac{N_1}{N}=\frac{N_1}{N_1+N_2}
$$
- consider the maximization with respect to $\mu_1$
$$
\sum_{n=1}^{N}t_n \ln{\mathcal{N}(x_n|\mu_1,\Sigma)}
=\frac{1}{2}\sum_{N}^{n=1}t_n(x_n-\mu_1)^T\Sigma^{-1}(x_n-\mu_1)+const
$$
$$
\mu_1=\frac{1}{N_1}\sum_{n=1}^{N}t_nx_n
$$
$$
\mu_2=\frac{1}{N_2}\sum_{n=1}^{N}(1-t_n) x_n
$$
- r the shared covariance matrix $\Sigma$
$$
	-\frac{N}{2}\ln |\Sigma|-\frac{N}{2}Tr\{\Sigma^{-1}\mathrm{S}\}
$$
$$
S=\frac{N_1}{N}S_1+\frac{N_2}{N}S_2
$$
$$
S_1=\frac{1}{N}\sum_{n \in C_1}(x_n-\mu_1)(x_n-\mu_1)^T
$$
$$
S_2=\frac{1}{N}\sum_{n \in C_2}(x_n-\mu_2)(x_n-\mu_2)^T
$$
## discrete features
- binary feature $x_i \in \{ 0,1 \}$
### naive Bayes
- in which feature values are treated as independent
$$
p(x|C_k)=\prod_{i=1}^{D}\mu_{ki}^{x_{i}}(1-\mu_{ki})^{1-x_i}
$$
$$
a_k(x)=\sum_{n=1}^{D}\{ x_i\ln \mu_{ki}+(1-x_i)\ln(1-\mu_{ki})\}+\ln{p(C_k)}
$$
## exponential family
$$
p(x|\lambda_k)=h(x)g(\lambda_k)exp\{\lambda_k^T\mu(x)\}
$$
$$
p(x|\lambda_k,s)=\frac{1}{s}h(\frac{1}{s}x)g(\lambda_k)exp\{\frac{1}{s}\lambda_k^Tx\}
$$
$$
a(X)=(\lambda_1-\lambda_2)^Tx+\ln g(\lambda_1)-\ln g(\lambda_2)+\ln p(C_1)-\ln p(C_2)
$$
$$
a_k(x)=\lambda_k^Tx+\ln g(\lambda_k)+\ln p(C_k)
$$