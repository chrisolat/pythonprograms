import openpyxl
from bs4 import BeautifulSoup
import requests
import os
import sys

wb = openpyxl.load_workbook("USA list.xlsx")
sheet = wb.get_sheet_by_name("Feuil1")