import requests
import pandas as pd
from bs4 import BeautifulSoup

new_list = list(range(500))  # Assuming you have a list of 500 elements

# Using list slicing to create a new list with elements from index 200 to the end
new_list = new_list[200:]

print(new_list)
