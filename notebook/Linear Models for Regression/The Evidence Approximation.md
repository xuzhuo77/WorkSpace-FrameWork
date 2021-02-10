- hyperparameters α and β

## predictive distribution
$$
p(t \mid \mathbf{t})=\iiint p(t \mid \mathbf{w}, \beta) p(\mathbf{w} \mid \mathbf{t}, \alpha, \beta) p(\alpha, \beta \mid \mathbf{t}) \mathrm{d} \mathbf{w} \mathrm{d} \alpha \mathrm{d} \beta
$$
- p(t|w, β)
- p(w|t, α, β)
-  posterior distribution p(α, β|t) 

### marginalizing
-marginalizing over w in which α and β are fixed to the values $\widehat{\alpha}  \quad and\quad \widehat{\beta}$
$$
p(t \mid \mathbf{t}) \simeq p(t \mid \mathbf{t}, \widehat{\alpha}, \widehat{\beta})=\int p(t \mid \mathbf{w}, \widehat{\beta}) p(\mathbf{w} \mid \mathbf{t}, \widehat{\alpha}, \widehat{\beta}) \mathrm{d} \mathbf{w}
$$
### Bayes’ theorem
$$
p(\alpha,\beta) \propto p(t|\alpha,\beta)p(\alpha,\beta)
$$
###  ratio α/β is analogous to a regularization parameter
-  Student’s t-distribution over w
-  (Gamma) prior distributions over α and β
- [[Laplace approximation]]
-  [[expectation maximization]]

## Evaluation of the evidence function
### marginal likelihood function
$$p(t|\alpha,\beta)=\int p(t|w,\beta)p(w|\alpha)dw$$
###  log of the marginal likelihood
$$
\ln p(\mathbf{t} \mid \alpha, \beta)=\frac{M}{2} \ln \alpha+\frac{N}{2} \ln \beta-E\left(\mathbf{m}_{N}\right)-\frac{1}{2} \ln |\mathbf{A}|-\frac{N}{2} \ln (2 \pi)
$$
- Hessian matrix
 $$
\mathbf{A}=\nabla \nabla E(\mathbf{w})
$$
- E(mN)
$$
E\left(\mathbf{m}_{N}\right)=\frac{\beta}{2}\left\|\mathbf{t}-\mathbf{\Phi} \mathbf{m}_{N}\right\|^{2}+\frac{\alpha}{2} \mathbf{m}_{N}^{\mathrm{T}} \mathbf{m}_{N}
$$
$$
\mathbf{A}=\alpha\mathbf{I}+\beta\mathbf{\phi}^T\mathbf{\phi}
$$
- mN
$$
\mathbf{m}_N=\beta \mathbf{A}^{-1}\mathbf{\phi}^{T}\mathbf{t}
$$
## Maximizing the evidence function
