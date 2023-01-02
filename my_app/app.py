from shiny import App, render, ui
import pandas as pd

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.input_file("f", "File"),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        excel_file = pd.ExcelFile(input.f()[0]["datapath"])
        head = excel_file.parse('MaxN').head()
        return head


app = App(app_ui, server)
