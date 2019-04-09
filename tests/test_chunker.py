import csv
import gibberish
import pytest
import pytest_mock
import random

from plastictap.chunker import CSVChunker

#
# File Operation Errors
#

# create input csv with random columns, rows and values
@pytest.fixture(scope="function")
def random_feeder_data_csv_path(tmpdir):
    # reset the rng seed
    random.seed()

    # select a random number of columns
    num_columns = random.randint(3, 20)

    # select a random number of rows
    num_rows = random.randint(10000, 50000)

    # write csv file (note: we dont care what the header is so every row will be random)
    with tmpdir.mkdir('test_csv').join('test_feeder_data.csv') as csv_file:
        csv_writer = csv.writer(csv_file)

        # write rows
        for _ in num_rows:
            row = gibberish.generate_words(num_columns)
            csv_writer.writerow(row)

    # return the filename
    return csv_file.abspath()


# handle input csv doesnt exist
def test_input_csv_doesnt_exist_throws_exception(mocker):
    m = mocker.patch('builtins.open', mocker.mock_open())
    m.side_effect = FileNotFoundError("file not found! (test_input_csv_doesnt_exist_throws_exception)")
    with pytest.raises(Exception) as e:
        chunker = CSVChunker(chunks=5, csv_path='test.csv')
        chunker.write_chunks()

    assert 'input CSV' in str(e.value)


# handle unable to open input csv

# handle read error on inputcsv

# handle unable to open output csv

# handle write error on output csv

#
# Chunking Process
#

# verify output has correct format (header, columnar format, etc)

# verify output chunks have equal number of lines (+/-1 for the last chunk)

# verify output chunks contain all data from input csv
