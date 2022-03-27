# Datathon-vs-Racism-2022

[Open colab](https://colab.research.google.com/drive/14SvMVg6vzlKjLmPJA0g91RQsoXRT4kjj)

Datathon Against Racism - BCN Analytics 2022

[Trello](https://trello.com/b/rMKoZ5Y0/datathon-against-racism)

## Insights

* Topics like economy + racism would not be reflected in tweets datasets since the Twitter API gives 1% of a non-representative universe of tweets. Furthermore, when searching tweets, only using an Academic Account is possible to retrieve all tweets, but for Essential and Expanded accounts is only allowd a 10-days window, producing inherent bias that cannot be solved in an easy way.
* We should classify `unknown` in labels predicted by BETO and then add them to training, identifying by a special tag.
* Generating new classifications to see if non classified models are falling in the **mild** cases or non-consensus cases.
 

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


