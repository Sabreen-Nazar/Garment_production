
## Garment_production
It is a Garments Productivity Project  - Regression Project



## Data Descrption

1. **date**: Date in MM-DD-YYYY format.
2. **day**: Day of the week.
3. **quarter**: A portion of the month. A month is divided into four quarters.
4. **department**: Associated department with the instance.
5. **team_no**: Associated team number with the instance.
6. **no_of_workers**: Number of workers in each team.
7. **no_of_style_change**: Number of changes in the style of a particular product.
8. **targeted_productivity**: Targeted productivity set by the Authority for each team for each day.
9. **smv**: Standard Minute Value, it is the allocated time for a task.
10. **wip**: Work in progress. Includes the number of unfinished items for products.
11. **over_time**: Represents the amount of overtime by each team in minutes.
12. **incentive**: Represents the amount of financial incentive (in BDT) that enables or motivates a particular course of action.
13. **idle_time**: The amount of time when the production was interrupted due to several reasons.
14. **idle_men**: The number of workers who were idle due to production interruption.
15. **actual_productivity**: The actual percentage of productivity that was delivered by the workers. It ranges from 0 to 1.


# Steps for Deployment

1. Create New environment (open New Terminal -> power shell + -> Command Prompt )

``` 
   python -m venv venv_name

"OR"
   
   conda create -p venv python  -y
```

2. Activate the Environment
```
venv_name\Scripts\activate

"OR"

conda activate venv_name

```

In case of error 
``` 
CALL conda.bat activate

```
and run the conda active code-

*OR*

```
conda activate venv_name

```

3. Install all necessary packages
```
pip install -r requirements.txt

```

4. create app.py file to have FLask Code

5. create template folder and inside templates folder create newfile and name it as home.html 
   In html file have your template design 







