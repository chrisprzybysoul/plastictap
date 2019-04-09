import csv


class CSVChunker:
    def __init__(self, chunks, csv_path):
        self.chunks = chunks
        self.csv_path = csv_path

    def write_chunks(self):
        try:
            with open(self.csv_path) as csv_file:
                # this is all the functionality we got tests written for
                pass
        except Exception as e:
            raise Exception("Could not open input CSV: {}".format(e))
