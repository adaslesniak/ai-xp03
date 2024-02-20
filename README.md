# artifical inteligence-experiment 3

The goal is to play with the idea of function that measures data linearity. Data linerity is an assumption for lot of data analysis there is assumption that data must be lineary correlated. Eg. for linear regression, logistic regression, pca. But there is no simple way to check if data falls into such criteria.

So idea is that PCA assumes linear data, so let's create simple tool around it:
- get pca with all pca components
- reconstruct the data
- measure the reconstruction error

For ideally linear data there shall be no reconstruction error. For real world data, there is some noise, but still error should be small. Finally for data with strong non linear correlations error will be big.

Plan is to:
1. create simple function that does it
2. play with it a little bit, to check how it works for various data
3. optionally if results of 2 are fine, figure out how to summarize result, so it's normalized and readable for all data
4. optionally figure out optimization algorithm so it can sample the data and not work on all of it

# end of project status
It was all based on wrong data from some previous test. No, no, no. PCA always captures 100% of data (not counting for ability to represent some tiny differences by floating point), so difference between original data and restored data assuming pca_components equals number of features is in the order of 10 to power -30. 
