

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import date, datetime,timedelta
from selenium.webdriver.edge.options import Options as EdgeOptions
import time
import csv
import os
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

def openMarketPlace(location):
    global driver
    edge_options = EdgeOptions()
    driver = webdriver.Edge(options=edge_options)
    driver.get(location)
    driver.maximize_window()


def getListings(location):
    count=1
    listing = ''
    data = []
    while(count <= 20):
        # print('/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div[' + str(count) + ']/div/div[4]')
        try:
            listing = WebelementByXpath('/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div[' + str(count) + ']/div/div[4]',SHORTEST_TIME_OUT).text
        except:
            count+=1
        else:
            print("ride on time")
            info = listing.splitlines()
            count+=1
            li = [info[len(info) - 1],info[1].replace('Verified',''),location]
            print(li)
            data.append(li)
            li = []
    return data
        
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
    
def writeToExcel(data, header=None):
    file_name = 'final.csv'
    file_exists = os.path.isfile(file_name)
    
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # If the file does not exist, write the header first (if provided)
        if not file_exists and header is not None:
            writer.writerow(header)
        
        # Write the data rows
        writer.writerows(data)
locations = [
             'vanier-north',
             'beacon-hill-south-cardinal-heights',
             'ledbury-heron-gate-ridgemont-elmwood',
             'alta-vista',
             'hunt-club-upper-blossom-park-timbermill',
             'south-keys-heron-gate-greenboro-west',
             'borden-farm-stewart-farm-parkwood-hills-fisher-glen',
             'crestview-meadowlands',
             'kanata',
             'braemar-park-bel-air-heights-copeland-park',
             'briar-green-leslie-park',
             'centretown',
             'west-centertown',
             'carlington',
             'laurentian',
             'civic-hospital-central-park',
             'woodroffe-lincoln-heights',
             'carlingwood-west-glabar-park-mckellar-heights',
             'whitehaven-queensway-terrace-north',
             'carson-grove-carson-meadows',
             'cummings',
             'rockcliffe-manor-park',
             'cityview-skyline-fisher-heights',
             'glebe-dows-lake',
             'emerald-woods-sawmill-creek'
             'hawthorne-meadows-sheffield-glen',
             'ottawa-south',
             'hunt-club-east-western-community',
             'iris',
             'westboro',
             'kanata-lakes-marchwood-lakeside-morgans-grant-kanata-north-business-park',
             'hunt-club-woods-quintarra-revelstoke',
             'lindenlea-new-edinburgh',
             'lowertown',
             'sandy-hill-ottawa-east',
             'crystal-bay-lakeview-park',
             'east-industrial',
             'elmvale-eastway-riverview-riverview-park-west',
             'rockcliffe-manor-park',
             'byward-market',
             'qualicum-redwood-park',
             'riverside-park',
             'playfair-park-lynda-park-guildwood-estates',
             'overbrook-mcarthur',
             'vanier-south',
             'trend-arlington'
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             ]
location = 'vanier-south'
openMarketPlace('https://rentals.ca/ottawa/' + location)
data = getListings(location)
writeToExcel(data)