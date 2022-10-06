### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  - PostgreSQL is a relational database that allows data to be stored in multiple tables. Various tables will have a relationship to one another

- What is the difference between SQL and PostgreSQL?

  - PostgreSQL uses SQL guidelines

- In `psql`, how do you connect to a database?

  - `\c database_name`

- What is the difference between `HAVING` and `WHERE`?

  - `WHERE` is used to filter records based on a certain condition. `HAVING` is used to filter records from groups based on a condition. `HAVING` must be used after `GROUP BY`

- What is the difference between an `INNER` and `OUTER` join?

  - `INNER` join will return only rows between 2 tables that match. `OUTER` join will return matching rows as well as rows from either table that do not match

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

  - `LEFT OUTER` will join all of the rows from the first table to all of the matching rows from the second table, as well as unmatching rows from the first table. `RIGHT OUTER` will join matching rows from the second table to the rows from the first table as well as unmatching rows from table 2

- What is an ORM? What do they do?

  - Object Relational Mapping allows you to manipulate objects within the language you are using rather than in SQL

- What are some differences between making HTTP requests using AJAX
  and from the server side using a library like `requests`?

  - Using client side requests can be faster in communicating directly with an external API. Server side requests are useful when you need to store or process the data recieved from an external API. Server side requests are also useful when Same-Origin Policy blocks browser requests

- What is CSRF? What is the purpose of the CSRF token?

  - CSRF is Cross-Site Request Forgery, which means a form can be submitted to another site. A CSRF Token prevents this from happening by requiring the submitted form to contain that token before the data is handled.

- What is the purpose of `form.hidden_tag()`?

  - It is used so that additional information such as a CSRF token will be passed with the form, but a user will not be able to see the field
