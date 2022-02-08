def get_account_type(account):
        assets = "Assets"
        liabilities = "Liabilities"
        equity = "Equity"

        return {
            "accounts receivable": assets,
            "cash": assets,
            "accounts payable": liabilities,
            "service expense": equity,
        }[account]

def get_assets():
    return "Assets"

def get_liabilities():
    return "Liabilities"

def get_equity():
    return "Equity"
    

