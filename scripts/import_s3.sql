-- - create table

drop table emp_basic;
create or replace table emp_basic (
  first_name string ,
  last_name string ,
  email string ,
  streetaddress string ,
  city string ,
  start_date date
  );

create or replace file format my_csv_format
  type = csv field_delimiter = ',' skip_header = 1 null_if = ('NULL', 'null') empty_field_as_null = true compression = gzip;

create or replace stage my_s3_stage url='s3://becloudready/data-analytics'
  credentials=(aws_key_id='<AKIA6ERB5MRO66YMPKO3>' aws_secret_key='<OSmJkK8UMhgPHHQOTqowa6OOLw/FUFKfM0FAcAsk>')
  file_format = (type = csv field_optionally_enclosed_by='"');

copy into EMP_BASIC
  from s3://shuba3/data-analytics credentials=(aws_key_id='<AKIA6ERB5MRO66YMPKO3>' aws_secret_key='<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>')
  file_format = (type = csv field_optionally_enclosed_by='"')
  pattern = '.*employees0[1-5].csv'
  on_error = 'skip_file';

  

copy into EMP_BASIC
  from @my_s3_stage
  file_format = (type = csv field_optionally_enclosed_by='"')
  pattern = '.*employees0[1-5].csv'
  on_error = 'skip_file';
  
snowsql -c example -d sf_tuts -w SF_TUTS_WH -q "select * from EMP_BASIC" -o output_format=csv -o header=false -o timing=false -o friendly=false  > output_file.csv


s3://shuba3/employees01.my_csv
snowsql -c example -d sf_tuts -w SF_TUTS_WH -q "select * from EMP_BASIC" -o output_format=csv -o header=false -o timing=false -o friendly=false  > output_file.csv
