from bs4 import BeautifulSoup
import time
import random
import requests


# options = webdriver.ChromeOptions()

# options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0")

# options.add_argument("--disable-blink-features=AutomationControlled")

# browser = webdriver.Chrome(options=options)
try:

	jazz_music = []
	
	for i in range(1, 49):

		url = f"https://www.last.fm/ru/tag/classical/artists?page={i}"

		headers = {
			"accept": "*/*", 
			"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0" 
		}

		req = requests.get(url, headers=headers)
		src = req.text

		# with open("index.html", "w", encoding="utf-8") as file:
		# 	file.write(src)

		# with open("index.html", encoding="utf-8") as file:
		# 	src = file.read()

		soup = BeautifulSoup(src, "lxml")

		allsingers = soup.find_all(class_="link-block-target")

		for name in allsingers[2:]:
			jazz_music_name = name.text
			jazz_music.append(jazz_music_name)


			
		print(f"{i} страница скопирована!")
		time.sleep(random.randrange(2, 4))

			
	with open("Classic.txt", "a", encoding="utf-8") as file:
		for name_jazz in jazz_music:
			file.write(name_jazz + "\n")
	print(Работа завершена!)
except Exception as ex:
	print(ex)
