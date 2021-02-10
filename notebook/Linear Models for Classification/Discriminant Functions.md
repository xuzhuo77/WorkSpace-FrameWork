
## Two classes

$$
y(x)=w^Tx+w_0
$$
-  a linear discriminant function
- $w^T(x_A-x_B)=0$ ,so  w determines the orientation of the decision surface
- vector w is orthogonal to every vector lying within the decision surface
### normal distance
- normal distance from the origin to the decision surface is
given by
$$
\frac{w^Tx}{\|w\|}=-\frac{w_0}{\|w\|}
$$

$$
\mathbf{x}=\mathbf{x}_{\perp}+r \frac{\mathbf{w}}{\|\mathbf{w}\|}
$$
- $x_\perp$ be its orthogonal projection onto the decision surface
- Multiplying both sides of this result by wT and adding w0
$$
r=\frac{y(x)}{\|w\|}
$$
## Multiple classes
### K-class discriminant comprising K linear functions
$$
y_k(x)=w_k^Tx+w_k0
$$
- decision boundary between class Ck and class Cj is therefore given by $y_k(x) = y_j (x)$
### a (D − 1)-dimensional hyperplane
$$
(\mathbf{w}_k-\mathbf{w}_j)^T\mathbf{x}+(w_{k0}+w_{j0})=0
$$
- two points $x_A$ and $x_B$ both of which lie inside decision region $\mathcal{R}_k$
- $\widehat x$ that lies on the line connecting these two points must also lie in $\mathcal{R}_k$
$$
\widehat{x}=\lambda x_A+(1-\lambda)x_B
$$
$$
\mathcal{y}_k(\widehat{x})=\lambda \mathcal{y}_k(x_A)+(1-\lambda)\mathcal{y}_k(x_B)
$$
- $\widehat x$ also lies inside $\mathcal{R}_k$. Thus $\mathcal{R}_k$ is singly connected and convex.
$$y_k(\widehat x) > y_j (\widehat x),$$
- xa,xb都在同一侧 ,Rk为连通


## Least squares for classification
- goup
$$ y_k(x)=w_k^T x+w_0$$
$$ y(x)=\widehat W^T\widehat x$$
- $\widehat w_k=(w_{k0},w_k^T)$
- input $(1,x^T)$
###  sum-of-squares error function
$$E_D(\widehat W)
=\frac{1}{2}Tr\{ (\widehat X\widehat W -T)^T(\widehat X\widehat W -T)\}
$$
- Setting the derivative with respect to W, to zero
$$
\widetilde{\mathbf{W}}=\left(\tilde{\mathbf{X}}^{\mathrm{T}} \widetilde{\mathbf{X}}\right)^{-1} \widetilde{\mathbf{X}}^{\mathrm{T}} \mathbf{T}=\widetilde{\mathbf{X}}^{\dagger} \mathbf{T}
$$
###  discriminant function
$$y(x)=\widehat W^T\widehat x=\widehat T^T(\widehat X ^{\dagger})^T\widehat x
$$
###  some linear constraint
$$ a^Tt_n+b=0$$
$$ a^Ty(x)+b=0$$
## Fisher’s linear discriminant
$$y=w^Tx$$
### maximizes the class separation.
- a two-class problem in which there are N1 points of class C1 and N2 points of class C2
$$
m_1=\frac{1}{N_1}\sum_{n\in C_1}x_n   \quad \quad
m_2=\frac{1}{N_2}\sum_{n\in C_2}x_n
$$
### mean of the projected data from class Ck.
$$
m_k=\mathrm{w}^T \mathrm{m}_k
$$
### maximize while choose w
$$
m_2-m_1=\mathrm{w}^T (\mathrm{m}_2-\mathrm{m}_1)
$$
$$
\mathrm{w} \propto (\mathrm{m}_2-\mathrm{m}_1)
$$

## within-class variance
$$
\mathrm{s}_k^2=\sum_{n \in \mathcal{C}_k}(y_n-m_k)^2
$$
where $y_n=w^T x_n$
### whole data set 
- Fisher criterion
$$
\mathcal{J}{\mathrm(w)}=\frac{(m_2-m_1)^2}{s_1^2+s_2^2}
$$ 
$$
\mathcal{J}{\mathrm(w)}=\frac{w^TS_Bw}{w^TS_Ww}
$$
$$
\mathbf{S}_{\mathrm{B}}=\left(\mathbf{m}_{2}-\mathbf{m}_{1}\right)\left(\mathbf{m}_{2}-\mathbf{m}_{1}\right)^{\mathrm{T}}
$$
$$
\mathbf{S}_{W}=\sum_{n \in \mathcal{C}_{1}}\left(\mathbf{x}_{n}-\mathbf{m}_{1}\right)\left(\mathbf{x}_{n}-\mathbf{m}_{1}\right)^{\mathrm{T}}+\sum_{n \in \mathcal{C}_{2}}\left(\mathbf{x}_{n}-\mathbf{m}_{2}\right)\left(\mathbf{x}_{n}-\mathbf{m}_{2}\right)^{\mathrm{T}}
$$
- Differentiating J(w) with respect to w, we find that J(w) is maximized when
$$
(w^TS_Bw)S_Ww= (w^TS_Ww)S_Bw
$$

- only its direction of (m2−m1). ,Multiplying both sides of (4.29) by $S^{−1}_W$
we then obtain 
$$
w\propto S^{−1}_W(\mathrm{m}_2-\mathrm{m}_1)
$$
##  Fisher’s linear discriminant
$$
w\propto S^{−1}_W(\mathrm{m}_2-\mathrm{m}_1)
$$
## Relation to least squares
### sum-of-squares error function 
$$
E=\frac{1}{2}\sum_{n-1}{N}(w^Tx_n+w_0-t_n)^2
$$
- Setting the derivatives of E with respect to w0 and w to zero,
$$
\sum_{n=1}^{N}\left(\mathbf{w}^{\mathrm{T}} \mathbf{x}_{n}+w_{0}-t_{n}\right) =0 
$$
(4.33)
$$
\sum_{n=1}^{N}\left(\mathbf{w}^{\mathrm{T}} \mathbf{x}_{n}+w_{0}-t_{n}\right) \mathbf{x}_{n} =0
$$
(4.33)
$$
w_{0}=-\mathbf{w}^{\mathrm{T}} \mathbf{m}
$$

$$
\sum_{n=1}^{N} t_{n}=N_{1} \frac{N}{N_{1}}-N_{2} \frac{N}{N_{2}}=0
$$
- mean of the total data set and is given by
$$
\mathbf{m}=\frac{1}{N} \sum_{n=1}^{N} \mathbf{x}_{n}=\frac{1}{N}\left(N_{1} \mathbf{m}_{1}+N_{2} \mathbf{m}_{2}\right)
$$
-  making use of the choice tuation (4.33) becomes
$$
\left(\mathbf{S}_{\mathrm{W}}+\frac{N_{1} N_{2}}{N} \mathbf{S}_{\mathrm{B}}\right) \mathbf{w}=N\left(\mathbf{m}_{1}-\mathbf{m}_{2}\right)
$$
- we note that $\mathrm{S}_{\mathrm{B}} \mathrm{w}$ is always in the Thus we can write
$$
\mathbf{w} \propto \mathbf{S}_{\mathrm{W}}^{-1}\left(\mathbf{m}_{2}-\mathbf{m}_{1}\right)
$$
## Fisher’s discriminant for multiple classes
###  function of the projection matrix
$$
J(w)=Tr\{  
(WS_WW^T)^{-1}(WS_BW^T)
\}
$$
$$
J(W)=Tr{s_W^{-1}s_B}
$$
- covariance matrices
$$
s_W=\sum_{k=1}^{K}\sum_{n \in C_k}(y_n-\mu_k)(y_n-\mu_k)^T
$$
$$
s_B=\sum_{k=1}^{K}N_k(\mu_k-\mu)(\mu_k-\mu)^T
$$
- where 
$$
\mu_k=\frac{1}{N_k}\sum_{n \in C_k}y_n \quad 
\mu=\frac{1}{N}\sum_{n =1}^K N_k \mu_k
$$