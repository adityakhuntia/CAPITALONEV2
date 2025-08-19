import requests

def get_live_price(state_name, from_date=None, to_date=None):
    today_str = datetime.today().strftime("%Y-%m-%d")
    from_date = from_date or today_str
    to_date = to_date or today_str
    url = "https://enam.gov.in/web/Liveprice_ctrl/trade_data_list"
    
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://enam.gov.in",
        "Referer": "https://enam.gov.in/web/dashboard/live_price",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15",
        "X-Requested-With": "XMLHttpRequest",
        "Cache-Control": "no-cache",
    }

    data = {
        "language": "en",
        "stateName": state_name.strip().upper(),  # ensure correct formatting
        "fromDate": from_date,
        "toDate": to_date
    }

    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Request failed with status {response.status_code}")

# Example usage:
#uttrakhand_data = get_live_price("WEST BENGAL")
#print(uttrakhand_data)
