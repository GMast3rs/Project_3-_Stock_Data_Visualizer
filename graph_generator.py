import pygal

def graph_generator(chart_type, dates, prices):
    if chart_type == "Line":
        chart = pygal.Line()
    elif chart_type == "Bar":
        chart = pygal.Bar()
    else:
        print("somehow got the pass chart check invalid chart type")
        return
    chart._title = "test"
    chart.x_labels = dates

    chart.render_in_browser()
