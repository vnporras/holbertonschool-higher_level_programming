#!/opt/homebrew/bin/python3
import requests, csv

def fetch_and_print_posts():
    response_post = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response_post.status_code}")

    if response_post.status_code == 200:
        parsed_data = response_post.json()

        for post in parsed_data:
            print(post['title'])


def fetch_and_save_posts():
    response_post = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response_post.status_code}")

    if response_post.status_code == 200:
        parsed_data = response_post.json() 
        
        with open('posts.csv', 'w', newline='') as csvfile:
            field_names = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)

            writer.writeheader()

            for post in parsed_data:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body' : post['body']})
    