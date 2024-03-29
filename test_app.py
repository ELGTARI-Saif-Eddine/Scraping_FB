import pytest
from starlette.testclient import TestClient
from scrap_fb_pages import app  

@pytest.fixture
def test_client():
    return TestClient(app)

def test_start_scraping_endpoint(test_client):
    # Test with valid parameters
    response = test_client.get("/start_scraping?&page_name=NatGeoAbuDhabi&posts_count=5")
    assert response.status_code == 200
    assert response.json() == {"message": "Scraping completed successfully!"}

    # Test with invalid parameters (simulate an error)
    response = test_client.get("/start_scraping?&page_name=InvalidPage&posts_count=5")
    assert response.status_code == 200  # The status code based on actual implementation
    assert response.json() == {"message": "Expected Error Message"}
