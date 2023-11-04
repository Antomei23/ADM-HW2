# RQ 3
months = {'01':'January', '02':'February', '03': 'March', '04':'April', '05': 'May', '06':'June',
           '07': 'July', '08': 'August', '09':'September', '10':'October', '11': 'November', '12':'December'}

def func_year(df, year):
    import pandas as pd

    df_row = df[df['pub_year']==year]

    # number of books published in the year
    num_books_per_year = df_row.groupby(['id'])[['id', 'title','author_name']].agg('sum')
    books_in_year = len(num_books_per_year['id'].values)

    # number of pages published in the year
    num_pages_per_year = df_row.groupby(['id'])[['id', 'title','author_name','num_pages']].agg('sum').sort_values(by= 'num_pages',ascending=False )
    pages_in_year = sum(num_pages_per_year['num_pages'].values)
    
    # the longest book written in the year
    longest_book = num_pages_per_year.title.values[0]
    
    # the most prolific month of the year (the month with more books)
    num_books_per_month = df_row.groupby(['pub_month'])[['id']].agg(tot_books=pd.NamedAgg(column='id', aggfunc='count')).sort_values(by= 'tot_books',ascending=False )  
    prolific_month = months[num_books_per_month.index[0]]
    
    return books_in_year, pages_in_year, longest_book, prolific_month

#RQ 4
def dictionary_for_authors(df, col_id, col_title,  list_of_auth):
    res = {}
    for auth in list_of_auth:
        res[auth] = list(df[df[col_id]==auth][col_title].values)
    return res

def find_longest_title(lista):

    longest = ''
    for el in lista: 
        for libro in el:       
            if len(libro) > len(longest):
                longest = libro
    return longest