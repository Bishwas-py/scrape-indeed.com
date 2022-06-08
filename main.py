import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/viewjob?jk=5f2fbaaa634be72b&from=searchOnHP&tk=1g50rs5ak2mnf003'


def main():
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html5lib')
        title = soup.find('h1').text
        companyInfoContainer = soup.find('div', {'class': 'jobsearch-CompanyInfoContainer'})
        companyName = companyInfoContainer.find('a', {'href': True}).text
        location = companyInfoContainer.find('a', {'href': True}).text
        salaryGuideSoup = soup.find('div', {'id': 'salaryGuide'})
        salaryGuides = [salaryGuide.text for salaryGuide in salaryGuideSoup.find('ul').find_all('li')]
        jobDescriptionText = soup.find('div', {'id': 'jobDescriptionText'}).text
        return {
            'title': title,
            'companyName': companyName,
            'location': location,
            'salaryGuides': salaryGuides,
            'jobDescriptionText': jobDescriptionText,
        }


if __name__ == "__main__":
    print(main())
