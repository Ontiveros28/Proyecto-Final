import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def HOT100():
    driver = ChromeDriverManager().install()
    service = Service(driver)
    options = Options()
    options.add_argument("--window-size=1020,1200")
    navegador = webdriver.Chrome(service=service, options=options)

    navegador.get("https://www.billboard.com/charts/hot-100/")
    time.sleep(5)

    # Extract the page content using BeautifulSoup
    soup = BeautifulSoup(navegador.page_source, "html.parser")
    navegador.quit()

    filename = "datasets/hot100.csv"
    os.makedirs("datasets", exist_ok=True)

    data = {
        "Peak": [],
        "Artist": [],
        "SongName": [],
        "Weeks": [],
    }

    for i, container in enumerate(soup.select("ul.o-chart-results-list-row")):
        song = container.find("h3", {"class": "c-title"}).text.strip()
        artist = container.find("span", {"class": "a-no-trucate"}).text.strip()

        last_week, peak_position, weeks_on_chart = container.find_all(
            "ul", {"class": "lrv-a-unstyle-list"})[-1].text.strip().split()

        data["Peak"].append(peak_position)
        data["Artist"].append(artist.replace("Featuring", "Feat."))
        data["SongName"].append(song)
        data["Weeks"].append(weeks_on_chart)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


def GLOBAL200():
    driver = ChromeDriverManager().install()
    service = Service(driver)
    options = Options()
    options.add_argument("--window-size=1020,1200")
    navegador = webdriver.Chrome(service=service, options=options)

    navegador.get("https://www.billboard.com/charts/billboard-global-200/")
    time.sleep(5)

    soup = BeautifulSoup(navegador.page_source, "html.parser")
    navegador.quit()

    filename = "datasets/global200.csv"
    os.makedirs("datasets", exist_ok=True)

    data = {
        "Peak": [],
        "Artist": [],
        "SongName": [],
        "Weeks": [],
    }

    for i, container in enumerate(soup.select("ul.o-chart-results-list-row")):
        song = container.find("h3", {"class": "c-title"}).text.strip()
        artist = container.find("span", {"class": "a-no-trucate"}).text.strip()

        last_week, peak_position, weeks_on_chart = container.find_all(
            "ul", {"class": "lrv-a-unstyle-list"})[-1].text.strip().split()

        data["Peak"].append(peak_position)
        data["Artist"].append(artist.replace("Featuring", "Feat."))
        data["SongName"].append(song)
        data["Weeks"].append(weeks_on_chart)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def Billboard_200():
    driver = ChromeDriverManager().install()
    service = Service(driver)
    options = Options()
    options.add_argument("--window-size=1020,1200")
    navegador = webdriver.Chrome(service=service, options=options)

    navegador.get("https://www.billboard.com/charts/billboard-200/")
    time.sleep(5)

    soup = BeautifulSoup(navegador.page_source, "html.parser")
    navegador.quit()

    filename = "datasets/bilboard200.csv"
    os.makedirs("datasets", exist_ok=True)

    data = {
        "Peak": [],
        "Artist": [],
        "SongName": [],
        "Weeks": [],
    }

    for i, container in enumerate(soup.select("ul.o-chart-results-list-row")):
        song = container.find("h3", {"class": "c-title"}).text.strip()
        artist = container.find("span", {"class": "a-no-trucate"}).text.strip()

        last_week, peak_position, weeks_on_chart = container.find_all(
            "ul", {"class": "lrv-a-unstyle-list"})[-1].text.strip().split()

        data["Peak"].append(peak_position)
        data["Artist"].append(artist.replace("Featuring", "Feat."))
        data["SongName"].append(song)
        data["Weeks"].append(weeks_on_chart)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


def tiktok_top50():

    driver = ChromeDriverManager().install()
    service = Service(driver)
    options = Options()
    options.add_argument("--window-size=1020,1200")
    navegador = webdriver.Chrome(service=service, options=options)

    navegador.get("https://www.billboard.com/charts/tiktok-billboard-top-50/")
    time.sleep(5)

    soup = BeautifulSoup(navegador.page_source, "html.parser")
    navegador.quit()

    filename = "datasets/tiktok50.csv"
    os.makedirs("datasets", exist_ok=True)

    data = {
        "Peak": [],
        "Artist": [],
        "SongName": [],
        "Weeks": [],
    }

    for i, container in enumerate(soup.select("ul.o-chart-results-list-row")):
        song = container.find("h3", {"class": "c-title"}).text.strip()
        artist = container.find("span", {"class": "a-no-trucate"}).text.strip()

        last_week, peak_position, weeks_on_chart = container.find_all(
            "ul", {"class": "lrv-a-unstyle-list"})[-1].text.strip().split()


        data["Peak"].append(peak_position)
        data["Artist"].append(artist.replace("Featuring", "Feat."))
        data["SongName"].append(song)
        data["Weeks"].append(weeks_on_chart)


    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    HOT100()
    GLOBAL200()
    Billboard_200()
    tiktok_top50()