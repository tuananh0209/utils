import json


# Assuming 'notifications' is your defaultdict object
def log_defaultdict(notifications):
    for account_type, account_info in notifications.items():
        for notification_type, notification_list in account_info.items():
            for notification in notification_list:
                timestamp, details = notification
                print(f"{Colors.HEADER}Timestamp:{Colors.ENDC} {timestamp}")
                print(f"{Colors.WARNING}Details:{Colors.ENDC} {json.dumps(details, indent=4)}")
        print("-" * 200)  # Separator for readability


def log_balances(balances_dict):
    for account_type, balance_data in balances_dict.items():
        print(f"{Colors.HEADER}Account Name:{Colors.ENDC} {account_type}")
        for date_time, balance in balance_data:
            print(f"\t{Colors.WARNING}Date & Time:{Colors.ENDC} {date_time}")
            for balance_dimension, amount in balance.items():
                print(f"\t\t{Colors.BLUE}{balance_dimension}{Colors.ENDC}: {amount}")
        print("-" * 200)  # Separator for readability


class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
