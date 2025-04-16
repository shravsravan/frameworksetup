*** Settings ***
Library           DotComRobot.py
Library           SeleniumLibrary

*** Variables ***
${BROWSER_PATH}   C:/Users/shravan.v/Pictures/New folder/msedgedriver.exe
${BASE_URL}       https://www.prodapt.com/

*** Test Cases ***
Test Navigation
    [Documentation]   To Verify navigation tabs work as expected.
    DotComRobot.Open Browser    ${BROWSER_PATH}    ${BASE_URL}
    Main Nav
    DotComRobot.Close Browser

Test Services Tab
    [Documentation]    To Verify services-related tabs.
    DotComRobot.Open Browser    ${BROWSER_PATH}    ${BASE_URL}
    Service Tab
    DotComRobot.Close Browser

Test Success Stories Tab
    [Documentation]    To Verify the success stories tab functionality.
    DotComRobot.Open Browser    ${BROWSER_PATH}    ${BASE_URL}
    Success Story Tab
    DotComRobot.Close Browser

Test Insights Tab
    [Documentation]    To Verify the Insights tab functionality.
    DotComRobot.Open Browser    ${BROWSER_PATH}    ${BASE_URL}
    Insights Tab
    DotComRobot.Close Browser

Test About us Tab
    [Documentation]    To Verify the Insights tab functionality.
    DotComRobot.Open Browser    ${BROWSER_PATH}    ${BASE_URL}
    About Us
    DotComRobot.Close Browser

Test Contact us form
    [Documentation]     To Verify the test contact us form submission funtionality.
    DotComRobot.Open Browser    ${BROWSER_PATH}    ${BASE_URL}
    Contact Us Form
    DotComRobot.Close Browser
