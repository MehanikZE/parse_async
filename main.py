import lxml
import requests

from bs4 import BeautifulSoup

user_agent = {'User-agent': 'Mozilla/5.0'}
url ='https://api.hh.ru/vacancies?text=python%20middle&per_page=30'

result = requests.get(url, headers=user_agent)

print(result.status_code)
print(result.text)
j = result.json()
print(j)
print(type(j))
vacans = result.json().get('items')
print(vacans)
for i, vac in enumerate(vacans):
    print(i+1) #vac['name'], vac['url'], vac['alternate_url'])
    s = vac['url']
    # print(s)
    res = requests.get(s, headers=user_agent)
    vacs = res.json()
    m = vacs['name']
    g = vacs['employer']['name']
    z = vacs['description']
    key_skills = vacs['key_skills']
    if key_skills:
        list = []
        for sk in key_skills:
            # list = []
            l = sk['name']
            list.append(l)

            # print(l)
    print(f'Вакансия:',m)
    print(f'Комания:',g)
    print(f'Требования', z)
    print(list)


# user_agent = {'User-agent': 'Mozilla/5.0'}
# result = requests.get('https://voronezh.hh.ru/vacancy/82402579', headers=user_agent)
# print (result)
# a = result.status_code
# print(a)
# b = result.content.decode()
# # print(b)
# soup = BeautifulSoup(result.content.decode(), 'lxml')
# # print(soup.prettify())
#
# v=soup.find('h1')
# # print(v)
# print(v.text)
#
# g = soup.find('a', attrs={'data-qa': 'vacancy-company-name'})
# # print(g)
# print(g.text)
#
# z = soup.find('div', attrs={'data-qa': 'vacancy-description'})
# # print(z)
# print(z.text)