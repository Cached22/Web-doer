```python
from review_bot.config.settings import ACCOUNT_LIST
import json
import os

class AccountManager:
    def __init__(self):
        self.account_file = 'accounts.json'
        self.load_accounts()

    def load_accounts(self):
        if not os.path.exists(self.account_file):
            with open(self.account_file, 'w') as file:
                json.dump(ACCOUNT_LIST, file)
        with open(self.account_file, 'r') as file:
            self.accounts = json.load(file)

    def get_unused_account(self):
        for account in self.accounts:
            if not account.get('used_status', False):
                return account
        return None

    def mark_account_as_used(self, account):
        for acc in self.accounts:
            if acc['email'] == account['email']:
                acc['used_status'] = True
                break
        self.save_accounts()

    def save_accounts(self):
        with open(self.account_file, 'w') as file:
            json.dump(self.accounts, file)

    def reset_accounts(self):
        for account in self.accounts:
            account['used_status'] = False
        self.save_accounts()

# Example usage:
# account_manager = AccountManager()
# unused_account = account_manager.get_unused_account()
# if unused_account:
#     # Use the account for operations
#     account_manager.mark_account_as_used(unused_account)
# else:
#     print("No unused accounts available.")
```