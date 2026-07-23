# Selenium Web Automation using Python #

## Overview

This project demonstrates basic web automation using **Python Selenium WebDriver** with the **Safari browser**. It includes examples of common Selenium operations such as:

- Opening a browser
- Searching on Google
- Clicking buttons and links
- Navigating backward and forward
- Refreshing pages
- Locating elements using XPath
- Extracting product information from Amazon

---

## Technologies Used

- Python 3.x
- Selenium WebDriver
- Safari Browser
- SafariDriver

---

## Prerequisites

Before running the project, make sure you have:

1. Python 3 installed
2. Selenium installed

Install Selenium using pip:

```bash
pip install selenium
```

3. Safari browser

4. Enable Safari WebDriver

Open **Safari** and navigate to:

```
Safari → Settings → Advanced
```

Enable:

- Show Develop menu in menu bar

Then go to:

```
Develop → Allow Remote Automation
```

---

## Project Structure

```
project/
│
├── selenium_demo.py
└── README.md
```

---

## Functions

### `search()`

- Opens Google
- Searches for "selenium"
- Presses Enter
- Waits for 5 seconds
- Closes the browser

---

### `auto()`

Demonstrates browser navigation.

Features:

- Search Google
- Click Search button
- Go Back
- Go Forward
- Close browser

---

### `met()`

Demonstrates searching using a button click.

---

### `link()`

Opens Amazon and clicks:

- Best Sellers
- Audio

using Link Text and Partial Link Text.

---

### `refresh()`

Demonstrates refreshing the current web page.

---

### `xpath()`

Uses XPath to:

- Search for "iphones" on Amazon
- Submit the search

---

### `data()`

Searches Amazon and extracts product names.

**Note:** This function currently contains errors and should use:

```python
find_elements()
```

instead of

```python
find_element()
```

to retrieve multiple products.

---

## Selenium Locators Used

| Locator | Description |
|----------|-------------|
| By.ID | Locate element by ID |
| By.NAME | Locate element by Name |
| By.XPATH | Locate element using XPath |
| By.LINK_TEXT | Locate link by full text |
| By.PARTIAL_LINK_TEXT | Locate link by partial text |

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/selenium-demo.git
```

Move into the project directory:

```bash
cd selenium-demo
```

Run the Python file:

```bash
python selenium_demo.py
```

---

## Improvements

The project can be improved by:

- Replacing `time.sleep()` with `WebDriverWait`
- Adding exception handling
- Using Page Object Model (POM)
- Writing unit tests with `pytest`
- Making the browser configurable (Chrome, Firefox, Edge, Safari)
- Logging execution details

---

## Learning Objectives

This project helps beginners learn:

- Selenium WebDriver setup
- Browser automation
- Web element locators
- Browser navigation
- XPath usage
- Data extraction
- Basic automation workflow

---

## Author

**Mehdi Hassan Sepai**

---

## License

This project is intended for educational and learning purposes.
