## Bayes' theorem 
$$p(w|D)=\frac{p(D|w)p(w)}{p(D)}$$
- $p(D|w)$ is a likelihood function 
- It expresses how probable the observed data set is for different settings of the parameter vector w.
-  Note that the likelihood is not a probability distribution over w, and its integral with respect to w does not (necessarily) equal one

## in words
$$posterior \propto likelihood \times prior$$
- where all of these quantities are viewed as functions of w.
- The denominator in[[#Bayes' theorem]] is the normalization constant, which ensures that the posterior distribution on the left-hand side is a valid probability density and integrates to one.

## denominator in Bayes’ theorem 
- integrating both sides of [[#Bayes' theorem]]
$$
p(D)=\int p(D|w)p(w)dw
$$