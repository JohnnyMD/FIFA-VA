import numpy                    as np
import pandas                   as pd

#from matplotlib      import pyplot  as plt
#from matplotlib.mlab import PCA 	 as mlabPCA




#read data from a CSV file, you can choose different delimiters
data=pd.io.parsers.read_csv('data.csv',
     delimiter=',',
     header=None,
     usecols=[0,1]
    )
data.columns=['X1','X2']
#pd.io.parsers.read_csv rturns a useful but complex type;
#to transform it in a numpy.array use .values
d=data.values
