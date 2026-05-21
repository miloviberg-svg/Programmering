from nicegui import ui

def calculate_fahrenheit(celsius):
    if type(celsius) is not float:
        return
    
    celsius = float(celsius)
    fahrenheit = (celsius * 1.8) + 32
    fahrenheit = round(fahrenheit, 1)
    fahrenheit_label.text = f"Det blir: {fahrenheit}"
ui.label("Celsius till fehrenheit")
ui.input("Celsius",
        on_change= lambda e: calculate_fahrenheit(e.value))
fahrenheit_label = ui.label("...")

ui.run(native=True)