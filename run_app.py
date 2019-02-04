import app.load_file_helper as hlp

file_path = hlp.process_args()

print(file_path)

row_header = hlp.get_header_row(file_path)

print(row_header)
results = hlp.load_file_to_table(file_path)
print(f"File load summary: Records Inserted:- {results[1]}, Rows in Table:- {results[0]}" )