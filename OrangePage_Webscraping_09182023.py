from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.orangepage.net/recipes/search?utf8=%E2%9C%93&search_recipe%5Bkeyword%5D=%E3%81%AB%E3%82%93%E3%81%98%E3%82%93')
soup = BeautifulSoup(res.text, 'html.parser')
#text = soup.h2.string #only the first one can come out.

#h2_tit_tags = soup.find_all('h2', class_='tit')
#h2_tit_str = [x.string for x in h2_tit_tags]

#print(h2_tit_str)

#print([x for x in h2_tags[27].stripped_strings])
#text = tag_obj.string

#print(h2_tags[27])

#recipes = soup.find('div', id='recipe_list', class_='recipesList')
#h2_tit_tags = recipes.find_all('h2', class_='tit')
#print([x.string for x in h2_tit_tags])


recipes = soup.find('div', id='recipe_list', class_='recipesList')
a_tag = recipes.find_all('a')
print([x['href'] for x in a_tag])
