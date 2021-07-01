# Deep-learning-Cryptocurrency-price-prediction
Predict cryptocurrencies prices/trend using historical and social media feed data.

In the recent years, cryptocurrencies have been very popular. 
That's because their values change over time in a great extend. 
We tried to solve this problem by using both historical data and social media activity in order to 

- Predict future prices (Regression problem)
- Predict whether the price will increase or decrease (Classification problem)

### Install

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [Tensorflow](https://www.tensorflow.org/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html) or run it in [Google colab](https://colab.research.google.com/).

If you do not have Python installed yet, it is highly recommended to install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has some of the above packages and more included. 

### Dataset

For Cryptos historical data, we started by using the [Yahoo Finance](https://finance.yahoo.com/) however, because of the [Coinmarketcap](https://coinmarketcap.com/) provides also the dailly market cap, we collected them from there.
Regarding, social media activity data, their availabillity is limited accross the internet, at least for free. 
Cryptocompare and Lunarcrash apis used. 
Unfortunatelly, we didn't achieve to get data for the whole life of the coin by only for close to 3 years.

### Code

There are two main files
- Cryptocurrency price prediction.ipynb, which contains all the related models work.
- lunarcrushapi.py, which contains the get data from apis code we used.

#### Cryptocurrency price prediction

Contains:
- Section 1, Data preprocessing 
- Section 2, Regression with historical data 
- Section 3, Model hypertuning for regression problem 
- Section 4, Extend dataset with social media information
- Section 5, Results after applying normalization in the whole dataset (instead of windows)
- Section 6, Classification problem
- Section 7, Concatenated models and transfer learning

For more information check the [notebook](https://nbviewer.jupyter.org/github/teoad95/Deep-learning-Cryptocurrency-price-prediction/blob/main/Cryptocurrency%20price%20prediction.ipynb).

Additionally, you can find all experimental results [here](https://drive.google.com/drive/folders/1kx9G1Jd4V5zsnmkPqmR4rIk68lIsDAgE?usp=sharing).

