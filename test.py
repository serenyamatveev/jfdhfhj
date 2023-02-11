from pywebio.input import input
from pywebio.output import put_text

name = input("Как вас зовут: ")
age = input("Сколько вам лет: ")

put_text(f"Привет {name}!\nТебе уже {age} лет!")