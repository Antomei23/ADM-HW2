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

# RQ 5
# Function to standardize and categorize formats
def categorize_format(format_value):
    if format_value in ['', '17 x 26', 'Beterback', 'Board Book', 'Bolsillo', 'Boxed Set', 'Broché', 'CD-ROM', 'Dwarsligger', 'Econo-clad',
  'Grand format', 'Klappenbroschur', 'Large Print', 'Unbound', 'Unknown Binding', 'Videocassette', 'book', 'large print',
  'unknown format', '創元推理文庫','[large print] /']:                                                                                            #I quitted smoking more than 2 years ago
        return 'Unknown'
    elif format_value in ['Audible Audio', 'Audible MP3 Download', 'Audible.com', 'Audio', 'Audio Book', 'Audio CD', 'Audio Cassette',
 'Audiobook', 'DVD', 'MP3', 'MP3 Book', 'MP3 CD', 'MP3 on CD', 'Playaway', 'Playaway Audiobook', 'Preloaded Digital Audio Player',
 'Preloaded Digital Audio Player with earbuds', 'Preloaded Digital Player', 'audio', 'audiobookAudio Playaway', 'audiobook', 'Audio Playaway']:  #If you guys continue to pass these type of values,
        return 'Audiobook'
    elif format_value in ['Electronic Book', 'Kindle Edition', 'Microsoft Reader Edition', 'Nook', 'Nook ebook', 'ebook', 'kindle', 'Kindle']:
        return 'Ebook'
    elif format_value in ['Fine Binding', 'Flexcover', 'Flipback', 'Hard Cover (gebonden)', 'Hardcover', 'Leather Bound', 'Library Binding',
 'School &amp; Library Binding', 'Slipcased Hardcover', 'Turtleback', 'fine binding', 'hardcover', 'leather bound']:                              #Just kidding
        return 'Hardcover'
    elif format_value in ['Loose Leaf', 'Pamphlet', 'Paperback', 'Paperback &amp; Audio CD', 'Paperback and CD', 'Paperback with flaps',
 'Poche', 'Pocket', 'Rústica bolsillo', 'Soft Cover', 'Tapa blanda', 'Trade Paperback', 'mass market paperback', 'paper', 'paperback'
 , 'جيبي', 'Capa Mole', 'Capa mole','[large print] /Capa mole', 'Mass Market Paperback']:                                                                                  #....
        return 'Paperback'
    else:
        return 'Other'

# Define a function to clean gender column
def clean_gender(gender):
    # Defining the most inclusive gender types based on the values in author['gender']
    valid_genders = ['male', 'female', 'non-binary', 'transgender', 'agender', 'genderqueer', 'genderfluid']

    if gender in valid_genders:
        return gender
    elif gender in ['Male (FtM)', '(He/Him)']:
        return 'male'
    elif gender in ['She/they', 'She/Her/Hers', 'Avocado/She', 'Femme lesbian','Woman', 'Travesti','Tomboy']:
        return 'female'
    elif any(keyword in gender for keyword in ['non', 'nb', 'enby', 'Maverique']):
        return 'non-binary'
    elif gender in ['trans', "lesbian in a man's body ;)"]:
        return 'transgender'
    elif gender in ['androgy', 'Adrogynous','Bigender', 'bigender']:
        return 'androgynous'
    elif gender in ['agender', 'Genderless', 'Gender Neutral', 'Neutrois', 'They', 'Gender Apathetic','neutral','Them','They/Them']:
        return 'agender'
    elif gender in ['queer', 'Genderq', 'Genderqueen']:
        return 'genderqueer'
    elif 'fluid' in gender:
        return 'genderfluid'
    elif gender in ['unknown', 'not specified', '', 'Undefined']:
        return 'not specified'
    else:
        return 'other'
    
# RQ 6
# Function to clean and preprocess publication_date column
def clean_publication_date(date):
  try:

    # If the date is in 'YYYY-MM-DD' format, return it as is
    if len(date) == 10:
        return datetime.strptime(date, '%Y-%m-%d')
    # If the date is in 'YYYY-MM' format, add a default day '01' to it
    elif len(date) == 7:
        return datetime.strptime(date, '%Y-%m')
    # If the date is in 'YYYY' format, add a default month '01' and day '01' to it
    elif len(date) == 4:
        return datetime.strptime(date, '%Y')
    else:
        # Handle other cases as needed, such as filling missing values with a default date
        return None
  except Exception as e:
      # Handle any exceptions that might occur during the conversion
      return None

# Function to calculate probability for each row(book)
def calculate_probability(row):
    total_ratings = row['ratings_count']
    # Handle division by zero
    if total_ratings == 0:
        return 0
    rating_dist = row['rating_dist']
    rating_dict = dict(item.split(":") for item in rating_dist.split("|"))
    num_high_ratings = sum(int(rating_dict.get(str(i), 0)) for i in range(5, 1, -1))
    return num_high_ratings / total_ratings

# Function to calculate probability
def calculate_new_book_probability(group):
    # Sort by publication date in descending order
    group = group.sort_values(by='cleaned_publication_date', ascending=False)

    # Check if there are at least 2 books published
    if len(group) >= 2:
        # Calculate time difference between the last two books
        time_diff = group['cleaned_publication_date'].iloc[0] - group['cleaned_publication_date'].iloc[1]
        # Check if the time difference is less than or equal to 2 years (730 days)
        if time_diff <= timedelta(days=730):
            return 1  # Author published a new book within 2 years
    return 0  # Author did not publish a new book within 2 years

# Function to calculate probability
def calculate_probability_2(row):
    if 'The Worst Books of All Time' in row['title'] and row['num_pages'] > 700:
        return 1  # Book is in the list and has more than 700 pages
    else:
        return 0  # Book is not in the list or does not have more than 700 pages

    