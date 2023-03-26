CREATE OR REPLACE PROCEDURE get_products()
language plpgsql    
as $$
begin
	SELECT * FROM public."Product"
	commit;
end;$$