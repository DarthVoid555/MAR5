from flask import Flask, url_for


app = Flask(__name__)
@app.route('/')
def nothnig():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(list)

@app.route('/image_mars')
def mars_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">'''
                    <h3>Вот она какая, красная планета.</h3>
                  </body>
                </html>"""
@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Колонизация</title>
                    <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                  </head>
                  <body>
                    <h2>Жди нас, Марс!</h2>
                    <img src="{url_for('static', filename='img/MARS_lidl.png')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    <br/>
                    <gy>Человечество вырастает из детства</gy><br/>
                    <gn>Человечеству мала одна планета</gn><br/>
                    <gy>Мы сделаем обитаемыми безжизненные пока планеты</gy><br/>
                    <y>И начинаем с Марса!</y><br/>
                    <r>Присоединяйся!</r><br/>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
