# Employee Leave Management System

**BCA Python 3 Console Project**

## Project objective
A console application that allows an employee to apply for leave, calculates the number of leave days, checks the available balance, approves or rejects the request, and displays leave balances.

## Employee data
The project includes the employee record specified in the assignment:

- Employee ID: `E101`
- Name: Amit
- Casual leave: 12 days
- Sick leave: 10 days
- Earned leave: 15 days

## Features
1. Apply for Casual, Sick, or Earned leave.
2. Validate employee ID and leave type.
3. Validate dates in `YYYY-MM-DD` format.
4. Calculate leave days inclusively (both from-date and to-date count).
5. Reject a request when the requested days exceed the available balance.
6. Deduct the balance only when leave is approved.
7. View the employee's remaining leave balance.

## Concepts used
- Python dictionaries
- Functions
- `datetime` module
- Conditional statements
- Loops
- Input validation

## How to run
Python 3 is required. No external packages are needed.

```bash
python3 employee_leave_management.py
```

## Test cases from the assignment

### Test 1: Normal input
- Employee: E101
- Leave type: Casual
- From: 2026-12-10
- To: 2026-12-12
- Expected: 3 days approved; Casual balance becomes 9.

### Test 2: Boundary / minimum input
- Employee: E101
- Leave type: Casual
- From: 2026-11-02
- To: 2026-11-13
- Expected: 12 days approved; Casual balance becomes 0.

### Test 3: Invalid input
- Employee: E101
- Leave type: Sick
- From: 2026-12-15
- To: 2026-12-10
- Expected: Invalid dates; to-date cannot be before from-date. Balance remains unchanged.

### Test 4: Insufficient balance
- Employee: E101
- Leave type: Casual
- From: 2027-01-01
- To: 2027-01-14
- Expected: Request rejected (14 requested, 12 available); balances remain Casual 12, Sick 10, Earned 15.

## Note
Balances are held in memory and reset to the initial values whenever the program is restarted. This is consistent with the assignment's minimum requirements; file/database persistence is not included.
