import threading
import requests
from selenium import webdriver

blocks = {}

def check_transaction(wallet_id):
    driver = webdriver.Chrome("chromedriver")
    # telegram_url = "https://api.telegram.org/bot1789201219:AAHxw5XAE72jn-rE8XTNTxMnCajvPHce6Wk"
    telegram_url = "https://api.telegram.org/bot1786452705:AAEUo6Yc498YYffRT_v_Aw_81pAhTgtWDhA"
    driver.get("https://etherscan.io/address/" + wallet_id)

    matching_data = driver.find_elements_by_xpath("//div[@id='transactions']//table[@class='table table-hover']//tr/td[4]")

    for row in matching_data:
        print(int(row.text))
        block_number = int(row.text)
        if wallet_id not in blocks:
            print('Running very first time')
            blocks[wallet_id] = block_number
            text = "Running very first time for the wallet - https://etherscan.io/address/" + wallet_id
            # params = {'chat_id': '1608606859', 'text': text}
            params = {'chat_id': '1759522086', 'text': text}
            response = requests.post(telegram_url + '/sendMessage', data=params)
            print(response)
            break
        else:
            if block_number > blocks[wallet_id]:
                print('new transaction found + ' + row.text)
                text = "new transaction found " + row.text + " - https://etherscan.io/address/" + wallet_id
                # params = {'chat_id': '1608606859', 'text': text}
                params = {'chat_id': '1759522086', 'text': text}
                response = requests.post(telegram_url + '/sendMessage', data=params)
            else:
                break

    driver.close()

if __name__ == '__main__':
    while True:
        wallets = ['0xa28602f18eb877b0b929caaae94faed4ff402929', '0x3859c1df244953382aa124e87afe80f817299f0b']

        for wallet in wallets:
            check_transaction(wallet)

        # time.sleep(1)
