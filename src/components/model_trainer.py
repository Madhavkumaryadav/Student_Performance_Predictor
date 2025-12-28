import os
import sys
from dataclasses import dataclass

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

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_model

from src.hyperparameter import model_param



@dataclass 
class ModelTrainerConfig:
    train_model_file_path=os.path.join('artifacts','model.pkl')
    

class ModelTrainer:
    def __init__(self) -> None:
        self.model_trainer_config=ModelTrainerConfig()
        
        
    def initiate_model_trainer(self,train_array,test_arry):
        try:
            logging.info('Spliting Training and testing data ')
            x_train,y_train,x_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_arry[:,:-1],
                test_arry[:,-1]
            )
                
            models=model_param.get_models()
            params=model_param.get_param()
            
                
            model_report: dict=evaluate_model(
                x_train=x_train,
                y_train=y_train,
                x_test=x_test,
                y_test=y_test,
                models=models,
                params=params      
            )

            # Best model name (based on highest score)
            best_model_name = max(model_report, key=model_report.get) # type: ignore

            # Best model score
            best_model_score = model_report[best_model_name]

            # Best model object
            best_model = models[best_model_name]
                
            if best_model_score<0.6:
                raise CustomException("Noe best model Found " , sys)
            logging.info(f"Best Found Model on both training and testing dataset ")
                
            save_object(
                file_path=self.model_trainer_config.train_model_file_path,
                obj=best_model
            )
                
            predicted=best_model.predict(x_test)
                
            r2_square=r2_score(y_test,predicted)
                
            return r2_square
        except Exception as e :
            raise CustomException(e,sys)
            
                
