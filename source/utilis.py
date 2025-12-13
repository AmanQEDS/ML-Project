import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from source.exception import customException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise customException(e, sys)



def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for i in range(len(list(models))):

            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            para = param[model_name]

            # ---------------------------------------------------------
            # SPECIAL FIX: CatBoostRegressor DOES NOT WORK WITH GridSearchCV
            # ---------------------------------------------------------
            if "CatBoost" in model_name or "CatBoosting" in model_name:
                model.grid_search(para, X_train, y_train)
                model.fit(X_train, y_train)

                y_test_pred = model.predict(X_test)
                report[model_name] = r2_score(y_test, y_test_pred)
                continue
            # ---------------------------------------------------------

            # Normal models -> use GridSearchCV
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Test predictions
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report

    except Exception as e:
        raise customException(e, sys)



def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise customException(e, sys)
