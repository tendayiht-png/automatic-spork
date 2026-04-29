import json

def create_mock_dvsa_data():
    # Synthetic data mimicking a vehicle inspection log
    test_data = [
        {
            "inspection_id": "DVSA-1001",
            "vehicle_category": "HGV",
            "location": "Birmingham-North",
            "inspector": {
                "name": "Alex Smith",
                "id": "INSP-552"
            },
            "status": "Pass",
            "defects_found": 0
        },
        {
            "inspection_id": "DVSA-1002",
            "vehicle_category": "PCV",
            "location": "Solihull-East",
            "inspector": {
                "name": "Jordan Lee",
                "id": "INSP-881"
            },
            "status": "Fail",
            "defects_found": 3
        }
    ]
    
    with open('test_input.json', 'w') as f:
        json.dump(test_data, f, indent=4)
    print("Success: 'test_input.json' generated.")

if __name__ == "__main__":
    create_mock_dvsa_data()
