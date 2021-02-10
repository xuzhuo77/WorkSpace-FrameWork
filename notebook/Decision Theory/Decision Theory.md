 ### decision regions
 regions $\mathcal{R}_{k}$
### decision boundaries

 ## probabilities
 $$
 p(c_k|x)=\frac{p(x|C_k)p(C_k)}{p(x)}
 $$
 
 ##  Minimizing the misclassification rate
$$
p(\text { mistake }) =p\left(\mathbf{x} \in \mathcal{R}_{1}, \mathcal{C}_{2}\right)+p\left(\mathbf{x} \in \mathcal{R}_{2}, \mathcal{C}_{1}\right) 
$$
$$
=\int_{\mathcal{R}_{1}} p\left(\mathbf{x}, \mathcal{C}_{2}\right) \mathrm{d} \mathbf{x}+\int_{\mathcal{R}_{2}} p\left(\mathbf{x}, \mathcal{C}_{1}\right) \mathrm{d} \mathbf{x}
$$
##
p(x, C1) > p(x, C2)
## maximize the probability of being correct
- more general case of K classes
$$
p(correct)
=\sum_{k=1}^{k}p(x \in \mathcal{R}_{k},\mathcal{C}_{k})
=\sum_{k=1}^{k}\int_{\mathcal{R}_{k}}p(x,\mathcal{C}_{k})\mathrm{d} \mathbf{x}
$$
## Minimizing the expected loss
$$
E[L]=\sum_k\sum_j\int_{R_j}L_{kj}p(x,C_k)dx
$$
- use the product rule$p(x, C_k) = p(C_k|x)p(x)$  to eliminate the common factor of p(x).
- a loss matrix $L_{kj}$


## The reject option
 - uncertain about class membership
 - avoid making decisions on the difficult cases

## Inference and decision
### discriminant function
-  outputs are known as generative models
-  posterior probabilities directly are called discriminative models
## Loss functions for regression
$$
E[L]=\iint\{y(x)-t\}^2p(x,t)\mathrm{d}x\mathrm{d}t
$$
$$
\frac{\delta E[L]}{\delta y(x)}=2\int\{{y(x)-t}\}\quad p(x,t)\mathrm{d}t=0
$$
$$
y(x)=\frac{\int t p(x,t)\mathrm{d}t}{p(x)}=\int t p(t|x)\mathrm{d}t=E_t[t|x]
$$
## Minkowski loss
$$
E[L_q]=\iint\|y(x)-t\|^q p(x,t)\mathrm{d}x\mathrm{d}t
$$