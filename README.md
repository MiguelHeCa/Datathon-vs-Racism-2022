# Datathon-vs-Racism-2022

[Datathon Against Racism - BCN Analytics 2022](https://bcnanalytics.com/datathon/)

Group name: **!Another DS Group**

(Not Another Data Science Group)

Winners of Best Insights!!!! 

## MVP at Hugginface

[BETO model sample](https://huggingface.co/jaumefib/datathon-against-racism)

## Insights

* A lot of doubt in defining what is racism even by professionals.
* In Spain racism seems to be related with immigration while in LatinoAmerica racism is associated with discrimination by race.
* The nationality that is most discriminated is moroccan and there is a general negative attitude towards muslims.
* People of discriminated nationalities are recurrently associated by Spaniards to violence, illegal immigration, illegal house occupants and poverty.
* Better division of train/val/test data.


## Rules for analysing consensus

| Case                 | Label             |
|----------------------|-------------------|
| All racist           | Strong racist     |
| Racist ~ non-racist  | Mild racist       |
| Racist > non-racist  | Mild racist       |
| Racist + unknown     | Mild racist       |
| Racist < non-racist  | Mild non-racist   |
| Non-racist + unknown | Mild non-racist   |
| All non-racist       | Strong Non-racist |
| All Unknown          | Unknown           |


