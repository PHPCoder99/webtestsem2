import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


def test_step1():
    x_selector1 = '//*[@id="login"]/div[1]/label/input'
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("12345678901234567891")
    x_selector2 = '//*[@id="login"]/div[2]/label/input'
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("499351bfa5")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    site.driver.implicitly_wait(3)
    x_selector3 = '//*[@id="app"]/main/div/div[1]/h1'
    blog_label = site.find_element("xpath", x_selector3)
    assert blog_label.text == "Blog"


def test_step2():
    x_selector4 = '//*[@id="create-btn"]'
    btn = site.find_element("xpath", x_selector4)
    btn.click()
    site.driver.implicitly_wait(3)
    x_selector5 = '//*[@id="create-item"]/div/div/div[1]/div/label/input'
    title = site.find_element("xpath", x_selector5)
    title.send_keys(testdata["post_title"])
    x_selector6 = '//*[@id="create-item"]/div/div/div[3]/div/label/div'
    content = site.find_element("xpath", x_selector6)
    content.send_keys(testdata["post_content"])
    x_selector7 = '//*[@id="create-item"]/div/div/div[7]/div/button'
    btn = site.find_element("xpath", x_selector7)
    btn.click()
    site.driver.implicitly_wait(3)
    x_selector8 = '//*[@id="app"]/main/div/div[1]/h1'
    title = site.find_element("xpath", x_selector8).text
    x_selector9 = '//*[@id="app"]/main/div/div[1]/div/div[3]'
    content = site.find_element("xpath", x_selector9).text
    assert all([title == testdata["post_title"], content == testdata["post_content"]])
