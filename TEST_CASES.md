# Test Cases – AI-Assisted Box Selection System

| Test ID | Test Scenario | Expected Result | Status |
|-------|-----------------------------------------|------------------------------------------|------|
| TC-01 | Product fits after rotation             | Returns True if a valid orientation fits | PASS |
| TC-02 | Calculate total order weight            | Returns the correct combined weight      | PASS |
| TC-03 | Recommend cheapest suitable box         | Returns the lowest-cost suitable box     | PASS |
| TC-04 | Order exceeds all box weight capacities | Returns None                             | PASS |

## Additional API Test

Endpoint: POST `/api/recommend-box/`

Input: One laptop and one mouse.

Expected Result:
- HTTP status: 200
- Total weight: 2.20 kg
- Recommended box: Small
- Box cost: ₹20.00

Actual Result: API returned HTTP 200 and recommended the Small box successfully.

## Test Execution

Run:

python manage.py test box_selection