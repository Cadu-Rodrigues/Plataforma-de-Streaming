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
        
        #teste para o campo de usuario para cadastro
        try:
            user = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/input[1]")))
            user.clear()
            user.send_keys("mariafernandabasso@gmail.com")
            assert(user.get_attribute("value") == "mariafernandabasso@gmail.com")
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para o campo de senha para cadastro
        try:
            password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/input[2]")))
            password.clear()
            password.send_keys("roger123")
            assert(password.get_attribute("value") == "* * * * * * * * ")
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para o botao cadastrar-se
        try:
            sign_in = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[2]/button/span[1]")))
            sign_in.click()
            assert(WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/input[3]"))))
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para o campo de nome para cadastro
        try:
            user = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/input[3]")))
            user.clear()
            user.send_keys("Maria Fernanda")
            assert(user.get_attribute("value") == "Maria Fernanda")
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para o botao entrar (cadastro)
        try:
            sign_in = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div/button/span[1]")))
            sign_in.click()
            assert(WebDriverWait(driver, 30).until(EC.url_to_be("http://localhost:3001/dashboard")))
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para avatar
        try:
            sign_in = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='avatar']")))
            sign_in.click()
            assert(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='configuracoes']"))))
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para o botao logout
        try:
            sign_in = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div/p[3]")))
            sign_in.click()
            assert(WebDriverWait(driver, 30).until(EC.url_to_be("http://localhost:3001/")))
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para o campo de usuario para login
        try:
            user = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/input[1]")))
            user.clear()
            user.send_keys("mariafernandabasso@gmail.com")
            assert(user.get_attribute("value") == "mariafernandabasso@gmail.com")
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para o campo de senha para login
        try:
            password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/input[2]")))
            password.clear()
            password.send_keys("roger123")
            assert(password.get_attribute("value") == "* * * * * * * * ")
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para o botao entrar (login)
        try:
            sign_in = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div/div[1]/button/span[1]")))
            sign_in.click()
            assert(WebDriverWait(driver, 30).until(EC.url_to_be("http://localhost:3001/dashboard")))
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para aba albuns
        try:
            albums = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]")))
            albums.click()
            page_albums = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/h1")))
            assert(page_albums.text == "Albuns")
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para um album
        try:
            album = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[2]/section/div[1]/label[1]")))
            album.click()
            assert(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='album-infos']"))))
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)
            
        #teste para aba artistas
        try:
            artists = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[3]")))
            artists.click()
            page_artists = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/h1")))
            assert(page_artists.text == "Artistas")
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para um artista
        try:
            artist = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[2]/section/div[1]")))
            artist.click()
            assert(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='album-infos']"))))
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para aba musicas
        try:
            songs = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/div[1]/div[4]")))
            songs.click()
            page_songs = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/h1")))
            assert(page_songs.text == "Musicas")
            time.sleep(2)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(2)

        #teste para reproduzir uma musica
        try:
            play = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='playbtn']")))
            play.click()
            time.sleep(5)
        except Exception as e:
            e = traceback.format_exc()
            print("Error: ", e)
            time.sleep(5)


        driver.close()

if __name__ == "__main__":
    Test_Interface()