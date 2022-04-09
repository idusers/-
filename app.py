from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
import time
import random
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

'''在浏览器中打开网址'''
# ed_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) >AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57')

line = random.random()
print(line)

options = ChromeOptions()
options.add_argument('--headless')
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
options.add_argument('user-agent="%s"' % ua)
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
# options.add_argument("-proxy-server=171.92.21.193:9000")

driver = webdriver.Chrome(chrome_options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
def origin():
	driver.get("XXXXXX")
	wait = WebDriverWait(driver, 15)


# 跳过起始页
from selenium.webdriver.common.action_chains import ActionChains
def tiao():
	ActionChains(driver).click(driver.find_element_by_xpath("//*[text()='上滑开始']")).perform()

time.sleep(5)

def t1():
	line = random.random()
	print(line)
	if line > 0.5:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div1 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div1 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()

def t2():
	line = random.random()
	print(line)
	if line >= 0.86:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div2 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.63 <= line < 0.86:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div2 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div2 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t3():
	line = random.random()
	print(line)
	if line >= 0.47:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div3 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.23 <= line < 0.47:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div3 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div3 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t4():
	# CSS_SELECTOR的方法来定位
	line = random.random()
	print(line)
	if line >= 0.86:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div4 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.43 <= line < 0.86:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div4 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div4 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t5():
	line = random.random()
	print(line)
	if line >= 0.65:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div5 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div5 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
	elif 0.43 <= line < 0.65:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div5 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div5 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.23 <= line < 0.43:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div5 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div5 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div5 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div5 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t6():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div6 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.50 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div6 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	elif 0.25 <= line < 0.50:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div6 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div6 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()

def t7():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div7 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.50 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div7 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	elif 0.25 <= line < 0.50:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div7 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div7 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()

def t8():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div8 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div8 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
	elif 0.50 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div8 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div8 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.25 <= line < 0.50:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div8 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div8 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div8 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div8 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t9():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div9 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div9 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
	elif 0.50 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div9 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div9 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.25 <= line < 0.50:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div9 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div9 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div9 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div9 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t10():
	line = random.random()
	print(line)
	if line >= 0.80:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div10 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div10 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
	elif 0.60 <= line < 0.80:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div10 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div10 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.45 <= line < 0.60:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div10 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div10 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div10 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div10 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t11():
	line = random.random()
	print(line)
	if line >= 0.85:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div11 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.70 <= line < 0.85:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div11 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	elif 0.15 <= line < 0.70:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div11 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div11 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()

def t12():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div12 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.50 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div12 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	elif 0.25 <= line < 0.50:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div12 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div12 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()

def t13():
	line = random.random()
	print(line)
	if line >= 0.86:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div13 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.25 <= line < 0.86:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div13 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div13 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t14():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div14 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.50 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div14 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	elif 0.25 <= line < 0.50:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div14 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div14 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()

def t15():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div15 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.50 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div15 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	elif 0.25 <= line < 0.50:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div15 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div15 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()

def t16():
	line = random.random()
	print(line)
	if line >= 0.86:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div16 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.43 <= line < 0.86:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div16 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div16 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t17():
	line = random.random()
	print(line)
	if line >= 0.85:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div17 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.70 <= line < 0.85:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div17 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	elif 0.15 <= line < 0.70:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div17 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div17 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()

def t18():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div18 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.50 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div18 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	elif 0.25 <= line < 0.50:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div18 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div18 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()

def t19():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div19 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.30 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div19 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div19 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()

def t20():
	line = random.random()
	print(line)
	if line >= 0.63:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(5) > div')).perform()
	elif 0.42 <= line < 0.63:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div19 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	elif 0.19 <= line < 0.42:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(5) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div20 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
		
def t21():
	line = random.random()
	print(line)
	if line >= 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div21 > div.ui-controlgroup.column1 > div:nth-child(1) > div')).perform()
	elif 0.50 <= line < 0.75:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div21 > div.ui-controlgroup.column1 > div:nth-child(2) > div')).perform()
	elif 0.25 <= line < 0.50:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div21 > div.ui-controlgroup.column1 > div:nth-child(3) > div')).perform()
	else:
		ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#div21 > div.ui-controlgroup.column1 > div:nth-child(4) > div')).perform()

def run():
	origin()
	tiao()
	time.sleep(1)
	t1()
	time.sleep(1)
	t2()
	time.sleep(1)
	t3()
	time.sleep(1)
	t4()
	time.sleep(1)
	t5()
	time.sleep(1)
	t6()
	time.sleep(1)
	t7()
	time.sleep(1)
	t8()
	time.sleep(1)
	t9()
	time.sleep(1)
	t10()
	time.sleep(1)
	t11()
	time.sleep(1)
	t12()
	time.sleep(1)
	t13()
	time.sleep(1)
	t14()
	time.sleep(1)
	t15()
	time.sleep(1)
	t16()
	time.sleep(1)
	t17()
	time.sleep(1)
	t18()
	time.sleep(1)
	t19()
	time.sleep(1)
	t20()
	time.sleep(1)
	t21()
	time.sleep(1)
	ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#ctlNext')).perform()
	time.sleep(3)
	ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#alert_box > div:nth-child(2) > div:nth-child(2) > button')).perform()
	time.sleep(2)
	ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, '#rectMask')).perform()
	time.sleep(3)
	driver.close()


run()
