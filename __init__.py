from flask import Flask, jsonify, request
from flask_restx import Api, fields, Resource
from flask import Blueprint
import csv
import datetime
from operator import sub
import joblib
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn import preprocessing, ensemble

'''
Starting point of the flask application. This file contains all necessary configurations
needed in this assessment.
'''

"""Flask & Swagger configurations"""
app=Flask(__name__)
api = Api(
        app = app, 
		  version = "1.0", 
		  title = "Genify Assessment", 
		  description = " Used to test the API for genify software development assessment"
)


