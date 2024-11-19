import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

class CurrencyConverterApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input for amount
        self.amount_input = TextInput(hint_text='Enter amount', multiline=False, input_filter='float')
        self.layout.add_widget(self.amount_input)
        
        # Initialize spinners
        self.from_currency_spinner = Spinner(text='From Currency', values=[], size_hint=(None, None), size=(500, 88))
        self.to_currency_spinner = Spinner(text='To Currency', values=[], size_hint=(None, None), size=(500, 88))

        self.layout.add_widget(self.from_currency_spinner)
        self.layout.add_widget(self.to_currency_spinner)

        # Convert button
        self.convert_button = Button(text='Convert')
        self.convert_button.bind(on_press=self.convert_currency)
        self.layout.add_widget(self.convert_button)

        #Display the converted amount
        self.result_label = Label(text='Converted amount will appear here')
        self.layout.add_widget(self.result_label)

        # Fetch exchange rates to populate currencies
        self.fetch_exchange_rates()

        return self.layout

    def fetch_exchange_rates(self):
        api_key = 'YOUR_API_KEY'  # Replace with your API key
        url = f'https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD'  # Use your actual API key

        response = requests.get(url)
        if response.status_code != 200:
            self.result_label.text = "Error fetching data from the API."
            print(f"Error fetching data: {response.status_code}")
            return

        data = response.json()
        self.currencies = list(data['conversion_rates'].keys())
        self.conversion_rates = data['conversion_rates']

        # Populate spinners with currency options
        self.from_currency_spinner.values = self.currencies
        self.to_currency_spinner.values = self.currencies
        print(f"Available currencies: {self.currencies}")  

    def convert_currency(self, instance):
        try:
            amount = float(self.amount_input.text)
            from_currency = self.from_currency_spinner.text
            to_currency = self.to_currency_spinner.text

            print(f"From Currency: {from_currency}, To Currency: {to_currency}")  

            if from_currency == 'Select From Currency' or to_currency == 'Select To Currency':
                self.result_label.text = "Please select both currencies."
                return

            if from_currency not in self.conversion_rates or to_currency not in self.conversion_rates:
                self.result_label.text = "Currency not found."
                return

            # Conversion formula
            converted_amount = amount * (self.conversion_rates[to_currency] / self.conversion_rates[from_currency])
            self.result_label.text = f'Converted Amount: {converted_amount:.2f} {to_currency}'
        except ValueError:
            self.result_label.text = "Please enter a valid amount."

try:
    CurrencyConverterApp().run()
except Exception as e:
    print(f"Unexpected error: {e}")
