** Settings **
Library    Selenium2Library
*** Test Cases ***
Findying dexcom at google

    Open Browser    https://www.google.com/    chrome
    Input Text      css:body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input    dexcom financial results
    Click Button    css:body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b
    Click Element    css:#hdtb-msb > div:nth-child(1) > div > div:nth-child(2) > a