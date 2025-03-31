import os
from idlelib import testing

import requests
import pytest
import logging
from api_testing_framework.utils.api_config import BASE_URL
from api_testing_framework.utils.excel_reader import read_test_data_from_excel  # Import the Excel reading function

# api_test_framework/
# ├── Dockerfile
# ├── test_data/
# │   └── test_data.xlsx  # Excel file with Test Case ID and Endpoint
# ├── tests/
# │   └── test_api.py #Main file
# └── utils/
#     ├── read_excel.py  # Contains the function to read test data from Excel
#     └── api_config.py  # Contains API base URL

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Test data from Excel
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'utils', 'test_data.xlsx')
test_data = read_test_data_from_excel(
    file_path)


# Pytest Parametrization for test cases
@pytest.mark.parametrize("test_case_id, endpoint", test_data)
def test_api_response(test_case_id, endpoint):
    url = BASE_URL + endpoint
    response = requests.get(url)

    assert response.status_code == 200, f"{test_case_id} - Failed with status code {response.status_code}"
    logging.info(f"{test_case_id} - PASSED with status code {response.status_code}")
