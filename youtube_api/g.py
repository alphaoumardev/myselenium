import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
ids = [
    'ginna_figueredo',
    'jazwanderlust',
    'callherclassy',
    'mattidomingue',
    'dreamalittledreamvt',
    'laurendombrowerr',
    'leahmob',
    'leraclark',
    'rachel.rachelrachel',
    'marielle.elizabeth',
    '_alyssamay',
    'jessajo7',
    'kotineru',
    'nikkiq',
    'courtneecrews',
    'naturallynella',
    'destineewray',
    'masonoglesby',
    'livingmybeststyle',
    'whereyourheartisnow',
    'frenchyfatim',
    'fionamaefit',
    'brittney_cherelle',
    'rae.hersey',
    'sewsarahr',
    'simplylaurenrose',
    'hope.ceee',
    'janellepaigebrandom',
    'mionabell',
    'threadloopfits',
    'daisyfarhm',
    'jeniferjbeauty',
    'alexajeanbrown',
    'holliewdwrd',
    'lindseyharrod',
    'roses_cloud',
    'georgiamayheath',
    'bludetiger',
    'sistersguidetostyle',
    'allaroundaudrey',
    'tatianaelizabethh',
    'jennjakson',
    'drea_vc',
    'daniellee_esther',
    'thecheekybeen',
    'itsallchictome',
    'lachelletrends',
]
driver.get('https://www.instagram.com')
time.sleep(70)
for i in ids:
    try:
        driver.get('https://www.instagram.com/{}/'.format(i))
        time.sleep(20)
    except:
        print('')
