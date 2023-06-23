from bs4 import BeautifulSoup #3.9.5 64-bit
#pip install bs4
#https://www.youtube.com/watch?v=XVv6mJpFOb0 10:28

with open('home.html', 'r') as html_file:
    content = html_file.read()
    

    soup = BeautifulSoup(content, 'lxml')
#    courses_html_tags = soup.find_all('h5')
 #   for course in courses_html_tags:
  #      print(course.text)
    course_cards = soup.find_all('div', class_='card') #needs to be class_ beacuse of python and also to identify it in the other code
    for course in course_cards:
#Find the class which signifies a certain thing...
#This means you have to look at the code and figure out what class a certain aspect is... for example <a> is money
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')


