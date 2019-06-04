# TUTORIAL ON PCA
## Basic concepts
  - Definition: PCA (principal component analyses is a technique to transform a
    dataset onto a lower dimensional subspace for visualization and
    further exploration)
  - Definition_2: PCA is an orthogonal transformation
  - Definition_3: PCA transforms variables into a new set of variables that are
  a linear combination of the original ones: this new set is called principal
  components.
  - Principal component: eigenpairs (eigen values and eigen vectors):
  they describe the direction in the original feature space with the greatest
  variance (the pca is the line representing the relationship between two
    variables), number of PCAs == number of dimensions in the data
  - Variance: it is a measure of how spread out the data is.
  -Eigenvector def1: vector that does not change its direction under the
  associated linear combination
  - Eigenvector def2: in relation to a matrix A, an eigenvector is a vector
  where if you multiply the matrix A by that eigenvector you get the same as
  multiplying the vector by some scalar value. This scalar values is known as
  the eigen value.
  - Eigenvalue def1: scalars attached to eigenvectors that give the
  axis magnitude.Size of eigen values informs size of variance, thats
  why we sort them, the highest one is the main one, so one and so fort.    
  -
## Steps:
  - 1: standardize: (not a necessary step in case of images I assume)
  - 2: extract the mean
  - 3: Covariance matrix
  - 4: eigendecomposition
  - 5: sort in decreasing order and get the highest eigen values and their
   corresponding eigenvectors.
   - 6: Construct the projection matrix from those selected eigenvectors
   - 7: Transform original dataset via the new projection matrix, to obtain
   a new lower dimensional subspace.
## Questions
  - 1 Why is variance important when thinking about the structure of a dataset?
  - 2 Why eigen values and vectors? What is it about the concepts of eigen
  values and vectors that make them ideal to describe a dataset?
  - 3 Why do I care about visualization, for me as human fine, but for the matter
  of assessing relationships, I probably should not need to see it to know
  that the interesting relationship is there.
  - 4 Why do I subtract the mean?
  - 5 Why is it relevant to center the data in zero?
  - 6 What is a dimension when we discuss images?
  - 7 Is the eigen values a value that scales the eigen vector in the direction
  of the data with the most variance?
  - 8 Is the principal component the axis on the new subspace or is the actual
  points?
  - 9 "PCA maximizes variance" and?
  - 10 PCA is the resulting axis??
  - 11 is the eigenvalue the "explained variance measurement?" because it
  informs on the size of the variance of the eigenvector calculated for a
  certain set of data points.?

So far the basic idea seems to be, I have a dataset that is really high
dimensional. Meaning A lot of dimensions and I wan to find hidden relationships in this dataset.

I get the idea that projection onto 2d or 3d space is nice because it allows
me to see the data and then understand the realtionship.

High dimensional data has problems...
The best intuition here so far is this: from a certain dataset I don't want the
entire data, I want specific features, so having some model that somehow
adresses this need is good, meaning gets from my high dimensional data the
features, informations and relationships that I want.

## Intuitions
  - Reduce dimensions, reduce noise
  - Dim reduction --> could inform on the relevant formerly unknown features
  of the orginal high dimensional space by understanding which were the more
  relevant agents that informed the variance that allowed the generation of the
  eigenpairs on the new subspace.
  - Covariance matrix: matrix with all the relationships between features on
  the original space, describes variance on the data and covariacne along the
  variables
  - Covariance: measure of how much two variables change with respect to
  each other
  - Intuitions for standardization in PCA is: by doing that you see better how
  the different components in the new subspace contribute to the variance
  - Standardization: putting the data into the same unit scale: (mean 0 and
    variance 1)
  - Eigenvector: some vector that does not change direction after some
  transformation
  - Eigenvalues: model how growth of 2 populations affect each other.
  - Eigendecomposition: some sort of simplification where from a matrix of
  coefficients we get independent functions...or something...decoupling of
  how linear transformations act on data...
  - PCA is a linear transformation technique

Two main topics in dimensionality reduction as a whole: feature selection
and feature extraction.
  - Feature selection: I select meaningful features, or some model selects the
  meaningful features it perceives as more important (unsupervised learning)
  - Feature extraction: finding new features after transforming from high
  dimensional to low dimensional.

  Its interesting that the size of the calculated eigenvalues informs us about
  the the magnitude eigenvectors, which informs us about the size of the variance,
  if there is a big difference in this variance information, dropping
  one of these dimensions makes sense, because one of them explains our dataset
  way better than the other.


## Applications
  - Data visualization
  - Speeding up ML algorithms

## TODOs:
  1 - Get an intuition for what does a covariance matrix looks like <span style="color: red "> &
