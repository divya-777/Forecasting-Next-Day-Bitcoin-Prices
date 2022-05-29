import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVR
import joblib

data_selected_final_24_4 = pd.read_csv('data_selected_final_24_4.csv')

# function to scale data with standard scaler
def scale_data1(X_fit,X_tras):
  from sklearn.preprocessing import StandardScaler
  scale1 = StandardScaler()
  scale = make_pipeline(scale1)
  scale.fit(X_fit)
  return scale.transform(X_tras)

data_selected_final = data_selected_final_24_4.copy()
joblib.dump(data_selected_final,'data.pkl')

X = data_selected_final.iloc[:,1:-1]
y= data_selected_final.iloc[:,-1:]
X_scaled = scale_data1(X,X)

SVRegressor=SVR(kernel= 'linear', C= 1e+4)
SVRegressor.fit(X_scaled,np.ravel(y))
y_pred_SVM = SVRegressor.predict(X_scaled)
joblib.dump(SVRegressor,'modelsvr.pkl')
