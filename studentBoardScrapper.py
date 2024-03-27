

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import date, datetime,timedelta
from selenium.webdriver.edge.options import Options as EdgeOptions
import time
import csv

#timeouts for different scenerieos 
LONG_TIME_OUT = 2000
MEDIUM_TIME_OUT = 50
SHORT_TIME_OUT = 20
SHORTEST_TIME_OUT = 2
#driver
driver = webdriver




def terminateProgram():

    driver.close()
    driver.quit()

def openBoard():

    global driver
    edge_options = EdgeOptions()


    driver = webdriver.Edge(options=edge_options)
    driver.get('https://web5.uottawa.ca/rezweb/search.php')
    driver.maximize_window()




        
def WebelementByXpath(xPath, timeout):
    '''finds an element by xpath specify the element first then the timeout'''
    try:
        element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH,xPath))
    )
    except TimeoutException or NoSuchElementException:
        raise Exception
    else:
        elem = driver.find_element(By.XPATH,xPath)
        return elem

def WebelementSearch(elem, timeout,option):
    '''find an element through either tag or class, specify the element then timeout then whether its by tag or class'''
    global driver
    if option.__eq__('tag'):
        optionReal = By.TAG_NAME
    elif option.__eq__('class'):
        optionReal = By.CLASS_NAME
    elif option.__eq__('id'):
        optionReal = By.ID
    try:
        element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((optionReal,elem))
    )
    
    except:
        try:
            element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((optionReal,elem))
        )
        except:
            raise Exception
    finally:
        return driver.find_elements(optionReal,elem)



def openOffCampus():
    location = WebelementByXpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/form/p[1]/select',LONG_TIME_OUT)
    offCampus = WebelementByXpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/form/p[1]/select/option[1]',LONG_TIME_OUT)
    submit = WebelementByXpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/form/input[1]',LONG_TIME_OUT)
    location.click()
    offCampus.click()
    submit.click()

    
def openOnCampus():
    location = WebelementByXpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/form/p[1]/select',LONG_TIME_OUT)
    offCampus = WebelementByXpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/form/p[1]/select/option[2]',LONG_TIME_OUT)
    submit = WebelementByXpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[1]/form/input[1]',LONG_TIME_OUT)
    location.click()
    offCampus.click()
    submit.click()


def getAptInfo():
    aptInfo = []
    temp = []
    table = WebelementByXpath('/html/body/table/tbody/tr[2]/td/table',LONG_TIME_OUT)
    print("CLEAR")
    for row in table.find_elements(By.XPATH,".//tr"""):
        aptInfo.append(temp)
        temp = []
        for cell in row.find_elements(By.XPATH,".//td"""):
            temp.append(cell.text)
    print(aptInfo)
    aptInfo.pop(0)
    return aptInfo
    
def writeToExcel(data,mode):
    if(mode.__eq__("on campus")):
        file_name = "aptinfoOn.csv"
    elif(mode.__eq__("off campus")):
        file_name = "aptinfoOff.csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        
openBoard()
openOffCampus()
# openOnCampus()
time.sleep(1)
data = getAptInfo()
writeToExcel(data,"off campus")