*** Settings ***
Library           SynaptAI.py
Library           SeleniumLibrary

*** Variables ***
${BROWSER_PATH}   C:/Users/shravan.v/Pictures/New folder/msedgedriver.exe
${BASE_URL}       https://synapt.ai/

*** Test Cases ***
Test Synapt AI Tab
    [Documentation]     To Verify the Synapt AI website.
    SynaptAI.Open Browser    ${BROWSER_PATH}    ${BASE_URL}
    Navigation Bar
    SynaptAI.Close Browser