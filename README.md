Google Earth Scraper
This project is a Flask application that uses Selenium to interact with Google Earth, search for a location, and capture a screenshot of the map. The user can enter a city or a keyword in the HTML form, and the application automatically navigates to Google Earth, finds the location, and captures a screenshot.

Important Note: This project is intended as a starting point, and anyone is free to modify, customize, or expand it as they see fit. Currently, the project is limited to taking a screenshot of the map, which might be considered a limited or trivial feature in more complex contexts. The goal is to provide a base from which more advanced or useful functionality can be built, such as map manipulation, interacting with geographical data, or more.

Features
Search for locations on Google Earth: Enter a city or a keyword in the HTML form to search for the location on Google Earth.
Capture screenshot: After finding the location, the application captures a screenshot of the map and saves it as a .png file.
Customizable project: This project is open to any modification or improvement. Anyone can extend its features based on their needs.
Potential Future Enhancements
Implement advanced zoom features or interactions with the Google Earth map.
Add the ability to save multiple screenshots or export geographical data.
Integrate geographical or data visualization APIs.
Improve the user interface to offer more customization options for the search.
Requirements
Python 3.x
Flask
Selenium
Google Chrome and ChromeDriver
Installation
Clone the repository:

bash

git clone <repository-url>
cd <repository-folder>
Install the dependencies:

bash

pip install -r requirements.txt
Download ChromeDriver compatible with your installed version of Chrome, and place it in the directory specified in the code.

Running
Start the Flask server:

bash

python GEarth.py
Open your browser and go to:

arduino

http://127.0.0.1:5000
Enter a city or keyword in the form and wait for a screenshot of the location on Google Earth to be captured.

Project Structure
scss

/GoogleEarth-scraper/
│
├── static/ (Folder for static images, such as screenshots)
│
├── templates/ (Folder for HTML templates)
│   └── index.html (Main HTML page for the user interface)
│
├── GEarth.py (Main code handling Flask and Selenium)
│
├── requirements.txt (File listing the Python dependencies)
How to Contribute
Feel free to modify the code, improve it, or add new features. If you think your improvement could be useful to others, you can create a pull request to this repository.
