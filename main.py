from selenium import webdriver
from time import sleep
from password import password
from selenium.webdriver.common.keys import Keys

#we need to actually start a webdriver. We can do so with only one line of code:

#automating a simple task like your website’s login form
class InstaBot():
    links=[]
    comments = ['Awesome!']
    def __init__(self):
        #enter your username
        self.login('enter your user name here')
        self.like_comment_hashtag('cars')
    def login(self, username):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        username_input=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        username_input.send_keys(username)
        password_input=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        #open file password and type your password there
        password_input.send_keys(password)
        submit_button=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
        submit_button.click()
        sleep(5)
        not_now_button1=self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        not_now_button1.click()
        sleep(5)
        not_now_button2=self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_button2.click()
    def like_comment_hashtag(self, hashtag):
        search_box = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_box.send_keys('#'+hashtag)
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a').click()
        sleep(5)

        links= self.driver.find_elements_by_tag_name('a')
        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        more_links = list(filter(condition, links))
        for i in range(7):
            link = more_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)
        for link in self.links:
            self.driver.get(link)


            #likeposts
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(3)
            # comment
            # comment
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            self.driver.find_element_by_xpath(
                "//textarea[@placeholder='Add a comment…']").send_keys(self.comments[0])
            sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[4]/div/div/button').click()
            self.driver.find_element_by_xpath(
                "//button[@type='submit']").click()
            sleep(2)
def main():
        instagram_bot=InstaBot()

if __name__ == '__main__':
    main()
