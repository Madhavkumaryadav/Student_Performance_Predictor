import os 
import sys 


from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score 
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

def get_models():
    models={
                "Decision Tree":DecisionTreeRegressor(),
                "Random Forest":RandomForestRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(),
                "Linear Regression":LinearRegression(),
                "K-Neighbours classifier":KNeighborsRegressor(),
                "XGB Classifier":XGBRegressor(),
                "CatBoosting Classifier":CatBoostRegressor(),
                "AdaBoost Classifier":AdaBoostRegressor()
            }
    return models

def get_param():
    params={
    'Decision Tree':{
        'criterion':['squared_error','friedman_mse','absolute_error','poisson'],
        'splitter':['best','random'],
        'max_features':['sqrt','log2']
    },

    'Random Forest':{
        'criterion':['squared_error','friedman_mse','absolute_error','poisson'],
        'max_features':['sqrt','log2',None],
        'n_estimators':[8,32,64,128,256]
    },

    'Gradient Boosting':{
        'learning_rate':[0.01,0.05,0.1,0.2],
        'n_estimators':[8,16,32,64,128,256],
        'subsample':[0.6,0.8,1.0],
        'max_depth':[3,4,5]
    },

    'Linear Regression':{},

    'K-Neighbours classifier':{
        'n_neighbors':[3,5,7,9,11],
        'weights':['uniform','distance'],
        'algorithm':['auto','ball_tree','kd_tree','brute']
    },

    'XGB Classifier':{
        'learning_rate':[0.01,0.05,0.1,0.2],
        'n_estimators':[8,16,32,64,128,256]
    },

    'CatBoosting Classifier':{
        'depth':[6,8,10],
        'learning_rate':[0.01,0.05,0.1],
        'iterations':[30,50,100]
    },

    'AdaBoost Classifier':{
        'learning_rate':[0.1,0.01,0.5,0.001],
        'loss':['linear','square','exponential'],
        'n_estimators':[8,16,32,64,128,256]
    }
    }
    return params
