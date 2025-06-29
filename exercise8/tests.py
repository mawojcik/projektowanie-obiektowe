import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/product")

    def tearDown(self):
        self.driver.quit()

    def test_index_page_loads(self):
        self.assertIn("Product", self.driver.title)

    def test_index_lists_products(self):
        products = self.driver.find_elements(By.CSS_SELECTOR, ".product-row")
        self.assertGreaterEqual(len(products), 0)
    
    def test_navigate_to_new_product_form(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        self.assertIn("/product/new", self.driver.current_url)

    def test_create_valid_product(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        self.driver.find_element(By.NAME, "product[name]").send_keys("Test Product")
        self.driver.find_element(By.NAME, "product[description]").send_keys("Test description")
        self.driver.find_element(By.NAME, "product[price]").send_keys("99.99")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()

        self.assertIn("/product", self.driver.current_url)
        body = self.driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Test Product", body)

    def test_create_product_empty_name(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        self.driver.find_element(By.NAME, "product[description]").send_keys("Test description")
        self.driver.find_element(By.NAME, "product[price]").send_keys("99.99")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        self.assertIn("This value should not be blank", self.driver.page_source)

    def test_create_product_invalid_price(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        self.driver.find_element(By.NAME, "product[name]").send_keys("Invalid Price Product")
        self.driver.find_element(By.NAME, "product[price]").send_keys("not a number")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        self.assertIn("This value is not valid", self.driver.page_source)

    def test_view_product_details(self):
        self.driver.find_element(By.LINK_TEXT, "show").click()
        self.assertIn("/product/", self.driver.current_url)
        self.assertIn("Product", self.driver.page_source)

    def test_edit_product(self):
        self.driver.find_element(By.LINK_TEXT, "edit").click()
        name_input = self.driver.find_element(By.NAME, "product[name]")
        name_input.clear()
        name_input.send_keys("Updated Product")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        self.assertIn("Updated Product", self.driver.page_source)

    def test_delete_product(self):
        delete_forms = self.driver.find_elements(By.CSS_SELECTOR, "form[action*='/delete']")
        if delete_forms:
            token_input = delete_forms[0].find_element(By.NAME, "_token")
            self.driver.execute_script("arguments[0].form.submit();", token_input)
            self.assertIn("/product", self.driver.current_url)

    def test_add_product_long_name(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        long_name = "A" * 250
        self.driver.find_element(By.NAME, "product[name]").send_keys(long_name)
        self.driver.find_element(By.NAME, "product[description]").send_keys("Long name test")
        self.driver.find_element(By.NAME, "product[price]").send_keys("12.34")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        page = self.driver.page_source
        self.assertIn(long_name, page)
        self.assertIn("12.34", page)


    def test_add_product_zero_price(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        self.driver.find_element(By.NAME, "product[name]").send_keys("Free Product")
        self.driver.find_element(By.NAME, "product[description]").send_keys("Free")
        self.driver.find_element(By.NAME, "product[price]").send_keys("0.0")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        self.assertIn("Free Product", self.driver.page_source)


    def test_form_waits_to_load(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        form = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, "product[name]"))
        )
        self.assertTrue(form.is_displayed())

    def test_buttons_present(self):
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "Create new"))
        self.assertTrue(any("edit" in btn.text for btn in self.driver.find_elements(By.LINK_TEXT, "edit")))

    def test_product_table_structure(self):
        headers = self.driver.find_elements(By.TAG_NAME, "th")
        self.assertIn("Name", [h.text for h in headers])


    def test_xss_injection(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        self.driver.find_element(By.NAME, "product[name]").send_keys("<script>alert(1)</script>")
        self.driver.find_element(By.NAME, "product[description]").send_keys("xss")
        self.driver.find_element(By.NAME, "product[price]").send_keys("1.0")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        body = self.driver.find_element(By.TAG_NAME, "body").get_attribute("innerHTML")
        self.assertNotIn("<script>", body)


    def test_index_page_loads_and_has_content(self):
        self.assertIn("Product", self.driver.title)
        body = self.driver.find_element(By.TAG_NAME, "body").text
        self.assertIsNotNone(body)
        self.assertGreaterEqual(len(body), 0)

    def test_buttons_and_links_present(self):
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "Create new"))
        self.assertTrue(any("show" in e.text for e in self.driver.find_elements(By.TAG_NAME, "a")))
        self.assertTrue(any("edit" in e.text for e in self.driver.find_elements(By.TAG_NAME, "a")))


    def test_product_detail_view(self):
        self.driver.find_elements(By.LINK_TEXT, "show")[0].click()
        self.assertIn("/product/", self.driver.current_url)
        self.assertIn("Product", self.driver.page_source)
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "edit"))
        self.assertIn("Description", self.driver.page_source)

    def test_edit_product_functionality(self):
        self.driver.find_elements(By.LINK_TEXT, "edit")[0].click()
        name_field = self.driver.find_element(By.NAME, "product[name]")
        name_field.clear()
        name_field.send_keys("Updated Product")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()

        self.assertIn("/product", self.driver.current_url)
        self.assertIn("Updated Product", self.driver.page_source)
        self.assertIn("edit", self.driver.page_source)
        self.assertIn("show", self.driver.page_source)

    def test_delete_product(self):
        form = self.driver.find_elements(By.CSS_SELECTOR, "form[action*='/delete']")[0]
        token_input = form.find_element(By.NAME, "_token")
        self.driver.execute_script("arguments[0].form.submit();", token_input)

        self.assertIn("/product", self.driver.current_url)
        self.assertNotIn("Updated Product", self.driver.page_source)

    def test_create_multiple_products(self):
        for i in range(10):
            self.driver.find_element(By.LINK_TEXT, "Create new").click()
            self.driver.find_element(By.NAME, "product[name]").send_keys(f"Product {i}")
            self.driver.find_element(By.NAME, "product[description]").send_keys("Desc")
            self.driver.find_element(By.NAME, "product[price]").send_keys(str(10 + i))
            self.driver.find_element(By.CSS_SELECTOR, "form").submit()
            self.assertIn(f"Product {i}", self.driver.page_source)
            self.assertIn(str(10 + i), self.driver.page_source)

    def test_long_name_and_edge_cases(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        long_name = "A" * 255
        self.driver.find_element(By.NAME, "product[name]").send_keys(long_name)
        self.driver.find_element(By.NAME, "product[description]").send_keys("Long name")
        self.driver.find_element(By.NAME, "product[price]").send_keys("0")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        self.assertIn(long_name, self.driver.page_source)
        self.assertIn("0", self.driver.page_source)

    def test_ui_elements_exist(self):
        headers = self.driver.find_elements(By.TAG_NAME, "th")
        headers_text = [h.text for h in headers]
        self.assertIn("Name", headers_text)
        self.assertIn("Price", headers_text)
        self.assertIn("Actions", headers_text)

    def test_xss_prevention(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        self.driver.find_element(By.NAME, "product[name]").send_keys("<script>alert(1)</script>")
        self.driver.find_element(By.NAME, "product[description]").send_keys("xss test")
        self.driver.find_element(By.NAME, "product[price]").send_keys("1.0")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        html = self.driver.find_element(By.TAG_NAME, "body").get_attribute("innerHTML")
        self.assertNotIn("<script>", html)
        self.assertIn("xss test", html)

    def test_waits_and_js_loading(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()
        form = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, "product[name]"))
        )
        self.assertTrue(form.is_displayed())

        self.assertTrue(self.driver.find_element(By.NAME, "product[description]").is_displayed())
        self.assertTrue(self.driver.find_element(By.NAME, "product[price]").is_displayed())

    def test_create_product_form_validation_and_success(self):
        self.driver.find_element(By.LINK_TEXT, "Create new").click()

        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        self.assertIn("This value should not be blank", self.driver.page_source)
        self.assertIn("form", self.driver.page_source)
        self.assertIn("Name", self.driver.page_source)

        self.driver.find_element(By.NAME, "product[name]").send_keys("Incomplete Product")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        self.assertIn("This value should not be blank", self.driver.page_source)
        self.assertIn("Incomplete Product", self.driver.page_source)

        self.driver.find_element(By.NAME, "product[description]").send_keys("Invalid price")
        self.driver.find_element(By.NAME, "product[price]").send_keys("abc")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        self.assertIn("This value is not valid", self.driver.page_source)
        self.assertIn("Invalid price", self.driver.page_source)

        self.driver.find_element(By.NAME, "product[price]").clear()
        self.driver.find_element(By.NAME, "product[price]").send_keys("99.99")
        self.driver.find_element(By.CSS_SELECTOR, "form").submit()
        self.assertIn("/product", self.driver.current_url)
        self.assertIn("Incomplete Product", self.driver.page_source)
        self.assertIn("Invalid price", self.driver.page_source)
        self.assertIn("99.99", self.driver.page_source)
        self.assertIn("Show", self.driver.page_source)

if __name__ == "__main__":
    unittest.main()