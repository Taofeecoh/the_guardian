import os
from datetime import date, timedelta

import awswrangler as wr
import boto3
import pandas as pd
from dotenv import load_dotenv

import guardianmodule as gm