from sys import stdin
import requests
import re
import html
import os
import multiprocessing

print('Podaj stronę od której zacząć ściąganie.')

start = stdin.readline().rstrip('\n')

print('Podaj stronę na której skończyć ściąganie.')

end = stdin.readline().rstrip('\n')

if not os.path.exists('data'):
    os.mkdir('data')

if not os.path.exists('full_data'):
    os.mkdir('full_data')

startCount = ''
endCount = '5000'
sort = 'COUNT'

search_uri = 'http://www.filmweb.pl/search/film?startCount=' + startCount + '&endCount=' + endCount + \
    '&sort=' + sort + '&page='
review_uri = 'http://www.filmweb.pl/reviews/'

film_links_processed = 0
accepted_reviews = 10667


def process_page(i):
    global film_links_processed
    global accepted_reviews
    print('------ PAGE: ' + str(i) + ' ------')
    search_page = requests.get(search_uri + str(i)).text
    film_links = re.findall('id="filmRecommendPageFB" class="hide">(http://www\.filmweb\.pl/.+?)'
                            '/userRecommends#recomm-list', search_page)
    # print(film_links)
    for link in film_links:
        film_links_processed += 1
        # print('\n')
        reviews_uri = link + '/reviews'
        reviews_page = requests.get(reviews_uri).text
        reviews_names = re.findall(
            '<h3 class="s-15"><a href="/reviews/([A-Za-z0-9_~:/?#\[\]@!$&\'()*+,;=`.%-]+)'
            , reviews_page)

        if reviews_names:

            unique_name = str.replace(link, 'http://www.filmweb.pl/', '')

            # print('--- Film: ' + str(film_links_processed) + ' ---')
            # print(unique_name)

            film_name = re.search('v:itemreviewed">(.+?)</a></h1><span class="halfSize">'
                                  , reviews_page).group(1)
            film_name = html.unescape(film_name)

            rating = re.search('<span property="v:average"> (.,.)</', reviews_page)
            if rating is not None:
                rating = rating.group(1)
            else:
                rating = '-1'
            # print(rating)

            for j, name in enumerate(reviews_names):
                reviews_names[j] = review_uri + reviews_names[j]
            reviews_links = reviews_names
            # print(reviews_links)
            for review_link in reviews_links:
                review_page = requests.get(review_link).text
                reviewer_mark = re.search('<span class="s-30"> <span class="normal">(..?)</span>', review_page)
                if reviewer_mark is not None:
                    reviewer_mark = reviewer_mark.group(1)

                    review = re.search('<div class="text text-large normal">(.+?)<div class="centeredContainer">',
                                       review_page).group(1)
                    review = review.replace('<br/>', '\n')
                    review = re.sub('<.*?>', '', review)
                    review = html.unescape(review)
                    accepted_reviews += 1
                    rating = rating.replace(',', '.')

                    full_data = '<unique_name>\n' + unique_name + '\n<film>\n' + film_name + '\n<film_link>\n' + link + \
                                '\n<film_rating>\n' + rating + '\n<review_link>\n' + review_link + \
                                '\n<reviewer_mark>\n' + reviewer_mark + '\n<review>\n' + review

                    data = '<reviewer_mark>\n' + reviewer_mark + '\n<review>\n' + review

                    if not os.path.exists('./data/' + str(accepted_reviews)):
                        with open('./data/' + str(accepted_reviews), 'w', encoding='utf8') as outfile:
                            outfile.write(data)
                    if not os.path.exists('./full_data/' + str(accepted_reviews)):
                        with open('./full_data/' + str(accepted_reviews), 'w', encoding='utf8') as outfile:
                            outfile.write(full_data)

                    print('REVIEW ' + str(accepted_reviews))
                    # print('Reviewer mark: ' + reviewer_mark + '\n')
                    print(film_name)
                    print(review_link)
                    # print(review)
                    # print('\n')


#inputs = range(int(start), int(end)+1)

cpu_count = multiprocessing.cpu_count()
step = 100
for j in range(int(start), int(end)+1, step):
    print('--- Part: ' + str(j) )
    inputs = range(j, j+step)
    pool = multiprocessing.Pool(processes=cpu_count)
    pool.map(process_page, inputs)
    pool.terminate()

#for i in range(int(start), int(end)+1):
#page 22500
