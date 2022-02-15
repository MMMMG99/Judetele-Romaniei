import turtle
import pandas
import time

ecran = turtle.Screen()
ecran.title('Judetele Romaniei')
img = 'romania_judete.gif'
ecran.addshape(img)
turtle.shape(img)
ecran.tracer(0)

date = pandas.read_csv('judete.csv')
numar_judete_corecte = 0
jocul_continua = True
judete_ghicite = []
judete_de_invatat = []

while jocul_continua:
    ecran.update()
    time.sleep(0.1)
    raspuns = ecran.textinput(title=f'{numar_judete_corecte}/{date["judet"].size} Ghiceste judetul',
                              prompt='Care este numele judetului?').title()

    if raspuns == 'Exit':
        for i in range(date['judet'].size):
            if date['judet'][i] not in judete_ghicite:
                stat_de_invatat = date['judet'][i]
                judete_de_invatat.append(stat_de_invatat)
        game_is_on = False
        break

    for i in range(date['judet'].size):
        if raspuns in judete_ghicite:
            continue
        else:
            if raspuns == date['judet'][i]:
                raspuns_corect = turtle.Turtle()
                raspuns_corect.penup()
                raspuns_corect.hideturtle()
                raspuns_corect.color("red")
                raspuns_corect.setpos(date['x'][i], date['y'][i])
                raspuns_corect.write(f'{raspuns}')
                numar_judete_corecte += 1
                judete_ghicite.append(raspuns)

    if len(judete_ghicite) == 41:
        game_is_on = False

date_finale = pandas.Series(judete_de_invatat)
date_finale.to_csv('judete_de_invatat.csv')

ecran.exitonclick()
