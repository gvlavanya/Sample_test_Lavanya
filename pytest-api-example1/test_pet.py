from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", [("available")])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)
    # TODO...
# Define all possible statuses to test
ALL_STATUSES = ["available", "pending", "sold"]

@pytest.mark.parametrize("status", ALL_STATUSES)
def test_pets_by_status_schema(status):
    endpoint = f"/pets?status={status}"
    response = api_helpers.get_api_data(endpoint)
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
def test_get_by_id_404():
    # TODO...
    invalid_pet_id = 9999  # Choose an ID that you know does not exist
    endpoint = f"/pets/{invalid_pet_id}"

    response = api_helpers.get_api_data(endpoint)

    # Validate 404 status code
    assert response.status_code == 404, f"Expected 404 Not Found, got {response.status_code}"
    pass