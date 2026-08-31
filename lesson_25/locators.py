# XPath-локатори

# 1. Header
xpath_header = "//header[contains(@class,'header')]"

# 2. Header to Logo
xpath_logo = "//header[contains(@class,'header')]//a[contains(@class,'header_logo')]"

# 3. Home
xpath_home = "//nav//a[contains(@class,'header-link') and normalize-space()='Home']"

# 4. About
xpath_about = "//button[@appscrollto='aboutSection']"

# 5. Contacts
xpath_contacts = "//button[@appscrollto='contactsSection']"

# 6. Guest log in
xpath_guest_login = "//button[normalize-space()='Guest log in']"

# 7. Sign In
xpath_sign_in = "//button[normalize-space()='Sign In']"

# 8. Sign up
xpath_sign_up = "//button[normalize-space()='Sign up']"

# 9. Contacts heading
xpath_contacts_heading = "//div[contains(@class,'col-md-6')]//h2[normalize-space()='Contacts']"

# 10. Contacts links Axe
xpath_contacts_link = "//h2[normalize-space()='Contacts']/ancestor::div[@id='contactsSection']//a[contains(@class,'contacts_link')]"

# CSS-локатори

# 1. Header
css_header = "header.header"

# 2. Logo in Header
css_logo = "a.header_logo"

# 3. Home
css_home = "nav a.header-link.-active"

# 4. About
css_about = "button[appscrollto='aboutSection']"

# 5. Contacts
css_contacts = "button[appscrollto='contactsSection']"

# 6. Guest log in
css_guest_login = "button.header-link.-guest"

# 7. Sign In
css_sign_in = "button.header_signin"

# 8. Sign up
css_sign_up = "button.hero-descriptor_btn"

# 9. Contacts heading
css_contacts_heading = "#contactsSection h2"

# 10. Footer Logo
css_footer_logo = "a.footer_logo"