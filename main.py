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



class MyApp(App):
    def build(self):
        return Test()

if __name__ == "__main__":
    MyApp().run()
