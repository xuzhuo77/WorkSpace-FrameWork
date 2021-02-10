- model selection from a Bayesian perspective
- be applied to the determination of regularization parameters in linear regression

## models
- a set of L models $\{M_i\}$ where i = 1,...,L. 
## prior probability distribution $p(M_i)$
$$
p(M_i|D)\propto p(D|M_i)p(M_i)
$$
## model evidence $p(D|M_i)$
- which expresses the preference shown by the data for different models
###  marginal likelihood 
- because it can be viewed as a likelihood function over the space of models, in which the parameters have been marginalized out.
###  a Bayes factor
- 
$$
\frac{p(D|M_i)}{p(D|M_j)}
$$
## predictive distribution
$$
p(t|x,D)=\sum_{i=1}^{L}p(t|x,M_i,D)p(M_i|D)
$$
- weighted by the posterior probabilities p(Mi|D)
- averaging the predictive distributions p(t|x,Mi, D)

## predictive distribution governed by parameters w
### model evidence
$$
p(D|M_i)=\int p(D|w,M_i)p(w|M_i)\mathrm{d}w
$$
- like [[Bayesian  probabilities#denominator in Bayes’ theorem]]
### posterior distribution over parameters
 - evidence is precisely the normalizing
 $$
 p(w|D,M_i)=\frac{p(D|w,M_i)p(w|M_i)}{p(D|M_i)}
 $$
 
 ## approximation to the integral over parameters
 $$
p(\mathcal{D})=\int p(\mathcal{D} \mid w) p(w) \mathrm{d} w \simeq p\left(\mathcal{D} \mid w_{\mathrm{MAP}}\right) \frac{\Delta w_{\text {posterior }}}{\Delta w_{\text {prior }}}
$$
$$
\ln p(\mathcal{D}) \simeq \ln p\left(\mathcal{D} \mid w_{\mathrm{MAP}}\right)+\ln \left(\frac{\Delta w_{\text {posterior }}}{\Delta w_{\text {prior }}}\right)
$$
- model having a set of M parameters
$$
\ln p(\mathcal{D}) \simeq \ln p\left(\mathcal{D} \mid w_{\mathrm{MAP}}\right)+M\ln \left(\frac{\Delta w_{\text {posterior }}}{\Delta w_{\text {prior }}}\right)
$$
## expected Bayes factor
$$
\int p(D|M_1)\ln\frac{p|M_1}{p(D|M_2)}\mathrm{d}D
$$
- Kullback-Leibler divergence