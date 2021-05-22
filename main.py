import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import os
from kivy.properties import StringProperty
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import sublist3r
import time
import re
import socket


class Test(TabbedPanel):
    ip = ObjectProperty(None)
    data_output = ObjectProperty(None)
    subdomain = ObjectProperty(None)
    subdomain_output = ObjectProperty(None)
    page_text = ObjectProperty(None)
    domain = ObjectProperty(None)
    in_title = ObjectProperty(None)
    file_type = ObjectProperty(None)
    in_body = ObjectProperty(None)
    in_url = ObjectProperty(None)
    query_output = ObjectProperty(None)
    search_iot = ObjectProperty(None)
    details_iot = ObjectProperty(None)
    open_ports = ObjectProperty(None)
    vulnerabilities = ObjectProperty(None)
    meta_data = ObjectProperty(None)
    emails_found = ObjectProperty(None)
    search_emails = ObjectProperty(None)
    employees_found = ObjectProperty(None)
    wmg_image = StringProperty(None)


    intro_data = """This is an OSINT toolset which contains a variety of tools designed for beginners who 
    just get started with OSINT and they might find it difficult to use the original tools which run on the terminal and they might be a bit confused at first, if they have never used a terminal before. \n
    The users are strongly advised to first use the Help page which will provided them with more details about the interface and about the tools.  
    """
    help_data = """This page provides you with information and some extra details about how to use this software.
    On each page there is a button called “Extra Info” and if you press it this will display extra information about the used feature.
    For example, on the “IP Addresses” page you can find extra details about the operations that works behind the feature.\n
    If you are new to OSINT you can use this software for getting a better understanding of some tools which can help you with your investigation in a more friendly way than just using the terminal.
    Once you have a basic understanding of the tools presented here, you can move on and use the full capabilities of the tools on the terminal.\n
    ***All the backend tools are used in a passive way so not damage/harm will be done to the domain that you are searching for as well as not revealing details about yourself.***
    """

    ip_addresses_data = """There are 2 features presented on this page, they can be used for identifying information about the domain that you want to investigate.
    The first one is used for identifying the IP address of a domain.
    The second one is used for identifying other subdomains related to your main domain.
    The information provided by these two tools can help you later with your research and give you new options to investigate. \n
    Please wait while the data is gathered and displayed back to you.
    Thank you
    """
    metadata_extraction_data = """Often files, especially images hide information about that file which can be useful when conducting an investigation, such as where the picture was taken, what device was to take the image or any comments 
    added to the file. \n
    This could help you when trying to find what other information the file can give you other than the actual data presented and it might lead your investigation to a different direction.
    """
    google_dorks_data = """This feature will allow you to create advanced search engine queries which will optimise your results when searching for a piece of information online.\n
    For example, if you are looking for a specific information or you are looking only for websites that have a specific word displayed, using advance search queries will only give you the results that you are looking after.
    """
    google_dorks_info = """
        Page Text -> Search for a specific data in the page
        Domain -> the name of the domain that you want to search
        Title -> search for a particular result that has your word in title
        File type -> display results which are in a file type format (e.g. .pdf, .csv)
        Body -> display results which have that word in their body
        URL -> display only the URLs that have that word in their URLs
        """
    iot_devices_data = """If you are investigating an IoT device and it is connected to the internet and you know its IP address, this 
    feature will allow you to identify basic details about it, such as where it is located, open ports and possible 
    vulnerabilities which can be exploited.\n
    Please wait for the program to display back your results.
    Thank you!
    """
    email_addresses_data = """During the OSINT investigation you might need to identify a list of possible email addresses which are related to the company you are investigating,
    this would be helpful for identifying possible people who are connected to the company and you can use this information for identifying further information. \n
    The tool behind this is called theHarvesters which is set to run in a passive way without interfering with the actual company that you are investigating.
    """
    employees_found_data = """Searching a list of possible employees related to a company could be helpful for identifying possible names which you can use later for trying to find extra information about the company that you are investigating.
    Once you have a possible list of names, you can do further analysis, by searching them on social media platforms and see what extra information you can find about them.
    """
    options = Options()
    options.headless = True
    # path to the Chrome Driver
    driver = webdriver.Chrome(r"/home/vanvu/Desktop/kivy/chromedriver", chrome_options=options)

    def ip_addresses(self):

        if self.ip.text == "":
            popup = Popup(title="WARNING !!!", content=Label(text="No data was introduced in the search field.\n\n"
                                            "Please add the name of a domain for identfying the needed information.",
                                            font_size = '20', markup = True, halign = 'center' ),
                                            auto_dismiss=True, size_hint=(0.4, 0.4))
            popup.open()

        else:
            self.data_output.text = str(os.system("nslookup " + str(self.ip.text) + "> domain_name.txt"))
            # used to delete the extra spaces from the file
            os.system("awk '{$2=$2};1' domain_name.txt > new_output_domain.txt")
            os.system("rm domain_name.txt")
            with open("new_output_domain.txt") as f:
                content = f.read()
                print(content)
                self.data_output.text = content
            f.close()

    def subdomains(self):

        print("test")
        if self.subdomain.text == "":
            popup = Popup(title="WARNING !!!", content=Label(text="No data was introduced in the search field.\n\n"
                                            "Please add the name of a domain for identfying the other subdomains.",
                                            font_size = '20', markup = True, halign = 'center' ),
                                            auto_dismiss=True, size_hint=(0.4, 0.4))
            popup.open()
        else:

            subdomains = sublist3r.main(str(self.subdomain.text), 10, "subdomains.txt", ports= None, silent=True, verbose=False,
                                           enable_bruteforce=False,engines=None)

            with open("subdomains.txt") as f:
                for line in f:
                    print(("".join(line.strip(str(f)))))
            f.close()

        # reducing the number for found subdomains because too many would turn the label black (why?)
            os.system('echo "$(tail -500 subdomains.txt)" > subdomains.txt')

        # Command used for doing sub_domain ennumaration of a main doamin
            with open("subdomains.txt") as f:
                facebook = f.read()
                self.subdomain_output.text = facebook
            f.close()


    def selected(self, file_name):
        # Layout of how this works
        # 1 - Use 1st button to load the path to the file
        # 2 - Display the path inside the label
        # 3 - Use the 2nd button to give the path to "exiftool" for extracting the data
        # 4 - Save the data to a file
        # 5 - Display the data on the interface.
        # Active the file-chooser widget when the "Load" button is pressed

        # add an image so it is already there for not having that small white squer

        self.ids.my_image.source = file_name[0]
        print(file_name[0])
        self.my_file.text = os.system("exiftool " + file_name[0] + "> metadata.txt")
        os.system("awk '{$2=$2};1' metadata.txt > metadata2.txt")
        os.system("rm metadata.txt")
        print(self.my_file.text)
        #with open("metadata.txt") as f:
           # meta = f.read()
            #self.meta_data.text = meta

        with open("metadata2.txt") as f:
            meta = f.read()
            print(meta)
            self.meta_data.text = meta
        f.close()

    def google_dorks(self):

        page_text = ""
        domain_text = ""
        in_title_text = ""
        file_type = ""
        in_body_text = ""
        in_url_text = ""
        #print(self.page_text.text)


        if self.page_text.text == "" and self.domain.text == "" and self.in_title.text == "" and\
                self.file_type.text == "" and self.in_body.text == "" and self.in_url.text == "":
            popup = Popup(title="WARNING !!!", content=Label(text="No data was introduced in the search fields.\n\n"
                                            "Please populate the fields for creating a query",
                                            font_size = '20', markup = True, halign = 'center' ),
                                            auto_dismiss=True, size_hint=(0.4, 0.4))
            popup.open()
        if self.page_text.text != "":
            page_text = "\"{}\"" .format(self.page_text.text)
        if self.domain.text != "":
            domain_text = " site: {}" .format(self.domain.text)
        if self.in_title.text != "":
            in_title_text = " intitle: \"{}\"" .format(self.in_title.text)
        if self.file_type.text != "":
            file_type = " filetype: {}" .format(self.file_type.text)
        if self.in_body.text != "":
            in_body_text = " inbody: \"{}\"" .format(self.in_body.text)
        if self.in_url.text != "":
            in_url_text = " inurl: \"{}\"" .format(self.in_url.text)
        query = page_text + domain_text + in_title_text + file_type + in_body_text + in_url_text
        #print(query)
        self.query_output.text = query
    def clear_google_dorks(self):
        self.page_text.text = ""
        self.domain.text = ""
        self.in_title.text = ""
        self.in_body.text = ""
        self.file_type.text = ""
        self.in_url.text = ""
        self.query_output.text = ""

    def iot_devices(self):

        #https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        #print(re.search(regex, self.search_iot.text))

        if self.search_iot.text == "" or re.search(regex, self.search_iot.text) == None:
            popup = Popup(title="WARNING !!!", content=Label(text="No data was introduced in the search field.\n\n"
                                              "Please make sure that the IP address exists and it is typed correctly",
                                             font_size = '20', markup = True, halign = 'center' ),
                                            auto_dismiss=True, size_hint=(0.4, 0.4))
            popup.open()
        else:
            # access the website
            Test.driver.get("https://www.shodan.io/")
            # log in into the account
            log_in = Test.driver.find_element_by_xpath('/html/body/div[2]/div/div/ul[2]/li[2]/a')
            log_in.click()
            username = 'Florin991'
            password = 'Plmplmplm1'
            log_in = Test.driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/div[1]/form/div[1]/input')
            log_in.send_keys(username)
            log_in = Test.driver.find_element_by_xpath('//*[@id="password"]')
            log_in.send_keys(password)
            log_in = Test.driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/div[1]/form/div[3]/input')
            log_in.click()

            # find the search bar
            iot_devices = Test.driver.find_element_by_xpath('//*[@id="search_input"]')
            # iot_ip = "117.50.14.196"

            # send the ip address to the website
            # time.sleep(10)
            # if self.search_iot.text !=
            iot_devices.send_keys(str(self.search_iot.text))

            # find and click the search button
            iot_devices = Test.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/button')
            iot_devices.click()
            # print("Details about the IoT Device")

            file1_iot = open('details_iot.txt', 'w')
            for i in range(1, 7):
                iot_devices = Test.driver.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[1]/table/tbody/tr' + "[" + str(i) + "]").text
                file1_iot.writelines(iot_devices + "\n")
                # print(iot_devices)
            file1_iot.close()
            # print("")
            with open("details_iot.txt", "r") as file1_iot:
                content = file1_iot.read()
                self.details_iot.text = content

            # Printing open ports
            file2_iot = open('open_ports_iot.txt', 'w')
            iot_devices = Test.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[1]/h2').text
            # print("Open " + iot_devices)

            iot_devices = Test.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/ul[1]').text
            file2_iot.writelines(iot_devices + '\n')
            file2_iot.close()
            with open('open_ports_iot.txt', 'r') as file2_iot:
                content = file2_iot.read()
                self.open_ports.text = content
            # print(iot_devices)

            file3_iot = open('vulnerabilities_iot.txt', "w")
            # Printing the possible vulnerabilities that the IoT might have
            # print("Possible vulnerabilities")
            # try to find a way of changing the range depending on how many numbers they have

            #for i in range(1, 25):
             #   if NoSuchElementException:
              #      break
               # else:
                #    iot_devices = Test.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[3]/table/tbody/tr' + "[" + str(i) + "]").text
                 #   file3_iot.writelines(iot_devices + "\n")
                # print(iot_devices)
                  #  print("")

            for i in range(1, 10):
                iot_devices = Test.driver.find_element_by_xpath(
                    '/html/body/div[3]/div/div[2]/div/div[1]/div[3]/table/tbody/tr' + "[" + str(i) + "]").text
                file3_iot.writelines(iot_devices + "\n")
                # print(iot_devices)
            print("")
            file3_iot.close()
            # keeping only the name of the vulnerabilities from the data provided by the website
            # print("test")
            with open("vulnerabilities_iot.txt", "r") as f:
                wordlist = [line.split(None, 1)[0] for line in f]
            #  print(wordlist)
            f.close()
            # over writing the data from the first file and
            with open("vulnerabilities_iot.txt", "w") as f_new:
                for i in range(1, 10):
                    f_new.write(wordlist[i] + "\n")
            f_new.close()

            with open("vulnerabilities_iot.txt", "r") as file3_iot:
                content = file3_iot.read()
                self.vulnerabilities.text = content





    #print(wordlist[i])

            #self.vulnerabilities.text = wordlist[i]
        #for i in range(11):
          #  print(wordlist[i])
        #print(driver.title)
        #print(driver.current_url)
        #time.sleep(10)
        #print(iot_devices.get_attribute('/html/body/div[3]/div/div[2]/div/div[2]/ul[1]'))

    def email_addresses(self):

        options = Options()
        options.headless = True

        # path to the Chrome Driver
        Test.driver = webdriver.Chrome(r"/home/vanvu/Desktop/kivy/chromedriver")
        # access the website

        os.chdir("theHarvester")
        os.system("pwd")
        os.system("python3 theHarvester.py -d " + self.search_emails.text + " -b google -f /home/vanvu/Desktop/kivy/new_data")
        os.system("cd ..")

        Test.driver.get("file:///home/vanvu/Desktop/kivy/new_data.html")

        asc = Test.driver.find_element_by_xpath('//*[@id="example-table"]/div[1]/div[1]/div[4]/div[1]/div[3]/input')

        asc.send_keys("email")
        asc.click()
        time.sleep(5)
        #print(driver.find_element_by_xpath('//*[@id="example-table"]/div[2]/div/div[1]/div[4]').text)
       # print(driver.find_element_by_xpath('//*[@id="example-table"]/div[2]/div/div[1]/div[5]').text)

        # it could be a good idea to remove the .html files after finishing the process

        # the program will only identify the first 500 emails and users if the index number it is not found in on the website, the loop will exit
        with open("email_addresses.txt", "w") as emails:
            for x in range(1,500):
                print(x)
                try:
                    if Test.driver.find_element_by_xpath('//*[@id="example-table"]/div[2]/div/div[' + str(x) + "]/div[4]").text == "email":
                        data = Test.driver.find_element_by_xpath('//*[@id="example-table"]/div[2]/div/div[' + str(x) + ']/div[5]').text
                        emails.writelines(data + "\n")
                    else:
                        print("fail")
                except NoSuchElementException:
                    break
            emails.close()

        with open("email_addresses.txt") as f:
            data = f.read()
            self.emails_found.text = data
        f.close()

    def employees_list(self):
        print("test")
        #options = Options()
        #options.headless = True

        # path to the Chrome Driver
        #driver = webdriver.Chrome(r"/home/vanvu/Desktop/kivy/chromedriver")
        # access the website

        #os.chdir("theHarvester")
       # os.system("pwd")
        #os.system("python3 theHarvester.py -d warwick.ac.uk -b google -f /home/vanvu/Desktop/kivy/users")

        #Test.driver.get("file:///home/vanvu/Desktop/kivy/users.html")
        #asc = Test.driver.find_element_by_xpath('//*[@id="example-table"]/div[1]/div[1]/div[4]/div[1]/div[3]/input')
        #asc.send_keys("people")
        #asc.click()
       # time.sleep(5)

        # Change the names in here + add the slide bar
        #with open("employees_list.txt", "w") as employees:
            #for x in range(1,500):
            #print(x)
                #try:
                   # if Test.driver.find_element_by_xpath('//*[@id="example-table"]/div[2]/div/div[' + str(x) + "]/div[4]").text == "people":
                       # data = Test.driver.find_element_by_xpath('//*[@id="example-table"]/div[2]/div/div[' + str(x) + ']/div[5]').text
                      #  employees.writelines(data + "\n")
                   # else:
                       # print("fail")
                #except NoSuchElementException:
                    #break
           # employees.close()

        with open("employees_list.txt") as f:
            data = f.read()
            self.employees_found.text = data
        f.close()


            #return True


       # with open("domain_name.txt") as f:
           # content = f.read()
            #self.data_output.text = content

        #email_address = driver.find_element_by_xpath('//*[@id="example-table"]/div[2]/div/div[29]/div[5]').text
        #print(email_address)
        #// *[ @ id = "example-table"] / div[2] / div / div[27] / div[5] / text()




class MyApp(App):
    def build(self):
        return Test()

if __name__ == "__main__":
    MyApp().run()