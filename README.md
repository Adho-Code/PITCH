## Pitch

## PITCH PROJECT
Pitcher is an application which enables one to pitch a certain category and can comment on it!

##The link to the website is

## Features!
* Adding a pitch category to the site
* Commenting on other people's pitches and having an insight
* Login and signup sheets


You can also:

* Making your own pitch
* Liking and disliking but with bugs
* Saving a favourite
* The overriding design goal for The pitcherapp is to place people in the context of global understanding in the pitches piched in the world

# Technology used
Python uses a number of open source projects to work properly:

* HTML
* CSS
* Python
* Twitter Bootstrap
* flask
* Installation
* To start application we first

`$ git clone https://adhoadhi.github.io/PITCH/`

# Install the dependencies which are :

`python3.6 -m venv --without pip virtual`
`$ pip install -r requirments.txt`
`$ chmod a+x start.sh`
`$ ./start.sh`

## For production environments...
`$ python manage.py server`

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display pitch categories | **On page load** | List of various categories of pitches |
| Display pitches | **On page load** | Pitch displays author, title, pitch, date comment tab |
| To add a pitch  | **Click an add pitch** | Redirected to the pitch collection form|
| Display category | **On Tab link click** | Clickable links to open pitches by category |
| Display profile | **Click profile page** | Redirected to a page with your profile |