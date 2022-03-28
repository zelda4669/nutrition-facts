from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestNewVisitor(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

# Our user wants to create a Nutrition Facts label for one of their favorite recipes.
# She navigates to the website and sees a form inviting her to input the ingredients for her recipe
    def test_site_can_accept_ingredients_and_generate_label(self):
        self.driver.get('http:localhost:8000')
        self.assertIn('Nutrition Facts', self.driver.title)

# She inputs her ingredients list into the box and clicks the "Generate Label" button
        recipe = '3 pounds bone-in, skin-on chicken thighs and drumsticks; 3 poblano peppers; 12 ounces tomatillos; ' \
                 '1 white onion; 2 Anaheim peppers; 2 Serrano peppers; 6 medium cloves garlic; 1 tablespoon cumin; ' \
                 '1/2 cup cilantro; 1 tablespoon Asian fish sauce'
        servings = self.driver.find_element(By.ID, 'noservings')
        ingredients = self.driver.find_element(By.ID, 'ingredients')
        servings.send_keys('8')
        ingredients.send_keys(recipe)

# A new page loads displaying her nutrition label

# She doesn't like how much sugar is in this recipe and wonders if she can edit the ingredients to reduce it.
# Then she sees the "Edit ingredients list" button in the top right corner and clicks it

# The page refreshes again to show an editable version of her ingredients list

# This time, the page also includes a list of suggested substitutions that pinpoints specific ideas to change

# She makes a few of the suggested changes and saves the new ingredients list.

# Once again, the page shows her newly updated Nutrition Facts label. Happy with her updated recipe,
# she now wonders how she can save the label

# She notices at the bottom of the page are instructions. She can print the label, save it as a PNG,
# or get a link to view her label online at any time in the future

if __name__ == '__main__':
    unittest.main()
