create or replace function add5 (n number)
  returns number
  as 'n + 5';

create or replace function add5 (s string)
  returns string
  as 's || ''5''';

  create function area_of_circle(radius float)
  returns float
  as
  $$
  pi() *radius *radius
  $$
  ;

  select area_of_circle
  