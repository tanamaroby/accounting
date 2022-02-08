def get_account_type(account):
        assets = "Assets"
        liabilities = "Liabilities"
        equity = "Equity"

        output = None
        try :
            output = {
                "accounts receivable": assets,
                "cash": assets,
                "accounts payable": liabilities,
                "service expense": equity,
            }[account]
            return output
        except:
            print(f"Unknown account name: {account}")

def get_assets():
    return "Assets"

def get_liabilities():
    return "Liabilities"

def get_equity():
    return "Equity"
    

