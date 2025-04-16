*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://prodaptcloud.sharepoint.com/sites/SynaptHub/SitePages/Synapt-Dev.aspx
${BROWSER}    Chrome

*** Test Cases ***
Open Synapt Hub Page
    [Documentation]    Open the Prodapt Synapt Hub page and verify elements
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    //input[@type='search']    10s
    Wait Until Page Contains    Synapt GPT
    Click Element    xpath=//div[text()='Synapt GPT']
    [Teardown]    Close Browser

Navigate And Verify Sections
    [Documentation]    Test navigation and presence of key sections
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    Use Case Factory
    Wait Until Page Contains    Playground
    Wait Until Page Contains    Case Studies
    [Teardown]    Close Browser
