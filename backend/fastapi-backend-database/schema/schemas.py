def individual_serialise(aadhar) -> dict:
    return {
        "id": str(aadhar['_id']),
        "name": aadhar['name'],
        "dob": aadhar['dob'],
        "gender": aadhar['gender'],
        "aadhar_no": aadhar['aadhar_no']
    }


def list_serialise(aadhars) -> list:
    return [individual_serialise(aadhar) for aadhar in aadhars]
