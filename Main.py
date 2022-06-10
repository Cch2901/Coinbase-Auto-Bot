from os import close
from selenium import webdriver
import time
web = webdriver.Chrome()
web.get('https://www.coinbase.com/login')
time.sleep(2)
from Setup import *

# NAVIGATION MENU v ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Login form auto complete
username = web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/form/div[2]/div/div/span/input') ;
username.send_keys(Username)
Continue = web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/form/div[5]/ul/li[1]/button');
Continue.click();
time.sleep(2);
RemoveDismissMsg = web.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/button');
RemoveDismissMsg.click();
password = web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div[1]/form/div[4]/div/div/div/span/input');
password.send_keys(Password)
time.sleep(2);
Login = web.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div[1]/form/div[8]/button');
Login.click();
    

#Wait for 2FA Code
time.sleep(60)
# Logged - Navigate
AcceptCookies = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/button[2]')
AcceptCookies.click()
TradeTab = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[1]/div/nav/div/nav/div[2]/a[3]/div/div/button')
TradeTab.click()
time.sleep(5)
#Currency Selector
ALL = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]')
GBP = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[6]/span')
USD = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[4]')
EUR = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]')
if (Currency == 'GBP'):
    GBP.click();
elif (Currency == 'USD'):
    USD.click();
elif (Currency == 'EUR'):
    EUR.click();
elif (Currency == 'ALL'):
    ALL.click();
time.sleep(5)
#Trading Pair Selector - Use href= element for it to work
BTCGBP = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/a[1]')
ETHGBP = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/a[2]')
ADAGBP = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/a[3]')
SOLGBP = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/a[4]')
USDCGBP = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/a[5]')
if (TradingPair == 'GBPBTC'):
  BTCGBP.click();
elif (Currency == 'GBPETH'):
    ETHGBP.click();
elif (Currency == 'GBPADA'):
    ADAGBP.click();
elif (Currency == 'GBPSOL'):
    SOLGBP.click()
elif (Currency == 'GBPUSDC'):
    USDCGBP.click()
#elif (Currency == ''):
time.sleep(5)
#Main Content Page
SkipMsg = web.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/div/div[3]/button[1]')
SkipMsg.click()
time.sleep(10)
# NAVIGATION MENU ^ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DATA CONTENT v ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Market Data for price & 1 day percentage indicator
Price = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/nav[1]/div[1]/h1/div/div[2]/div[1]/div/span[1]').text
Change = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/nav[1]/div[1]/h1/div/div[2]/div[1]/div/span[2]').text
#Type of order
Limit = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/button[1]/div/span')
Market = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/button[2]/div/span')
StopLimit = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/button[3]/div/span')
BuyTab = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/span')
SellTab = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]/span')
BuyBelow1 = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/span') #selects -1%
SellAbove1 = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[3]/span') # selects +1%
FiatBalance = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[3]/p').text #Get's the Fiat Balance
CryptoBalance = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[1]/p').text #Get's the Crypto Balance
FiatAmountInput = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div/input')
CryptoAmountInput = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div/div/input')
Fee = web.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div/span').text
BuyBtn = web.find_element_by_xpath('')
SellBtn = web.find_element_by_xpath('')
# DATA CONTENT ^ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SCRIPTS v -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if (ImmediateTrade == 'Disable'):
    webdriver.Chrome(close);

if (OrderType == 'Limit'):
     Limit.click();
elif (OrderType == 'Market'):
     Market.click();
elif (OrderType == 'StopLimit'):
     StopLimit.click();


if (Change < '0.00'):
    BuyTab.click(); # Clicks Buy Tab to start a buy order
    BuyBelow1.click(); #Buys below 1%
    FiatAmountInput.click();
    FiatAmountInput.send_keys(FiatBalance) #fills out the form to input amount to buy in fiat
    BuyBtn.click(); #
    print(Price);
    print('Fee=', Fee)
    print('Bought@', Price + Fee + '1.00%');

elif (Change > '0.00'):
    SellTab.click(); # Clicks Buy Tab to start a buy order
    SellAbove1.click(); #Buys below 1%
    CryptoAmountInput.click();
    CryptoAmountInput.send_keys(FiatBalance); #fills out the form to input amount to buy in fiat
    SellBtn.click() #
    print(Price);
    print('Fee=', Fee);
    print('Sold@', Price - Fee + '1.00%');