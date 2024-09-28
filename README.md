### 2. The Perfect Arrangement
Write a query to print the id, first_name and last_name. To filter the names, concatenate the first and last names to create a combined name. Return the names of customers whose combined names are less than 12 letters long. Sort the results by their combined name lengths, then alphabetically, case insensitive, by combined name, then by id. All sorts are ascending.
![image](https://github.com/user-attachments/assets/6ff7acdf-2ef8-4df0-9cb6-75ea6ce7fab0)
Answer : 

````
SELECT ID, FIRST_NAME, LAST_NAME
FROM CUSTOMER
WHERE LENGTH(CONCAT(FIRST_NAME, LAST_NAME)) < 12
ORDER BY LENGTH(CONCAT(FIRST_NAME, LAST_NAME)), 
         CONCAT(FIRST_NAME, LAST_NAME) COLLATE utf8mb4_unicode_ci, 
         ID;
````

### 3 Are you an expert on data structures?
Which of the following data structures can erase from its beginning or its end in O(1) time?
![image](https://github.com/user-attachments/assets/5881cd51-248c-47f3-8561-b4e6bb9f7b68)
### The correct answer is ```` deque````.
