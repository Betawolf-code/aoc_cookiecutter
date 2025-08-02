## Cookiecutter template for Advent of Code

This template for cookiecutter automatically sets up a project for a day (by default, the current day) in an Advent 
of Code year of your choosing. It then downloads the input data (provided you have your session cookie defined in an 
environment variable) and puts the story of the puzzle in the Python script for the first assignment. It also 
extracts the testdata from the story and puts it in a script called `inputdata.py` in the project package.

### Usage

#### 1. Download your session cookie
First, make sure you have your session cookie defined as an environment variable `AOC_SESSIONCOOKIE`. You can find 
the cookie in your browser, when you open the page `https://adventofcode.com/` and you login with your credentials. 
Using developer tools. 

Firefox
: Click the three horizontal lines to the right of the address bar, choose More Tools > Web Developer Tools. Then 
select Storage from the toolbar of the developer tools and Cookies from the left menu. The session cookie will show 
up.

Edge
: Click the three dots to the right of the address bar, choose More
Tools > Developer Tools. Then click the icon that looks like an
application window (called 'Application') and select Cookies from
the menu on the left. The session cookie shows up.

Chrome
: Open Chrome DevTools, then select Application > Storage > Cookies
and the session cookie will show up.

#### 2. Create an environment variable of the cookie

Copy the value of the cookie (a 135 character string, at least for me) and create an environment variable on your 
machine.

Linux
: Edit your `.bashrc` file, enter somewhere at the bottom `export AOC_SESSIONCOOKIE=xxx`, where you put the value of 
your session cookie instead of the `xxx`

Windows
: Open your Start menu and type `environment`. You'll see some option appearing in the Start menu. Select `Edit 
environment variables for your account`. Add a new environment variable called `AOC_SESSIONCOOKIE` and give it the 
value you copied from your browser.

#### 3. Execute the cookiecutter

Create a folder for all the days of Advent of Code. I've got one for each year. **Inside that folder**, you execute
```bash
cookiecutter https://github.com/Betawolf-code/aoc_cookiecutter
```
and answer the questions. A folder with the number of the day (e.g. day01) will be created containing your code.


Start hacking your solution!
