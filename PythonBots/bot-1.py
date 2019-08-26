from selenium import webdriver
import os
import time




class InstagramBot:

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.base_url = ('https://www.instagram.com')
		self.driver = webdriver.Chrome('chromedriver.exe')
		
		self.login()



	def login(self):
		self.driver.get('{}/accounts/login/'.format(self.base_url))

		self.driver.find_element_by_name('username').send_keys(self.username)
		self.driver.find_element_by_name('password').send_keys(self.password)
		self.driver.find_element_by_xpath(
			'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
		time.sleep(4)
		self.driver.find_element_by_xpath(
			'/html/body/div[3]/div/div/div[3]/button[2]').click()


	def nav_user(self,user):
		self.driver.get('{}/{}/'.format(self.base_url, user))
		time.sleep(10)


	def followers_list(self):

		self.driver.find_element_by_xpath(
			'//*[@id="react-root"]/section/main/div/ul/li[2]/a/span').click()






if __name__ == '__main__':
	

	ig_bot = InstagramBot('paarthur_','nevermind123' )
	ig_bot.nav_user('casadesincha')
	





