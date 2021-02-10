$$
y(x)=f(w^T\phi(x))
$$

$$
f(a)=\left\{
\begin{array}
{ll}
+1, & a \geqslant 0 \\
-1, & a<0
\end{array}
\right.
$$ 
$$
E_P(w)=-\sum_{n \in M}w^T\phi_n t_n
$$

$$
w^{\tau+1}=w^{\tau}-\eta \nabla E_P(w)=w^{\tau}+\eta \phi_n t_n
$$