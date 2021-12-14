import os
from selenium import webdriver
from selenium.webdriver.ie.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import traceback

class Test_Interface():
    def __init__(self):

        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        
        caps = webdriver.DesiredCapabilities().FIREFOX
        caps["marionette"] = True
        driver = webdriver.Firefox(capabilities=caps, executable_path="./geckodriver")
        driver.get("http://localhost:3001/")
        
        #teste para o campo de usuario
        try:
            user = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/input[1]")))
            user.clear()
            user.send_keys("mariafernandabasso@gmail.com")
            assert(user.get_attribute("value") == "mariafernandabasso@gmail.com")
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)

        #teste para o campo de senha
        try:
            password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/input[2]")))
            password.clear()
            password.send_keys("roger123")
            assert(password.get_attribute("value") == "* * * * * * * * ")
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)

        #teste para o botao entrar (login)
        try:
            sign_in = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button/span[1]")))
            sign_in.click()
            assert(WebDriverWait(driver, 30).until(EC.url_to_be("http://localhost:3001/dashboard")))
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)

        #teste para aba albuns
        try:
            albums = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]")))
            albums.click()
            page_albums = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/h1")))
            assert(page_albums.text == "Albuns")
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)

        #teste para um album
        try:
            album = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[2]/section/div[1]/label[1]")))
            album.click()
            assert(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='album-infos']"))))
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            

        #teste para aba artistas
        try:
            artists = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]")))
            artists.click()
            page_artists = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/h1")))
            assert(page_artists.text == "Artistas")
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)

        #teste para um artista
        try:
            artist = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[2]/section/div[1]")))
            artist.click()
            assert(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='album-infos']"))))
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)

        #teste para aba musicas
        try:
            songs = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[4]")))
            songs.click()
            page_songs = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/h1")))
            assert(page_songs.text == "Musicas")
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)

        #teste para reproduzir uma musica
        try:
            play = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='playbtn']")))
            play.click()
            playing = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/section/div[1]/div[1]/svg/path")
            assert(playing.get_attribute("d") == "M9 16h2V8H9v8zm3-14C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm1-4h2V8h-2v8z")
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)


        driver.close()

if __name__ == "__main__":
    Test_Interface()