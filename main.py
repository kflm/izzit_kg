from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from selenium import webdriver
from selenium.webdriver.common.by import By
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Builder.load_file("bu.kv")

def nsm(a, b, c, d):
    prb = (a*d/100)*b*c/10000
    return prb
def scrap(lig):
    txt = open("sonuc.txt", "w")
    pth = "C:\Program Files (x86)\chromedriver.exe"
#!!!!path of chrome driver
    driver = webdriver.Chrome(pth)

    driver.get(lig)
    lst1 = driver.find_elements(By.XPATH, '//*[@id="matches-list"]/div[8]/div/div/div/div/div/ul')
    hlnk, alnk = [], []
    hi, ai = [], []
    for i in range(1, 1 + len(lst1)):
        ltf1 = '//*[@id="matches-list"]/div[@class="full-matches-table mt1e "]/div/div/div/div/div/ul[{}]/li[2]/a[1]'.format(i)
        ltf2 = '//*[@id="matches-list"]/div[@class="full-matches-table mt1e "]/div/div/div/div/div/ul[{}]/li[2]/a[3]'.format(i)
        ltf3 = "//*[@id='matches-list']/div[@class='full-matches-table mt1e ']/div/div/div/div/div/ul[{}]/li[1]/div/span[2]".format(i)
        ltf4 = '//*[@id="matches-list"]/div[@class="full-matches-table mt1e "]/div/div/div/div/div/ul[{}]/li[2]/a[1]/div/span'.format(i)
        ltf5 = '//*[@id="matches-list"]/div[@class="full-matches-table mt1e "]/div/div/div/div/div/ul[{}]/li[2]/a[3]/span'.format(i)
        iia = driver.find_element(By.XPATH, ltf3).get_attribute("data-match-status")
        if iia == "incomplete":
            lnkh = driver.find_element(By.XPATH, ltf1).get_attribute('href')
            lnka = driver.find_element(By.XPATH, ltf2).get_attribute('href')
            sk1 = driver.find_element(By.XPATH, ltf4).text
            sk2 = driver.find_element(By.XPATH, ltf5).text
            hi.append(sk1)
            ai.append(sk2)
            hlnk.append(lnkh)
            alnk.append(lnka)
        else:
            continue
    ct = 0
    for home in hlnk:
        away = alnk[ct]
        driver.get(home)
        fnd1 = driver.find_element(By.XPATH, '//*[@id="overview-0"]/table/tbody/tr[9]/td[3]')
        fnd2 = driver.find_element(By.XPATH, '//*[@id="overview-0"]/table/tbody/tr[10]/td[3]')
        hd = 100 - int(str(fnd1.text)[:-1])
        hs = 100 - int(str(fnd2.text)[:-1])
        driver.get(away)
        fnd3 = driver.find_element(By.XPATH, '//*[@id="overview-0"]/table/tbody/tr[9]/td[4]')
        fnd4 = driver.find_element(By.XPATH, '//*[@id="overview-0"]/table/tbody/tr[10]/td[4]')
        ad = 100 - int(str(fnd3.text)[:-1])
        ass = 100 - int(str(fnd4.text)[:-1])
        bts = str(float(100- nsm(hd, hs, ad, ass)))
        txt.write("maç: " + hi[ct] + " vs " + ai[ct] + "\n")
        txt.write("both to not score: %" + bts + "\n")
        txt.write("**********************" + "\n")
        ct += 1
    driver.close()

#norveç 1 https://footystats.org/norway/first-division/fixtures
#isvec super https://footystats.org/sweden/superettan/fixtures
#bra seri a https://footystats.org/brazil/serie-a/fixtures
#bra seri b https://footystats.org/brazil/serie-b/fixtures
#kore 1 https://footystats.org/south-korea/k-league-1/fixtures
#kore 2 https://footystats.org/south-korea/k-league-2/fixtures
#arjantin premier https://footystats.org/argentina/primera-division/fixtures
#abd major https://footystats.org/usa/mls/fixtures




class MyLayout(Widget):
    def stb(self):
        if self.ids.sbx.text== "jp1":
            scrap("https://footystats.org/japan/j1-league/fixtures")
        elif self.ids.sbx.text=="jp2":
            scrap("https://footystats.org/japan/j2-league/fixtures")
        elif self.ids.sbx.text=="jp3":
            scrap("https://footystats.org/japan/j3-league/fixtures")


        elif self.ids.sbx.text=="bra a":
            scrap("https://footystats.org/brazil/serie-a/fixtures")
        elif self.ids.sbx.text=="bra b":
            scrap("https://footystats.org/brazil/serie-b/fixtures")
        elif self.ids.sbx.text=="k1":
            scrap("https://footystats.org/south-korea/k-league-1/fixtures")
        elif self.ids.sbx.text=="k2":
            scrap("https://footystats.org/south-korea/k-league-2/fixtures")
        elif self.ids.sbx.text=="abd msl":
            scrap("https://footystats.org/usa/mls/fixtures")
        elif self.ids.sbx.text=="norvec 1":
            scrap("https://footystats.org/norway/first-division/fixtures")
        elif self.ids.sbx.text=="isvec s":
            scrap("https://footystats.org/sweden/superettan/fixtures")
        elif self.ids.sbx.text=="arj pre":
            scrap("https://footystats.org/argentina/primera-division/fixtures")
        
class baap(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    baap().run()
