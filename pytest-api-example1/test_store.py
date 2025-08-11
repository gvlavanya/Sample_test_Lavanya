import requests
from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
#def test_patch_order_by_id():
 #   pass
#1) Creating a function to test the PATCH request /store/order/{order_id}

def patch_order(order_id, update_data):
    url = f"http://localhost:8000/store/order/{order_id}"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.patch(url, json=update_data, headers=headers)
    return response

 #3.Validate the response codes and values

def test_patch_order_success():
    order_id = 456  # Replace  real order ID in your system
    update_data = {
        "status": "shipped",
        "quantity": 5
    }

    response = patch_order(order_id, update_data)

    assert response.status_code == 200

    data = response.json()

    # Check values
    assert data["orderId"] == order_id
    assert data["status"] == update_data["status"]
    assert data["quantity"] == update_data["quantity"]

    #4) Validate  the  response  message "Order and pet status updated successfully"

    {
        "message": "Order and pet status updated successfully",
        "orderId": 123,
        "status": "shipped",
        "updated Date":"systemDate"
     }
    assert response.status_code == 200