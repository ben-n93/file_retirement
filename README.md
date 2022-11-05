# File Retirement

A simple command-line tool for deleting old files (based on creation date).

Automate with **crontab** or **Windows Task scheduler** to regularly clean up old files.

No external packages are needed as this only uses modules from the standard library.

## How to use

Call the script from the command line, specifying the directory path of the folder that contains the files you want to delete using the `--d` flag and specifying the file name (or a string that appears in the file name) using the `--f` flag.

Be sure to wrap the directory path in double quotation marks.

Windows
```
$ python file_retirement.py --d "H:\Documents\finance_files_export" --f "monthly_earnings"
```

Mac
```
$ python3 csv_to_snowflake.py --d "Users/ben/finance_files_export" --f "monthly_earnings"
```

## Modifying the script
If you want to delete based on modification time, just update `os.path.getctime(file)` on line 35 to `os.path.getmtime(file)`.

## Warning
Don't pass a string likely to be found in the names of files you don't want deleted. 
