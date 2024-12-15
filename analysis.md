# **Analysis**

## **Dataset Overview**

For this assignment, I chose the `Iris` dataset. This dataset contains 150 samples of iris flowers, each with four features (sepal length, sepal width, petal length, and petal width) and a target label (species).

The dataset includes the following key features:

- **Feature 1**: Sepal Length (cm)
- **Feature 2**: Sepal Width (cm)
- **Feature 3**: Petal Length (cm)
- **Feature 4**: Petal Width (cm)
- **Target**: Species (setosa, versicolor, virginica)
- **Classes**: 3
- **Data Points**: 150

---

## **Steps Followed**

### **1. Data Exploration**

- **Structure and Summary**:
  - The dataset consists of 150 rows and 5 columns.
- **Data Types**:
  - Features include float values, and the target is a categorical variable.
- **Random Sample**:
  - A quick look at 5 random rows helped ensure data validity.

Analysis output:

```bash
(.venv) dorpascal@MacBook-Air-4 ps7-visualization-Dor-sketch % python3 ./main.py
**Author**: R.A. Fisher
**Source**: [UCI](https://archive.ics.uci.edu/ml/datasets/Iris) - 1936 - Donated by Michael Marshall
**Please cite**:

**Iris Plants Database**
This is perhaps the best known database to be found in the pattern recognition literature.  Fisher's paper is a classic in the field and is referenced frequently to this day.  (See Duda & Hart, for example.)  The data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant.  One class is     linearly separable from the other 2; the latter are NOT linearly separable from each other.

Predicted attribute: class of iris plant.
This is an exceedingly simple domain.

### Attribute Information:
    1. sepal length in cm
    2. sepal width in cm
    3. petal length in cm
    4. petal width in cm
    5. class:
       -- Iris Setosa
       -- Iris Versicolour
       -- Iris Virginica

Downloaded from openml.org.
   sepallength  sepalwidth  petallength  petalwidth        class
0          5.1         3.5          1.4         0.2  Iris-setosa
1          4.9         3.0          1.4         0.2  Iris-setosa
2          4.7         3.2          1.3         0.2  Iris-setosa
3          4.6         3.1          1.5         0.2  Iris-setosa
4          5.0         3.6          1.4         0.2  Iris-setosa
Sample data:
     sepallength  sepalwidth  petallength  petalwidth            class
41           4.5         2.3          1.3         0.3      Iris-setosa
50           7.0         3.2          4.7         1.4  Iris-versicolor
133          6.3         2.8          5.1         1.5   Iris-virginica
93           5.0         2.3          3.3         1.0  Iris-versicolor
144          6.7         3.3          5.7         2.5   Iris-virginica
Summary statistics:
       sepallength  sepalwidth  petallength  petalwidth
count   150.000000  150.000000   150.000000  150.000000
mean      5.843333    3.054000     3.758667    1.198667
std       0.828066    0.433594     1.764420    0.763161
min       4.300000    2.000000     1.000000    0.100000
25%       5.100000    2.800000     1.600000    0.300000
50%       5.800000    3.000000     4.350000    1.300000
75%       6.400000    3.300000     5.100000    1.800000
max       7.900000    4.400000     6.900000    2.500000
Data types:
sepallength     float64
sepalwidth      float64
petallength     float64
petalwidth      float64
class          category
dtype: object
Available features: ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'class']
Selected features:  ['sepallength', 'petallength']
2024-12-15 09:53:53.818 Python[48964:5660928] +[IMKClient subclass]: chose IMKClient_Modern
2024-12-15 09:53:53.819 Python[48964:5660928] +[IMKInputSession subclass]: chose IMKInputSession_Modern
(.venv) dorpascal@MacBook-Air-4 ps7-visualization-Dor-sketch %
```

---

### **2. Selected Features**

From the dataset, I selected the following features for detailed analysis:

1. **Feature A**: Sepal Length (cm)
2. **Feature B**: Petal Length (cm)

---

### **3. Visualization**

#### **Histograms**

[Histograms](./hist_plot.png)

#### **Scatter Plots**

Scatter plots were generated to explore correlations between the selected features:

[Scatter Plot A vs B](./scatter_plot_A_vs_B.png)

- **First Plot**: Sepal Length vs Petal Length (cm)
  - This plot ahows a positive linear relationship between Sepal Length and Petal Length. Aka, as Sepal Length increases, Petal Length also increases.
- **Second Plot**: Sepal Width vs Petal Length (cm)
  - This plot shows a weak correlation between Sepal Width and Petal Length.
  - The data points are scattered, indicating no clear relationship between the two features.
- **Third Plot**:  Petal length vs Petal length (cm)
  - This plot shows a strong positive linear relationship since we compare the same feature.
- **Forth Plot**: Petal width vs Petal length (cm)
  - This plot shows a strong positive linear relationship between Petal Width and Petal Length.
- **Fifth Plot**: Class vs Petal length (cm)
  - This plot shows a clear separation of the classes based on Petal Length.
  - Iris-setosa has the smallest Petal Length, while Iris-virginica has the largest.
  - Iris-versicolor falls in between the other two classes.
  - This indicates that Petal Length is a good feature for classifying the iris species.

---

## **Key Insights**

### **Correlation Plot Analysis**

I chose the scatter plot for sepallength vs peta length
for further analysis because:

- It showed a strong positive linear relationship.
- This suggests that Sepal Length is a good predictor for Petal Length.
- The plot was saved as `correlation_plot.png`.

[Correlation Plot](./correlation_plot.png)

### **Patterns Observed**

- **Positive Correlation**:
  - Sepal Length and Petal Length showed a strong positive correlation.
  - As Sepal Length increased, Petal Length also increased.
  - This indicates a linear relationship between the two features.
  - The scatter plot showed a clear pattern of data points aligned in a positive direction.
  - This suggests that Sepal Length can be a good predictor for Petal Length.

---

## **Conclusion**

This analysis highlights:

- The importance of selecting relevant features for analysis.
- The significance of visualizations in understanding data relationships.
- The value of correlation analysis in identifying patterns and trends.
- The potential of certain features as predictors for target variables.
- The need for further exploration to gain deeper insights into the dataset.

By following these steps, we can gain valuable insights from the data and make informed decisions based on the analysis.
