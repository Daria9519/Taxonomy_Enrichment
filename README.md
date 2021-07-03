# Taxonomy_Enrichment
Application of neural network methods for automatic taxonomy enrichment for the Russian language.

The goal is to create methods that automatically enrich any knowledge base with new terms, and at the same time connect them with existing words using Is-A relations. 

The task is to develop a method for prediction the Is-A relations between entities in texts of the Computer Science category. 

![g2](https://user-images.githubusercontent.com/55661759/124359173-0686f600-dc4e-11eb-81ad-c92deb84817e.png)

Train dataset:  the 80 annotated texts:  the 659 observations with the following types of relations: USAGE, PARTOF, SYNONYMS, ISA, COMPARE, CAUSE, NONE. It includes 90 Is-A relations.

Test dataset: the 74 observations with 11 Is-A relations.

An additional data is a dataset that includes 1000 scientific articles on Russian language in Computer Science.

The target of train and test data was converted in bynary, where 1 - Is-A relation, 0 - Other.
