import pandas as pd


#read in the data to pandas dataframe
marriage = pd.read_excel('state-marriage-rates-90-95-99-17.xlsx',
                         skiprows = 5,              #skips first 5 rows of excel sheet
                         skipfooter = 8,            #skips last 8 rows of excel sheet
                         na_values = '---',         #empty values are "---" in excel sheet
                         index_col=0)               #index column stays at 0


#pivot "Marriage rate" into its own column
marriage = marriage.stack()

#last column gets header of "Marriage Rates"
marriage.name = 'Marriage Rates'


#cleans and reshapes
#drop rows that have all null values
marriage.dropna(how = 'all', inplace = True)


#index names are changed to "State" (first column) and "Year" (second column)
marriage.index.names = ['State', 'Year']


#dataframe to excel file
marriage.to_excel(excel_writer='marriage_rates_clean.xls',           #name the excel file to "marriage_rates_clean"
                sheet_name = 'Marriage Rates by State',              #name the excel sheet "Marriage Rates by State"
                na_rep = 'null')                                     #treat "---" as "null"












