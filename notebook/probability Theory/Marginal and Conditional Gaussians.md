##
- Given a marginal Gaussian distribution for x and a conditional Gaussian distribution for y given x in the form
$$
p(\mathbf{x})=\mathcal{N}\left(\mathbf{x} \mid \boldsymbol{\mu}, \boldsymbol{\Lambda}^{-1}\right)
$$
(2.113)
$$
p(\mathbf{y} \mid \mathbf{x})=\mathcal{N}\left(\mathbf{y} \mid \mathbf{A} \mathbf{x}+\mathbf{b}, \mathbf{L}^{-1}\right)
$$
(2.114)

## 
- the marginal distribution of y and the conditional distribution of x given y are
given by
$$
p(\mathbf{y})=\mathcal{N}\left(\mathbf{y} \mid \mathbf{A} \boldsymbol{\mu}+\mathbf{b}, \mathbf{L}^{-1}+\mathbf{A} \mathbf{\Lambda}^{-1} \mathbf{A}^{\mathrm{T}}\right)
$$
(2.115)
$$
p(\mathbf{x} \mid \mathbf{y})=\mathcal{N}\left(\mathbf{x} \mid \mathbf{\Sigma}\left\{\mathbf{A}^{\mathrm{T}} \mathbf{L}(\mathbf{y}-\mathbf{b})+\mathbf{\Lambda} \boldsymbol{\mu}\right\}, \mathbf{\Sigma}\right)
$$
(2.116)
- where
$$
\boldsymbol{\Sigma}=\left(\boldsymbol{\Lambda}+\mathbf{A}^{\mathrm{T}} \mathbf{L} \mathbf{A}\right)^{-1}
$$
(2.117)