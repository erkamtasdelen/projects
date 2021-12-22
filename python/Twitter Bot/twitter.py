from selenium import webdriver
import requests as r
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from urllib.parse import unquote
import random


class twitter:
    def __init__(self,username,password):
        self.tarayici = webdriver.Chrome(executable_path='chromedriver.exe')
        self.loginsucsses = False

        self.username = username
        self.password = password

        self.xpathforhome = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div[2]/div/a/div[4]/div"



    def write(self,text):
        text += "\n- Takibe Takip -"
        try:
            self.tarayici.get("https://twitter.com/compose/tweet")
            self.waitload(
                "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div")
            try:
                self.tarayici.find_element(By.XPATH,
                                           "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div").send_keys(
                    random.choice(texts))
            except:
                self.tarayici.find_element(By.XPATH,
                                           "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div").send_keys(
                    text)

            sendtweet = self.tarayici.find_element(By.XPATH,
                                                   "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]")
            self.tarayici.execute_script("arguments[0].click();", sendtweet)

            try:
                time.sleep(1)
                self.tarayici.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div")
            except:
                time.sleep(25)
        except:
            pass

    def waitload(self,xpath,msg=""):
        while True:
            try:
                self.tarayici.find_element(By.XPATH,xpath)
                print("Loaded ",msg)
                break
            except:
                pass

    def login(self):

        self.tarayici.get("https://twitter.com/login?lang=en")
        self.waitload(
            "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        self.tarayici.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').send_keys(self.username)
        self.tarayici.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span").click()

        self.waitload('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.tarayici.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(self.password)
        self.tarayici.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div").click()

        self.waitload(self.xpathforhome)
        self.loginsucsses = True
        print("Successful Login")


    def writetopics(self,times=99999):
        if self.loginsucsses :
            for trycaount in range(0,times):
                try:
                    cohice = random.choice(self.topics)
                    self.topics.remove(cohice)
                    self.tarayici.get(cohice)
                    key = unquote(self.tarayici.current_url)[29:].replace('"',"").replace("+"," ")

                    print(key)
                    self.waitload("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]","Feed")
                    html = self.tarayici.page_source
                    texts = []
                    errorcount = 0
                    while True:
                        soup = BeautifulSoup(html, "lxml").find_all("div", lang=True)

                        for text in soup:
                            if key in text.getText():
                                try:
                                    animals.index('dog')
                                except:
                                    texts.append(text.getText().replace("\n"," "))
                                    pass
                        print(len(texts))
                        errorcount+=1
                        if len(texts) <= 35 :
                            self.tarayici.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                            time.sleep(3)
                            html = self.tarayici.page_source
                            if errorcount >= 10:
                                break
                        else:
                            break
                    print(texts)
                    for onetext in texts:
                        self.write(onetext)


                    print("TWİT COUNT : ",trycaount)
                except:
                    print("EROR ABOUT TWİT : ",trycaount)

        else:
            print("Please Login First !")

    def gettopics(self,ilkkac=""):

        self.tarayici.get("https://trends24.in/turkey/")
        self.waitload("/html/body/div[2]/div[3]/div/div[1]")
        html = self.tarayici.page_source
        soup = BeautifulSoup(html,"lxml")
        links = soup.find_all("a",href=True)
        self.topics = []
        for i in links:
            if "search" in i['href']:
                try:
                    self.topics.index(i['href'])
                except:
                    self.topics.append(i['href'])

        if ilkkac != "":
            print("hi")
            self.topics = self.topics[:ilkkac]
        print("Ready Topics We Have : ", len(self.topics))


    def fallowusers(self,username,howmuch):
        self.tarayici.get("https://twitter.com/{}/following".format(username))
        self.waitload("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div","Fallowing Page")
        currentfallow = 0
        currentorder = 1
        while True:
            global fallowbutton
            try:
                fallowbutton = self.tarayici.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[{}]/div/div/div/div[2]/div[1]/div[2]/div".format(currentorder))
                self.waitload("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[{}]/div/div/div/div[2]/div[1]/div[2]/div".format(currentorder))
            except:
                self.tarayici.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.waitload(
                "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[{}]/div/div/div/div[2]/div[1]/div[2]/div".format(
                    currentorder))
            fallowbutton = self.tarayici.find_element(By.XPATH,
                                                      "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[{}]/div/div/div/div[2]/div[1]/div[2]/div".format(
                                                          currentorder))
            currentorder +=1
            print(fallowbutton.text ,currentorder)
            if fallowbutton.text == "Following" or fallowbutton.text == "Pending":
                print("Already Fallowing")
            else:
                self.tarayici.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                print("Falow request : ", currentorder)
                time.sleep(2)
                currentfallow +=1
                try:
                    fallowbutton.click()
                    if currentfallow >= howmuch :
                        break
                except:
                    print("We have eror on click")

        print("Over fallowing")





        #/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div
        #/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/div
        #/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[3]/div/div/div/div[2]/div[1]/div[2]/div
        #/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div[27]/div/div/div/div[2]/div[1]/div[2]/div









ilkhesap = twitter("CanavarGundem","pas78k78")
ilkhesap.login()
ilkhesap.gettopics(10)
ilkhesap.writetopics()