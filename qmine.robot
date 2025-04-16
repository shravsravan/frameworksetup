*** Settings ***
Library     SeleniumLibrary
Library    Collections

*** Test Cases ***
Login
    Open Browser                        https://prodaptcloud.sharepoint.com/sites/Voice-Dev/SitePages/Qmine.aspx                  edge
    Maximize Browser Window
    Sleep    15
    Click Element    xpath=//*[@id="setempvalue"]
    Sleep    5
    Element Text Should Be    xpath=//*[@id="setempvalue"]    sethuraman.m@prodapt.com
    List Should Contain Value    list_    value

