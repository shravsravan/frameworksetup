import SeleniumLibrary

*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
Login
    Open Browser                        https://www.saucedemo.com/                  chrome
    Maximize Browser Window
    Wait Until Element Is Visible       id:user-name
    Input Text                          id:user-name                                standard_user
    Input Password                      id:password                                 secret_sauce
    Click Element                       id:login-button
    Wait Until Element Is Visible       id=add-to-cart-sauce-labs-backpack          timeout=10
    Click Element                       id=add-to-cart-sauce-labs-backpack
    Click Element                       css=.shopping_cart_link
    Click Element                       id=checkout
    Input Text                          xpath=//input[@data-test="firstName"]        DummyUser
    Input Text                          xpath=//input[@data-test="lastName"]         UserDummy
    Input Text                          xpath=//input[@data-test="postalCode"]       100250
    Click Element                       xpath=//input[@data-test="continue"]
    Click Element                       xpath=//button[@data-test="finish"]
    Click Element                       xpath=//button[@data-test="back-to-products"]
    Sleep                               5s
    Close Browser
