
# Currency Converter App

A **Currency Converter** application built with **Kivy** and **Python**. This app allows users to convert amounts between various currencies using real-time exchange rates fetched from an API.

---

## Features
- User-friendly interface for currency conversion.
- Select source and target currencies from dropdown menus.
- Input the amount to convert.
- Displays the converted amount instantly.
- Fetches live exchange rates from the **ExchangeRate API**.

---

## Prerequisites
Before running the app, ensure the following are installed on your system:
- Python 3.6+
- Kivy framework
- Requests library

---

## Installation

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/ErwinBiju/currency-converter-app.git
   cd currency-converter-app
   ```

2. Install the required Python packages:
   ```bash
   pip install kivy requests
   ```

3. Replace the placeholder API key in the code with your actual API key:
   ```python
   api_key = 'YOUR_API_KEY'  # Replace with your API key
   ```

   You can obtain a free API key from [ExchangeRate-API](https://www.exchangerate-api.com/).

---

## Usage

1. Run the application:
   
2. Enter the amount to convert in the text input field.

3. Select the **source currency** ("From Currency") and **target currency** ("To Currency") from the dropdowns.

4. Click the **Convert** button to see the converted amount displayed.

---

## Files in the Project

- `currency_converter.py`: The main application script.

---

## Troubleshooting

- If the dropdown menus do not populate, ensure that:
  1. You have replaced the API key in the code.
  2. You are connected to the internet.
  3. The API is responding correctly.

- If you encounter any errors, check the console logs for details.

---

## Acknowledgments
- [Kivy](https://kivy.org) for the GUI framework.
- [ExchangeRate-API](https://www.exchangerate-api.com/) for live currency exchange rates.
