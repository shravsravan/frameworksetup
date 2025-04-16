*** Settings ***
Library           Pivot.py
Library           SeleniumLibrary

*** Variables ***
${BROWSER_PATH}   C:/Users/shravan.v/Pictures/New folder/msedgedriver.exe
${BASE_URL}       https://prodaptcloud.sharepoint.com/sites/voiceportal

*** Test Cases ***
Test Navigation
        Pivot.Open Browser    ${BROWSER_PATH}    ${BASE_URL}
        Main Nav
        Pivot.Close Browser