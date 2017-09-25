import urllib
from pathlib import Path
import os
import pandas as pd


def data_by_year(year):
    file_name = '{}.csv.bz2'.format(year)
    return pd.read_csv(file_name, sep=',', encoding='latin1', nrows=50000)


def download_csv_by_year(year):
    file_name = '{}.csv.bz2'.format(year)
    file_downloaded = Path('{}/{}'.format(current_dir(), file_name))

    if not file_downloaded.exists():
        print('downloading file for year: {}'.format(year))
        url = 'http://stat-computing.org/dataexpo/2009/{}'.format(file_name)
        urllib.request.urlretrieve(url, file_name)
    else:
        print("file exists")


def current_dir():
    return os.getcwd()


def percentaje_cancellation(year):

    print("processing data for year:" + str(year))

    df = data_by_year(year)
    total_fligths = len(df.index)
    cancelled_fligths = df.query('Cancelled==1')
    num_cancelled_fligths = len(cancelled_fligths)
    return (num_cancelled_fligths / total_fligths) * 100


def year_data(year):
    return {
        'year': year,
        'percentajeCancellation': percentaje_cancellation(year)
    }

if __name__ == '__main__':

    cancelled_fligths_by_year = []

    for year in range(1999, 2004):
        download_csv_by_year(year)
        cancelled_fligths_by_year.append(year_data(year))

    cancelled_fligths_data = pd.DataFrame(cancelled_fligths_by_year)

    print("Ratio of cancelled fligths per year 99-03")
    print(cancelled_fligths_data)

