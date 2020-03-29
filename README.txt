FlexiRankColleges Interface by Team Uno:

	Christian Laggui
	Parth Merchant
	Timeer Mehta

Getting Started
	
	Prerequisites:
		Python Tkinter: https://tkdocs.com/tutorial/install.html

	Installing:
		Unpack zip file

	Deploying:
		-In command prompt or terminal, move current working directory into same location as FRC.
		-In terminal execute the following command:
			python menu.py

FlexiRankColleges (FRC) Interface

This interface was implemented using Python's tkinter interface. We loaded the .csv files, from the years 2006-2017, to allow the user to look at 11 academic years of data. The initial form (menu.py) allows the user to add in their preferences, such as what states they want to see, the year they want to look at, the attribute they want to rank on, and what the minimum and maximum SAT scores, admission rates and cost of attendance the user wants to see.

That data is then sent as arguments to the interface file (main.py) as a filtered .csv file, the attribute that the user wants ranked and the year that is being displayed. That information is then used to create a bar chart and table, which will display the data on the interface. 


	
	