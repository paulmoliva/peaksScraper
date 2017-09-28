import requests

districtID = 5
schoolID = 50970

count = 0



while count < 11:
    url = 'https://education.alaska.gov/tls/Assessments/AsmtVer2017/SchoolOverview.cfm?DistrictID={0}&SchoolID={1}&Test=PEAKS'.format(districtID, schoolID)
    print(url)
    response = requests.get(url)
    print(response.text)
    htmlName = str(schoolID) + '.html'
    try:
        filename = open(htmlName, 'r')
    except IOError:
        filename = open(htmlName, 'w')
    with open(htmlName, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=128):
            fd.write(chunk)
    schoolID += 10
    count += 1
