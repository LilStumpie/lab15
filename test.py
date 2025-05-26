import requests
import random

def get_hacker_news_fact():
    """
    Получает случайный факт из Hacker News API.
    """
    try:
        # Получаем список ID верхних новостей
        top_stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        response = requests.get(top_stories_url)
        response.raise_for_status()  # Проверяем на ошибки HTTP
        story_ids = response.json()

        # Выбираем случайный ID новости
        random_story_id = random.choice(story_ids)

        # Получаем детали случайной новости
        story_url = f'https://hacker-news.firebaseio.com/v0/item/{random_story_id}.json'
        story_response = requests.get(story_url)
        story_response.raise_for_status()  # Проверяем на ошибки HTTP
        story = story_response.json()

        # Формируем факт о новости
        title = story.get('title', 'Без названия')
        author = story.get('by', 'Неизвестный автор')
        url = story.get('url', 'URL отсутствует')

        fact = f"Интересный факт Hacker News: статья '{title}' написана пользователем {author}. " \
               f"Оригинал статьи можно найти здесь: {url}"

        return fact

    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении факта из Hacker News: {e}"
    except Exception as e:
        return f"Непредвиденная ошибка: {e}"


def display_two_facts():
    """
    Выводит два случайных факта из Hacker News.
    """
    print("Два интересных факта из Hacker News:")
    for i in range(2):
        fact = get_hacker_news_fact()
        print(f"{i+1}. {fact}\n")


if __name__ == "__main__":
    display_two_facts()