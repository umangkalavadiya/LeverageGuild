
# LeverageGuild

A Django based web application which using machine learning regression model to predict the output which is especially designed for students to make their admission and univesity selection procedure completely conspicious. furthmore, it helps them in a wide range of feature as showing their chances of getting into their dream university, handing out an essay outline through OpenAi, also it nudges students by sending them scholarship deadline updates. Agglomerating it is a one stop shop which has a crisp delivery to otherwise fussed up students.

Installation Steps(Windows): 
Perform the following steps in order to install the Project onto your System: 

Step 1: Create Virtual Environment: 
```bash
  python -m venv env
```

Step 2: Activate the Environment:  
```bash
env\Scripts\Activate.bat
``` 

Step 3: Clone 
```bash
git clone https://github.com/umangkalavadiya/LeverageGuild.git
``` 
Step 4: Install all the Packages: After Activating the Virtual Environment. For installing all the packages used for the development of this project (Note: requirements.txt will be included in the project folder.).
```bash
 pip install -r requirements.txt
 ```

Step 5: Run the below command to makemigrations
 ```bash
 python manage.py makemigrations
 ```
Step 6: Run the below command to migrate
  ```bash
 python manage.py migrate
 ```
Step 7: Run the below to start the server
  ```bash
 python manage.py runserver
 ```
