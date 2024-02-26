import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Change the image name pattern in this function
def create_filename(x):
    """
    Create a standardized filename based on input data.

    Args:
        x (dict): A dictionary containing information to construct the filename.

    Returns:
        str: The constructed filename in the format "{id}__{sample_name}__{quantity}".

    Example:
        input_data = {
            'id': 123,
            'sample_name': 'Acetaminphen Codeine',
            'quantity': 5
        }
        filename = create_filename(input_data)
        # Resulting filename: "123__acetaminphen-codeine__5"
    """    
    # Convert `sample_name` to lowercase and replace spaces with hyphens
    transformed_name = x['sample_name'].lower().replace(' ', '-')
    
    # Create the filename
    #fname = f"{x['id']}__{transformed_name}__{x['quantity']}__{x['image_hash']}.png"
    fname = f"{x['id']}__{x['sample_id']}__{transformed_name}__{x['quantity']}.png"
    
    return fname

def get_iso8601_datetime():
    import pytz
    from datetime import datetime
    
    # Create a datetime object for the current time
    current_time = datetime.now()

    # Set the timezone to UTC
    current_time_utc = current_time.replace(tzinfo=pytz.UTC)

    # Format the datetime in ISO 8601 format
    iso8601_datetime = current_time_utc.strftime('%Y-%m-%dT%H:%M:%S%z')

    return iso8601_datetime

def standardize_names(name):
    return name.lower().replace(' ', '-')

def show_by_camera_type(df, sample_id):

    # select samples by sample_id    
    samples = df[df['sample_id'] == sample_id]

    # setup for ipyplot
    label_column = 'camera_type_1'
    images = samples['url'].values
    labels = samples[label_column].values
    labels_list_filtered = samples[label_column].unique().tolist()
    
    # Show with tabs
    ipyplot.plot_class_tabs(
        images, labels, tabs_order=labels_list_filtered, show_url=False,
    )

def list_url_by_camera_type(df, sample_id):
    samples = df[df['sample_id'] == sample_id]
    for _,sample in samples.iterrows():
      print(f"{sample['id']}\t{sample['sample_name']}\t{sample['camera_type_1']}\t\t{sample['quantity']}\t{sample['url']}")


def get_heatmap_table(df, rows, cols, values, rows_order = None):
    import pandas as pd 
    df_cat = df.copy()    
    df_cat[rows] = pd.Categorical(df_cat[rows])
    df_cat[rows] = df_cat[rows].cat.set_categories(rows_order) 
    df_cat.sort_values([rows], inplace=True)
    table = df_cat.pivot(index=rows, columns=cols, values=values)
    return table
    
def show_heatmap_tables(table1, table2, save_name= None, figsize=(18, 8)):
    #plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig, axes = plt.subplots(1, 2, figsize=figsize)

    sns.heatmap(table1, annot=True, annot_kws={"size": 9}, fmt='g', cmap='Blues', linewidths=.4,  ax=axes[0])
    sns.heatmap(table2, annot=True, annot_kws={"size": 9}, fmt='g', cmap='Blues', linewidths=.4,  ax=axes[1])
    plt.show()
    if save_name: fig.savefig(save_name, bbox_inches='tight')    
    
def show_heatmap(df, rows, cols, values, rows_order = None, save_name= None, figsize=(6, 6)):
    import pandas as pd 
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    df_cat = df.copy()
    df_cat[rows] = pd.Categorical(df[rows], rows_order)
    table = df_cat.pivot(index=rows, columns=cols, values=values)
    
    fig, _ = plt.subplots(figsize=figsize)
    sns.heatmap(table, annot=True, annot_kws={"size": 9}, fmt='g', cmap='Blues', linewidths=.4)
    plt.show()
    if save_name: fig.savefig(save_name,bbox_inches='tight') 
    

def check_duplicates_by_hash(df):
    num_samples = df['url_status_code'].isin([200]).sum()
    x = df.groupby(['hashlib_md5']).size().reset_index(name='counts')
    one_sample_hash = x[x['counts']==1]
    two_more_sample_hash = x[x['counts']>1]

    if len(one_sample_hash.index) < len(x.index):
        print('Summary:')
        print(f"Total unique hash codes : {len(x.index)}")
        print(f"Total of hash code with one sample: {len(one_sample_hash.index)}")
        print(f"Total of hash code with two or more samples: {len(two_more_sample_hash.index)}")
        
        print('')
        print(f"Total of samples: {num_samples}")
        print(f"Total of samples without duplicates: {len(x.index)}")
        print(f"Total of samples in some duplicate case (will be deleted): {num_samples-len(x.index)}")

        return two_more_sample_hash

    else:
        print('There is no duplicates.')
        return 0