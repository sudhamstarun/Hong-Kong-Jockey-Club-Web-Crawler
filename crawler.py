#import libraries 
import urllib2
import string
import json
import itertools 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

#starting the webdriver
driver = webdriver.Firefox()
driver.get('http://www.hkjc.com/english/racing/SelectHorse.asp')
alphabets = string.ascii_uppercase

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


names = list() 
country_of_origin_age = list() 
colour_sex = list() 
import_type = list() 
season_stakes = list() 
total_stakes = list() 
no_of_123_starts = list() 
no_of_starts_in_past_races = list() 
trainer = list() 
owner = list() 
current_rating = list() 
start_of_season_rating = list() 
sire = list() 
dam = list() 
dam_sire = list() 

for i in alphabets: 
    #click on index
    driver.find_element_by_link_text(i).click()

    #find the size of the table and do the required operation
    row_count = len(driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/p/table/tbody/tr[2]/td/table/tbody/tr"))
    column_count = len(driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/p/table/tbody/tr[2]/td/table/tbody/tr[1]/td"))

    print(row_count)
    print(column_count)

    for j in range(1,row_count+1):
        for k in range(1,column_count+1): 
            if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/p/table/tbody/tr[2]/td/table/tbody/tr[%d]/td[%d]/table/tbody/tr/td[1]/li/a" %(j,k))):
                driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/p/table/tbody/tr[2]/td/table/tbody/tr[%d]/td[%d]/table/tbody/tr/td[1]/li/a" %(j,k)).click() 

                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[1]/table/tbody/tr/td/table/tbody/tr[1]/td/font")):
                    names.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[1]/table/tbody/tr/td/table/tbody/tr[1]/td/font").text)
                else:
                    names.append('')

                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/font")):
                    country_of_origin_age.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[2]/font").text)
                else:
                    country_of_origin_age.append('')
            
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/font")):
                    colour_sex.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/font").text)
                else:
                    colour_sex.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/font")):
                    import_type.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[2]/font").text)
                else:
                    import_type.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/font")):
                    season_stakes.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/font").text)
                else:
                    season_stakes.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[2]/font")):
                    total_stakes.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[2]/font").text)
                else:
                    total_stakes.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[6]/td[2]/font")):
                    no_of_123_starts.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[6]/td[2]/font").text)
                else:
                    no_of_123_starts.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td[2]/font")):
                    no_of_starts_in_past_races.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td[2]/font").text)
                else:
                    no_of_starts_in_past_races.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[4]/font/a")):
                    trainer.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[4]/font/a").text)
                elif(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[4]/font")):
                    trainer.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[4]/font").text)
                else:
                    trainer.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[4]/font/a")):
                    owner.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[4]/font/a").text)
                elif(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[4]/font")):
                    owner.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[4]/font").text)
                else:    
                    owner.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[4]/font")):
                    current_rating.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[4]/font").text)
                else:
                    current_rating.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[4]/font")):
                    start_of_season_rating.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[4]/font").text)
                else:
                    current_rating.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[4]/font/a")):
                    sire.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[4]/font/a").text)
                elif(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[4]/font")):
                    sire.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[5]/td[4]/font").text)
                else:
                    sire.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[6]/td[4]/font/a")):
                    dam.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[6]/td[4]/font/a").text)
                elif(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[6]/td[4]/font")):
                    dam.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[6]/td[4]/font").text)
                else:
                    dam.append('')
                
                if(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td[4]/font/a")):
                    dam_sire.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td[4]/font/a").text)
                elif(check_exists_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td[4]/font")):
                    dam_sire.append(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td[4]/font").text)
                else:
                    dam_sire.append('')
                
                driver.back()                            
            else:
                break

    driver.back()

#writing all the lists to json file

#output_data = dict(zip(names, zip(country_of_origin_age, zip(colour_sex, zip(import_type, zip(season_stakes, zip(total_stakes, zip(no_of_123_starts, zip(no_of_starts_in_past_races, zip(trainer, zip(owner, zip(current_rating, zip(start_of_season_rating, zip(sire, zip(dam, dam_sire)))))))))))))))
data = [{'Name': a, 'Country of Origin & Age': b, 'Colour & Sex': c, 'Import Type': d, 'Season Stakes': e, 'Total Stakes': f, 'Number Of 123 Starts': g, 'Number of Starts In Past Races': h, 'Trainer': i, 'Owner': j, 'Current Rating': k, 'Start Of Season Rating': l, 'Sire': m, 'Dam': n, 'Dam Sire': o } for a, b, c, d, e, f, g, h, i, j, k, l, m, n, o in itertools.izip(names, country_of_origin_age, colour_sex,import_type, season_stakes, total_stakes, no_of_starts_in_past_races, no_of_starts_in_past_races, trainer, owner, current_rating, start_of_season_rating, sire, dam, dam_sire)]


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
