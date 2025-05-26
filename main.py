from tkinter import *
import requests
import random

root = Tk()
root['bg'] = '#fafafa'
root.title('HackerNews Facts')
root.geometry('1400x720')
root.resizable(width=False, height=False)
frame_first_fact = Frame(root, bg = '#ffb700', bd = 5)
frame_first_fact.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.5)
frame_second_fact = Frame(root, bg = '#ffb700', bd = 5)
frame_second_fact.place(relx = 0.05, rely = 0.7, relwidth=0.9, relheight=0.2)
fact_1 = Label(frame_first_fact, text='Факты', bg='#ffb700', font = 1)
fact_1.pack()
def get_fact():
    story = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    res = requests.get(story)
    story_ids = res.json()
    rand_story_id = random.choice(story_ids)
    story_url = f'https://hacker-news.firebaseio.com/v0/item/{rand_story_id}.json'
    story_res = requests.get(story_url)
    story_fin = story_res.json()

    title = story_fin.get('title')
    author = story_fin.get('by')
    url = story_fin.get('url')

    fact = f'Факт из HackerNews: {title}, написанная {author}. \n Ссылка на статью - {url}'
    return fact

def button():
    text = ''
    for i in range(2):
        text += get_fact() + '\n' + '\n'

    fact_1['text'] = text

btn = Button(frame_second_fact, text= 'Get two random facts', command = button)
btn.pack()

root.mainloop()
