class Locators:
#Login page elements
    textbox_email_name = "username"
    textbox_password_name = "password"
    Checkbox_rememberme = ""
    button_Login_xpath = "//*[@id='loginfrm']/button"
    button_Signup_xpath = "//*[@id='loginfrm']/div[4]/div[1]/a"
    button_forgetpwd_xpath = "//*[@id='loginfrm']/div[4]/div[3]/a"
    Button_logout_xpath = "//*[@class='d-none d-md-block fl']"
    Click_Logout_xpath ="//*[@class='dropdown-item tr']"

#Signup page elements
    Button_Signup = "//*[@id='loginfrm']/div[4]/div[1]/a"
    textbox_firstname_name = "firstname"
    textbox_lastname_name = "lastname"
    textbox_mobilenum_name = "phone"
    textbox_emailid_name = "email"
    textbox_pwd_name = "password"
    textbox_c_pwd_name = "confirmpassword"
    Button_click_signup = "//*[@id='headersignupform']/div[8]/button"

#Homepage elements
    Link_homepage = "//*[@id='mobileMenuMain']/nav/ul[1]/li/a"
    Link_hotels = "//*[@id='search']/div/div/div/div/div/nav/ul/li[1]/a"
    Link_flights = "//*[@id='search']/div/div/div/div/div/nav/ul/li[2]/a"
    Link_Tours = "//*[@id='search']/div/div/div/div/div/nav/ul/li[3]/a"
    Link_TourThailand = "/html/body/div[2]/div[1]/div[3]/div/div[2]/div[2]/figure/a"



