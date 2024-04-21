# import psycopg2 
# import csv

# data = {
#     "host": "localhost",
#     "port": 5432,
#     "database": "education",
#     "user": "postgres",
#     "password": "postgres"
# }

# try:
#     connection = psycopg2.connect(**data)
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM people_data WHERE age > 16 ORDER BY age;")
#     people_data = cursor.fetchall()
#     file_name = "people_data.csv"

#     with open(file_name, "w", newline='',encoding='utf-8') as csv_file:
#         writer = csv.writer(csv_file)
        
#         for i in people_data:
#             writer.writerow(i)


# except psycopg2.Error as e:
#     print(f"Error: {e}")
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("postgres yopildi")
import requests
import multiprocessing
import time
from bs4 import BeautifulSoup

start = time.perf_counter()

text_urls = [
    'https://uz.wikipedia.org/wiki/Arslon',
    'https://bank.uz/currency#RUB',
    'https://www.bbc.com/news'
]

def write_text(url):
    try:
        response = requests.get(url)
        result = BeautifulSoup(response.content, 'html.parser') 
        text_content = result.get_text()  
        file_name = f"{url.split('/')[-1]}.txt"
        with open(file_name, "w", encoding="utf-8") as text_file:
            text_file.write(text_content)
            print(f"{file_name} kochirildi")
    except Exception as e:
        print(f"Error {url}: {e}")

threads = []
if __name__ == '__main__':
    for url in text_urls:
        thread = multiprocessing.Process(target=write_text, args=[url])
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

end = time.perf_counter()
print(f"{end - start} second")