#FIXME: cor branca em hexadecimal
#584BD5
import flet as ft
def main(page:ft.Page):
    #RED GREEN BLUE
    #YELLOW
    page.bgcolor = "#988908"

    linha1 = ft.Row(
        controls=[
            ft.Text("Sabadão da programação 1")
        ]
    )
    linha2 = ft.Row(
        controls=[
            ft.Text("Sabadão da programação 2")
        ]
    )
    linha3 = ft.Row(
        controls=[
            ft.Text("Sabadão da programação 3")
        ]
    )
    mensagem = ft.Text()
    def btn_click(e):
        mensagem.value = "Sabadão no Flet aplicando Cor"
        btn.bgcolor = "YELLOW"
        btn.color = "BLACK"
        page.update()
    btn = ft.ElevatedButton("Clique aqui!",color="WHITE",bgcolor="RED",on_click=btn_click)
    page.add(linha1, linha2, linha3,btn)
    page.update()

ft.app(target=main)