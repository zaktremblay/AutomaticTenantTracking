# AutomaticBudgetGoogleSheets

This automatic budget sheet has been done to track and verify tenant payments and expenses for a real estate renting business that I plan on having. Around 70% of the programming has been done with Google Sheets' dynamic functions, which update automatically without the need for the press of a button like an Excel macro would. 25% of the programming uses Python, which uses the mintapi library, used to scrape mint with transaction data, and the g2spread library, used to input the data into the google sheet that holds the interface. The remaining 5% is the maintenance of the link between the Python code written and the google sheet, which is performed by enabling google sheet's API from the Google Cloud Platform. The only parts of the program that require manual input are the tenant details. To refresh the data, I run the python script periodically. This process is soon to be automated as well.

---
This project holds features such as:
- Expected payment date for each tenant and each unit
- Confirmation on the status of the payment for each day (late or on time)
- Expected occupancy of each unit
- Payment graphics
- Expense graphics
- Marketing details graphics
---
The point of the entire project was to have a reliable interface on which to see all of the accounting details of the tenant stays. It would also be useful to have it be as automatic as possible in order to facilitate the management of new tenants and tenant archives.
For example, here is the interface for the unit occupancy, where each color has a different meaning (Orange:Late, Yellow:Double-booked, Dark-Green:Payday, etc...):
![Image](Capture.JPG)
Here is an example of the graphics:
![Image](Capture2.JPG)

---
Here is a list of features yet to add:
- A net worth over time calculator
- A cash reserves over time calculator
- A redundancy for importing data using BudgetSheets (Google Sheets add-on)
- Automatic periodic run of the Python script to refresh the data
