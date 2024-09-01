# Functional Dependencies and Normalization for Relational Databases


- [Functional Dependencies and Normalization for Relational Databases](#functional-dependencies-and-normalization-for-relational-databases)
  - [INTRO](#intro)
  - [1. informal guidelines for designing a relation schema](#1-informal-guidelines-for-designing-a-relation-schema)
    - [1.1 semantics of the attributes](#11-semantics-of-the-attributes)


## INTRO 

Any relational Database are collections of relation schemas and each relation schema  is formed by grouping different attributtes 
. 
> BUT HOW TO DECIDE WHICH ATTRIBUTE GROUP TO SELECT I.E. HOW TO COMPARE DIFFERENT GROUPS OF ATTRIBUTES FOR A RELATION SCHEMA
---
based on diffrent perspectives or choices different design for a smae miniworld can be designed. 

---

 > NOW TO MEASURE THE APPROPRIATENESS OFR GOODNESS OF A SELECTED DESIGN FORA MINIWORLD 

 
 there are to level at which the goodness ofa db designs are evaluated 

| logical or (conceptual) level | implementation level  |
| -------- | -------- |
|  level which describes a relation to the user    | level describes how the  tuples in the  relation schema is stored and updated  |
| having a good design at this level makes the relational schema more easy to understand    | a good implementation design ensures that the database operates efficiently and can scale as needed.  |
| this level is appplied to both base level schemas or views (virtual relations) |  this is applied to base relations (relations which are stored as files|


> the theory  discussed are  base relations 


## 1. informal guidelines for designing a relation schema 

thera are 4 major thinks to keep in mind for designing a relation schema 

- Semantics of the attributes
- Reducing the redundant values in tuples
- Reducing the null values in tuples
- Disallowing the possibility of generating spurious tuples


### 1.1 semantics of the attributes 

a relation schema must be defined in such a way that

- **Clarity of Semantics:** The relation schema should be designed so that the meaning (semantics) of the relation is easily apparent, making it straightforward to understand what the relation represents.

- **Interpretability of Tuples:** The values stored in the tuples of the relation should be easily interpretable, with clear relationships between the attribute values within each tuple.

- **Comprehensive Semantic Representation:** The relation schema should fully account for and clearly represent all the relevant semantics (facts or statements) of the real-world context it models, ensuring that the design has a clear and understandable meaning.

---
---
---

> #### GUIDLINE 1 
>> **Ease of Explanation:** Design the relation schema in a way that makes it easy to explain its meaning.
>
>> **Avoid Combining Different Types:** Do not combine attributes from multiple entity types and relationship types into a single relation.
>
>> **Clarity Through Single Correspondence:** A relation schema that corresponds to one entity type or one relationship type is easier to explain.
>
>> **Avoid Semantic Ambiguities:** If a relation schema combines multiple entities and relationships, it will result in semantic ambiguities, making the relation difficult to explain.

---
---
---
---

| Base Relations | virtual realtions (Views) |
| -------- | -------- |
|Should maintain clarity by focusing on a single entity or relationship type to avoid complexity and ambiguity.|Can integrate data from multiple base relations, combining different entities and relationships as needed to provide meaningful and useful summaries or perspectives on the data.|


