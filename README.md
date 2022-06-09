# Forecasting-Next-Day-Bitcoin-Prices

Web App : https://div-bitcoin-forecast-app.herokuapp.com/

Blog    : https://medium.com/p/cb833ab61183

**1. Getting Data:**
  Bitcoin related raw features were extracted from various sources, some of them were Web Scraped through custom python code using Beautiful Soup library, while others   extracted from available Web APIs.

  **source1:**  https://bitinfocharts.com/bitcoin/

  **source2:** https://alternative.me/crypto/fear-and-greed-index/

  **source3:** https://investpy.readthedocs.io/_api/crypto.html

  **source4:** https://data.nasdaq.com/data/BCHAIN/MIREV-bitcoin-miners-revenue

**2. Exploratory Data Analysis**
  EDA and statistical analysis done using Correlation plots and Kernel Density Estimates(KDE).

**3. Feature Engineering:**
Performed Feature Engineering using library TA-lib , Smoothening techniques were used to extract noise free features from the existing raw features that allows important patterns to stand out and to perform technical analysis.

**4.Feature Selection:**
**Modeling:**

Implemented Multivariate Forecasting models to predict next day BTC prices using previous day high dimensional data.

Exploratory Data Analysis(EDA) and statistical analysis done using Correlation plots and Kernel Density Estimates(KDE).

Bitcoin related raw features were extracted from various sources, some of them were Web Scraped through custom python code using Beautiful Soup library, while others extracted from available Web APIs.

Exploratory Data Analysis(EDA) and statistical analysis done using Correlation plots and Kernel Density Estimates(KDE).

Performed Feature Engineering using library TA-lib , Smoothening techniques were used to extract noise free features from the existing raw features that allows important patterns to stand out and to perform technical analysis.

Performed Feature Scaling through Scikit-Learn library, used either Robust Scalar followed by Min-Max Scalar or Standard Scaler to scale the data based on the performance.

Topmost important Features were selected after multiple iterations by Recursive Feature Elimination & Cross-Validated using an estimator Random Forest Regressor, and a correlation measure Variance Inflation Factor(VIF).

Support Vector Regression outperformed Linear Regression with SGD optimizer in terms of low Latency and performed better than Baseline model and other machine learning and deep learning models. Model deployed on Heroku platform using Flask API.
