## Logistic regression
$$
p(C_1|\phi)=y(\phi)=\sigma(w^T\phi)
$$
$$
p(C_2|\phi)=1-p(C_1|\phi)
$$
 ## derivative of the logistic sigmoid function
 $$
 \frac{d\sigma}{da}=\sigma(1-\sigma)
 $$
 ### likelihood function 
 $$
 p(t|w)=\prod_{n=1}^{N}y_n^{t_n}\{1-y_n\}^{1-t_n}
 $$
 $$
 y_n=p(C_1|\phi_n)
 $$
 ### cross-entropy
 $$
 E(w)=-\ln p(t|w)
 =-\sum_{n=1}^{N}\{t_n \ln y_n +(1-t_n)\ln (1-y_n) \}
 $$
 $$
 y_n=\sigma(a_n)   \quad  a_n=w^T\phi_n
 $$
 - an error function by taking the negative logarithm of the likelihood
###  gradient of the error function
$$
\nabla E(w) =\sum_{n=1}^{N}(y_n-t_n)\phi_n
$$
## Iterative reweighted least squares
### Newton-Raphson
$$
w^{(new)}=w^{(old)}-H^{-1}\nabla E(w)
$$
$$
\nabla E(w) =\sum_{n=1}^{N}(w^T\phi_n-t_n)\phi_n
=\mathrm{\phi}^T\mathrm{\phi}w-\mathrm{\phi}^T\mathrm{t}
$$
- Hessian matrix
$$
\nabla\nabla E(w)
=\sum_{n=1}^{N}\phi_n\phi_n^T
=\mathrm{\phi}^T{\phi}
$$
- then 
$$
w^{(new)}=w^{(old)}-(\mathrm{\phi}^T\mathrm{\phi})^{-1}\{\mathrm{\phi}^T\mathrm{\phi}w^{(old)}-\phi^Tt\}
=(\phi^T\phi)^{-1}\phi^Tt
$$
### update to the cross-entropy error function
-  gradient and Hessian 
$$
\nabla E(w) =\sum_{n=1}^{N}(y_n-t_n)\phi_n=\phi^T(y-t)
$$
$$
\mathrm{H}=\nabla\nabla E(w)
=\sum_{n=1}^{N}y_n(1-y_n)\phi_n\phi_n^T
=\mathrm{\phi}^T\mathrm{R}\mathrm{\phi}
$$
$$
R_{nn}=y_n(1-y_n)
$$
- 
$$
\begin{aligned}
\mathbf{w}^{(\text {new })} &=\mathbf{w}^{(\text {old })}-\left(\Phi^{\mathrm{T}} \mathbf{R} \Phi\right)^{-1} \Phi^{\mathrm{T}}(\mathbf{y}-\mathbf{t}) \\
&=\left(\Phi^{\mathrm{T}} \mathbf{R} \Phi\right)^{-1}\left\{\Phi^{\mathrm{T}} \mathbf{R} \Phi \mathbf{w}^{(\text {old })}-\Phi^{\mathrm{T}}(\mathbf{y}-\mathbf{t})\right\} \\
&=\left(\mathbf{\Phi}^{\mathrm{T}} \mathbf{R} \Phi\right)^{-1} \Phi^{\mathrm{T}} \mathbf{R} z
\end{aligned}
$$
$$
z=\phi w^{(old)}-R^{-1}(y-t)
$$
## Multiclass logistic regression
## Probit regression
## Canonical link functions