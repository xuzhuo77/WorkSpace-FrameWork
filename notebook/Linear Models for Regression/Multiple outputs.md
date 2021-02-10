## 

$$
\mathbf{y}(\mathbf{x}, \mathbf{w})=\mathbf{W}^{\mathrm{T}} \boldsymbol{\phi}(\mathbf{x})
$$
- where y is a K-dimensional column vector, W is an M × K matrix of parameters,
and φ(x) is an M-dimensional column vector with elements φj (x), with φ0(x)=1
as before. 
## conditional distribution of the target vector
$$
p(\mathbf{t} \mid \mathbf{x}, \mathbf{W}, \beta)=\mathcal{N}\left(\mathbf{t} \mid \mathbf{W}^{\mathrm{T}} \boldsymbol{\phi}(\mathbf{x}), \beta^{-1} \mathbf{I}\right)
$$
## log likelihood function 
$$
\begin{aligned}
\ln p(\mathbf{T} \mid \mathbf{X}, \mathbf{W}, \beta) &=\sum_{n=1}^{N} \ln \mathcal{N}\left(\mathbf{t}_{n} \mid \mathbf{W}^{\mathrm{T}} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right), \beta^{-1} \mathbf{I}\right) \\
&=\frac{N K}{2} \ln \left(\frac{\beta}{2 \pi}\right)-\frac{\beta}{2} \sum_{n=1}^{N}\left\|\mathbf{t}_{n}-\mathbf{W}^{\mathrm{T}} \boldsymbol{\phi}\left(\mathbf{x}_{n}\right)\right\|^{2}
\end{aligned}
$$
- maximize this function with respect to W
$$
\mathbf{W}_{\mathrm{ML}}=\left(\mathbf{\Phi}^{\mathrm{T}} \mathbf{\Phi}\right)^{-1} \mathbf{\Phi}^{\mathrm{T}} \mathbf{T}
$$
- each target variable tk
$$
\mathbf{w}_{k}=\left(\mathbf{\Phi}^{\mathrm{T}} \mathbf{\Phi}\right)^{-1} \mathbf{\Phi}^{\mathrm{T}} \mathbf{t}_{k}=\mathbf{\Phi}^{\dagger} \mathbf{t}_{k}
$$
- [[pseudo-inverse matrix]]