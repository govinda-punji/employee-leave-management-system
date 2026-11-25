"""Employee Leave Management System
BCA Mini Project | Project No. 72 | Presented by Govind Punji
Python 3 console application.
"""

from datetime import datetime

employees = {
    "E101": {
        "name": "Amit",
        "leave_balance": {"Casual": 12, "Sick": 10, "Earned": 15},
    }
}

LEAVE_TYPES = ("Casual", "Sick", "Earned")
DATE_FORMAT = "%Y-%m-%d"


def parse_date(date_text):
    """Parse a date in YYYY-MM-DD format; raise ValueError if invalid."""
    return datetime.strptime(date_text.strip(), DATE_FORMAT).date()


def calculate_leave_days(from_date, to_date):
    """Return inclusive leave days; reject a to-date before from-date."""
    if to_date < from_date:
        raise ValueError("to-date cannot be before from-date.")
    return (to_date - from_date).days + 1


def display_leave_balance(employee_id):
    """Display remaining balances for the given employee."""
    employee = employees.get(employee_id.strip().upper())
    if employee is None:
        print("Invalid employee ID.")
        return
    print(f"Leave balance for {employee['name']} ({employee_id.strip().upper()}):")
    for leave_type in LEAVE_TYPES:
        print(f"{leave_type}: {employee['leave_balance'][leave_type]} days")


def apply_leave(employee_id, leave_type, from_text, to_text):
    """Validate and process a leave request. Return (approved, message)."""
    employee_id = employee_id.strip().upper()
    if employee_id not in employees:
        return False, "Invalid employee ID."

    normalized_type = leave_type.strip().title()
    if normalized_type not in LEAVE_TYPES:
        return False, "Invalid leave type. Choose Casual, Sick, or Earned."

    try:
        from_date = parse_date(from_text)
        to_date = parse_date(to_text)
        requested_days = calculate_leave_days(from_date, to_date)
    except ValueError as error:
        return False, f"Invalid dates: {error}"

    balance = employees[employee_id]["leave_balance"][normalized_type]
    if requested_days > balance:
        return False, (
            f"Leave rejected. Requested: {requested_days} days; "
            f"Available: {balance} days."
        )

    employees[employee_id]["leave_balance"][normalized_type] -= requested_days
    remaining = employees[employee_id]["leave_balance"][normalized_type]
    return True, (
        f"Leave approved: {requested_days} days {normalized_type} | "
        f"Balance {normalized_type}: {remaining}"
    )


def main():
    """Run the menu-driven console application."""
    while True:
        print("\\n===== Employee Leave Management System =====")
        print("1. Apply Leave")
        print("2. View Leave Balance")
        print("3. Exit")
        choice = input("Enter menu option: ").strip()

        if choice == "1":
            employee_id = input("Enter Employee ID: ")
            leave_type = input("Enter Leave Type (Casual/Sick/Earned): ")
            from_text = input("From (YYYY-MM-DD): ")
            to_text = input("To (YYYY-MM-DD): ")
            approved, message = apply_leave(
                employee_id, leave_type, from_text, to_text
            )
            print(message)
        elif choice == "2":
            employee_id = input("Enter Employee ID: ")
            display_leave_balance(employee_id)
        elif choice == "3":
            print("Thank you for using Employee Leave Management System.")
            break
        else:
            print("Invalid menu option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
