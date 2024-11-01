import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        model: str,
        seller_type: str,
        fuel_type: str,
        transmission_type: str,
        vehicle_age: int,
        km_driven: int,
        mileage: int,
        engine: int,
        max_power: int,
        seats: int
        ):

        self.model = model
        self.seller_type = seller_type
        self.fuel_type = fuel_type
        self.transmission_type = transmission_type
        self.vehicle_age = vehicle_age
        self.km_driven = km_driven
        self.mileage = mileage
        self.engine=engine
        self.max_power=max_power
        self.seats=seats

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "model": [self.model],
                "seller_type": [self.seller_type],
                "fuel_type": [self.fuel_type],
                "transmission_type": [self.transmission_type],
                "vehicle_age": [self.vehicle_age],
                "mileage": [self.mileage],
                "engine": [self.engine],
                "max_power": [self.max_power],
                "seats": [self.seats]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

